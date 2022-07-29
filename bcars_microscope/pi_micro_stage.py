from pipython import GCSDevice
from time import sleep
import traceback

from bcars_microscope.devices import AbstractStage
from bcars_microscope.ui.ui_bcars2_pi_macro import Ui_Dialog as Ui_MacroStage

from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtCore


QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)


class DialogMacroStage(QDialog):
    def __init__(self, macrostage):
        # Boilerplate stuff
        super().__init__()
        self.ui = Ui_MacroStage()
        self.ui.setupUi(self)
        self.macrostage = macrostage

        if self.macrostage is not None:
            self.populate_ui()

        # Signals and Slots
        self.ui.spinBoxVelocity.editingFinished.connect(self.change_settings)
        self.ui.spinBoxAcceleration.editingFinished.connect(self.change_settings)

    def populate_ui(self):
        """ Populate the UI and set current values"""
        vel = self.macrostage.get_velocity()['1']
        self.ui.spinBoxVelocity.setValue(vel)
        acc = self.macrostage.get_acceleration()['1']
        self.ui.spinBoxAcceleration.setValue(acc)

    def change_settings(self):
        sender = self.sender()

        if sender == self.ui.spinBoxVelocity:
            new_vel = self.ui.spinBoxVelocity.value()
            self.macrostage.set_velocity({'1':new_vel, '2':new_vel})
        else:
            new_acc = self.ui.spinBoxAcceleration.value()
            self.macrostage.set_accel_decel({'1':new_acc, '2':new_acc})

        self.populate_ui()

    def accept(self):
        super().accept()

    def reject(self):
        super().reject()

    def keyPressEvent(self, event):
        """ This prevents the enter button from accepting the dialog. Needed since I have a spinBox with editingFinished signal"""
        if self.ui.spinBoxVelocity.hasFocus() | self.ui.spinBoxAcceleration.hasFocus():
            self.ui.buttonBox.buttons()[0].setFocus()


