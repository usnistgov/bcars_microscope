import traceback

from pipython import GCSDevice
from bcars_microscope.devices import AbstractStage
# from bcars_microscope.ui.ui_bcars2_pi_nano import Ui_Dialog as Ui_NanoStage

# from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtCore

# QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)


class NanoStage(AbstractStage):

    device_name = 'PI E-517 Display and Interface SN 0114071272'
    prefix = 'Nano'

    def __init__(self):
        super().__init__(self)

    def open(self):
        print('Opening device: {}'.format(self.device_name))
        try:
            self.sdk = GCSDevice('E-545')
            self.sdk.ConnectUSB(self.device_name)

            # Turn control mode to ONLINE (axis number : 1=ONLINE)
            self.sdk.ONL({1: 1, 2: 1, 3: 1})

            # Turn on all Servos (axis ID : 1=ON)
            self.sdk.SVO({'X': 1, 'Y': 1, 'Z': 1})
            self.get_position()
            self.get_velocity()
            self.get_wavegen_rate()

        except Exception:
            print('Opening failed')
            print(traceback.format_exc())
        else:
            print('Opening succeeded')

    def close(self):
        print('Closing device: {}'.format(self.device_name))
        try:
            self.sdk.CloseConnection()
        except Exception:
            print('Closing failed')
            print(traceback.format_exc())
        else:
            print('Closing succeeded')
            self.sdk = None

    def get_position(self):
        if self.sdk:
            pos = self.sdk.qPOS()
            for k in pos:
                self.settings['position.{}'.format(k)] = pos[k]
            return pos

    def set_position(self, pos_dict, read_after=True):
        assert isinstance(pos_dict, dict)
        self.sdk.MOV(pos_dict)
        if read_after:
            self.get_position()

    def wait_till_done(self, n_iter, pause, let_settle, settle_pause):
        raise NotImplementedError('Haven\'t found a good way to do this yet')

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
            return vel

    def get_wavegen_rate(self, num_wavegen=None):
        if self.sdk:
            if num_wavegen is None:
                wg = self.sdk.qWTR()
                for k in wg:
                    self.settings['wavegen_rate.{}'.format(k)] = wg[k][0]
                return wg
            else:
                wg = self.sdk.qWTR(num_wavegen)
                self.settings['wavegen_rate.{}'.format(num_wavegen)] = wg[num_wavegen][0]
                return wg

    def set_wavegen_rate(self, num_wavegen, rate, read_after=True):
        if self.sdk:
            self.sdk.WTR(num_wavegen, rate, 0)
            if read_after:
                self.get_wavegen_rate()

    def set_linescan(self, table_num, start, num_points, stop):
        self.sdk.WAV_LIN(table=table_num, firstpoint=0, numpoints=num_points,
                         append='X', speedupdown=0, amplitude=stop - start,
                         offset=start, seglength=num_points)
        self.settings['wav_lin'] = 'WAV {} X LIN {} {} {} {} 0 0'.format(table_num, num_points, stop-start, start, num_points)


if __name__ == '__main__':
    
    try_ui = False

    try:
        devices = {}
        devices['NanoStage'] = NanoStage()
        devices['NanoStage'].open()
        devices['NanoStage'].set_velocity({'X':1.})
        print('Current velocity: {}'.format(devices['NanoStage'].get_velocity()))
        # print('Max velocity: {}'.format(devices['NanoStage'].sdk.gcscommands.qSPA('1', '0xA')['1'][0xA]))
    except Exception:
        print(traceback.format_exc())
    else:
        pass
        # if try_ui:
        #     import sys
        #     from bcars_microscope import dark_style_sheet as stylesheet
        #     app = QApplication(sys.argv)
        #     app.setStyle("Fusion")
        #     app.setStyleSheet(stylesheet)

        #     window = DialogNanoStage(macrostage=devices['NanoStage'])
        #     ret = window.exec_()
        #     print(ret)
    finally:
        devices['NanoStage'].close()