class MicroStage(AbstractStage):
    device_name = 'PI C-867 Piezomotor Controller SN 0111036765'
    num_to_axis = {'2': 'X', '1': 'Y'}
    prefix = 'Macro'
    # axis_to_num = {'X': '1', 'Y': '2'}

    def __init__(self):
        super().__init__()
        self.axis_to_num = {self.num_to_axis[k]: k for k in self.num_to_axis}
        for k in self.num_to_axis:
            self.settings['axis.{}'.format(k)] = self.num_to_axis[k]

    def open(self):
        print('Opening device: {}'.format(self.device_name))
        try:
            self.sdk = GCSDevice('C-867')
            self.sdk.ConnectUSB(self.device_name)
            # Turn on Servos
            self.sdk.SVO({'1': 1, '2': 1})
            if not all(self.sdk.qFRF().values()):
                print('Referencing axis')
                # Reference switch referencing
                self.sdk.FRF()
                self.wait_till_done()
            assert all(self.sdk.qFRF().values()), 'Axes not referenced'
            self.sdk.MOV({'1': 12.5, '2': 12.5})
            self.sdk.JAX(1, 2, '1')
            self.sdk.JAX(1, 1, '2')
            self.get_velocity()
            self.get_position()
        except Exception:
            print('Opening failed')
            print(traceback.format_exc())
        else:
            print('Opening succeeded')
            self.set_joystick_off()

    def close(self):
        print('Closing device: {}'.format(self.device_name))
        try:
            self.set_joystick_off()
            self.sdk.CloseConnection()
        except Exception:
            print('Closing failed')
            print(traceback.format_exc())
        else:
            print('Closing succeeded')
            self.sdk = None

    def get_position(self, axis=None):
        if self.sdk:
            if axis is None:
                pos = self.sdk.qPOS()
                for k in pos:
                    self.settings['position.{}'.format(k)] = pos[k]
                    self.settings['position.{}'.format(self.num_to_axis[k])] = pos[k]
                return pos
            else:
                return self.sdk.qPOS(axis)[axis]

    def set_position(self, pos_dict, read_after=True):
        assert isinstance(pos_dict, dict)
        self.sdk.MOV(pos_dict)
        if read_after:
            self.get_position()

    def set_x_position(self, pos, read_after=True):
        self.set_position({self.axis_to_num['X']: pos}, read_after=read_after)

    def set_y_position(self, pos, read_after=True):
        self.set_position({self.axis_to_num['Y']: pos}, read_after=read_after)

    def wait_till_done(self, pause=0.1, let_settle=False, settle_pause=0.1):
        while self.is_moving():
            sleep(pause)
        if let_settle:
            sleep(settle_pause)

    def wait_till_near(self, axis, start, stop, threshold=0.01, pause=0.01, max_iter=10000, per_iter_fcn=None):
        n_iter = 0
        curr_pos = []
        other_fcn_output = []
        is_near = False
        while (not is_near) & (n_iter < (max_iter - 1)):
            is_near, pos = self.is_near(axis, start, stop, threshold)
            curr_pos.append(pos)
            if per_iter_fcn is not None:
                other_fcn_output.append(per_iter_fcn())
            sleep(pause)
            n_iter += 1
        if per_iter_fcn is None:
            return curr_pos
        else:
            return curr_pos, other_fcn_output

    def is_near(self, axis, start, stop, threshold):
        pos = self.get_position(axis)
        rel_dist = 1 - abs((pos - start) / (stop - start))
        return (rel_dist < threshold, pos)

    def is_moving(self):
        move_status = self.sdk.IsMoving()
        return (move_status['1'] | move_status['2'])

    def set_velocity(self, vel_dict, read_after=True):
        if self.sdk:
            self.sdk.VEL(vel_dict)
            if read_after:
                self.get_velocity()

    def get_velocity(self):
        if self.sdk:
            vel = self.sdk.qVEL()
            for k in vel:
                self.settings['velocity.{}'.format(k)] = vel[k]
                self.settings['velocity.{}'.format(self.num_to_axis[k])] = vel[k]
            return vel

    def get_acceleration(self):
        if self.sdk:
            acc = self.sdk.qACC()
            for k in acc:
                self.settings['acceleration.{}'.format(k)] = acc[k]
                self.settings['acceleration.{}'.format(self.num_to_axis[k])] = acc[k]

            return acc

    def set_acceleration(self, acc_dict, read_after=True):
        if self.sdk:
            self.sdk.ACC(acc_dict)
            if read_after:
                self.get_acceleration()

    def set_deceleration(self, dec_dict, read_after=True):
        if self.sdk:
            self.sdk.DEC(dec_dict)
            if read_after:
                self.get_deceleration()

    def get_deceleration(self):
        if self.sdk:
            dec = self.sdk.qDEC()
            for k in dec:
                self.settings['deceleration.{}'.format(k)] = dec[k]
                self.settings['deceleration.{}'.format(self.num_to_axis[k])] = dec[k]

            return dec

    def set_accel_decel(self, accdec_dict, read_after=True):
        if self.sdk:
            self.set_acceleration(accdec_dict, read_after=read_after)
            self.set_deceleration(accdec_dict, read_after=read_after)

    def get_joystick_status(self):
        if self.sdk:
            return self.sdk.qJON(1)[1]

    def set_joystick_on(self):
        if self.sdk:
            self.sdk.JON(1, 1)

    def set_joystick_off(self):
        if self.sdk:
            self.sdk.JON(1, 0)


if __name__ == '__main__':
    
    try_ui = True

    try:
        devices = {}
        devices['MicroStage'] = MicroStage()
        devices['MicroStage'].open()
        print(devices['MicroStage'].sdk.gcscommands.qHPA())
        print('Max acceleration: {}'.format(devices['MicroStage'].sdk.gcscommands.qSPA('1', '0x4A')['1'][0x4A]))
        print('Current acceleration: {}'.format(devices['MicroStage'].get_acceleration()))
        print('Max deceleration: {}'.format(devices['MicroStage'].sdk.gcscommands.qSPA('1', '0x4B')['1'][0x4B]))
        print('Current deceleration: {}'.format(devices['MicroStage'].get_deceleration()))

        print('Current velocity: {}'.format(devices['MicroStage'].get_velocity()))
        print('Max velocity: {}'.format(devices['MicroStage'].sdk.gcscommands.qSPA('1', '0xA')['1'][0xA]))
    except Exception:
        print(traceback.format_exc())
    else:
        if try_ui:
            import sys
            from bcars_microscope import dark_style_sheet as stylesheet
            app = QApplication(sys.argv)
            app.setStyle("Fusion")
            app.setStyleSheet(stylesheet)

            window = DialogMacroStage(macrostage=devices['MicroStage'])
            ret = window.exec_()
            print(ret)
    finally:
        devices['MicroStage'].close()

    # Run a demo raster scan
    # from bcars_microscope.andor_ccd import AndorNewton970    
    
    # devices = {}
    # start = 12.5
    # stop = 13.5
    # diff = stop-start
    # vel = 1. 
    

    # try:
    #     devices['CCD'] = AndorNewton970(settings_kwargs={'exposure_time': 0.0035, 'readout_mode': 'FULL_VERTICAL_BINNING', 'trigger_mode': 'INTERNAL'})

    #     devices['CCD'].init_all()
    #     # devices['CCD'].set_internal_trigger()
    #     dwell = devices['CCD'].net_acquisition_time
    #     # print('Estimated total time per acquisition (2): {}'.format(dwell))
    #     devices['CCD'].sdk.SetExposureTime(0.0035)
    #     print('Exposure time: {}'.format(devices['CCD'].sdk.GetAcquisitionTimings()[1]))
    #     devices['MicroStage'] = MicroStage()
    #     devices['MicroStage'].open()
    #     print('Delay: {}'.format(devices['MicroStage'].sdk.DEL(0)))
    # except Exception:
    #     print(traceback.format_exc())
    # else:
    #     # Set velocity
    #     devices['MicroStage'].set_velocity({'1':vel, '2':vel})
    #     print('Velocity: {}'.format(devices['MicroStage'].get_velocity()))
        
    #     # Set acceleration
    #     print('Acceleration: {}'.format(devices['MicroStage'].get_acceleration()))
        
    #     N_iter = 10
    #     n_img_list = []

    #     for _ in range(N_iter):
    #         # Set initial position
    #         devices['MicroStage'].set_position({'1':start, '2':start})
    #         while devices['MicroStage'].is_moving():
    #             sleep(0.01)
    #         curr_pos = [devices['MicroStage'].get_position('2')]
    #         n_imgs_w_pos = [0]
    #         # Start CCD
    #         devices['CCD'].start_acquisition()

    #         # MOVE 
    #         devices['MicroStage'].set_position({'2':stop})
    #         temp_pos, temp_n_imgs = devices['MicroStage'].wait_till_near('2', start, stop, threshold=0.01, pause=0.01, 
    #                                                                      per_iter_fcn=lambda: devices['CCD'].get_num_new_images()[1])
    #         n_imgs_w_pos.extend(temp_n_imgs)
    #         curr_pos.extend(temp_pos)
                    
    #         # Stop acquisition
    #         devices['CCD'].stop_acquisition()
    #         # print(curr_pos)

    #         # Collect images
    #         _, n_images, _, _ = devices['CCD'].get_num_new_images()
    #         n_img_list.append(n_images)
    #         # print('New Images: {}'.format(n_images))
    #         (_, _, _, _) = devices['CCD'].get_all_images16()
    #     print('N images: {} +/- {:.1f}'.format(int(np.mean(n_img_list)), np.std(n_img_list)))
    #     print(n_imgs_w_pos)
    # finally:
    #     devices['CCD'].free_memory()
    #     devices['CCD'].shutdown()
    #     devices['MicroStage'].close()
