import serial
import time
import traceback
from bcars_microscope.devices import AbstractStage
from bcars_microscope.ui.ui_bcars2_esp import Ui_Dialog as Ui_DelayStage

from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtCore

QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)


class DialogDelayStage(QDialog):
    def __init__(self, delaystage):
        # Boilerplate stuff
        super().__init__()
        self.ui = Ui_DelayStage()
        self.ui.setupUi(self)
        self.delaystage = delaystage

        if self.delaystage is not None:
            self.populate_ui()

        # Signals and Slots
        self.ui.spinBoxVelocity.editingFinished.connect(self.change_settings)
        self.ui.spinBoxAcceleration.editingFinished.connect(self.change_settings)

    def populate_ui(self):
        """ Populate the UI and set current values"""
        vel = self.delaystage.get_velocity()
        self.ui.spinBoxVelocity.setValue(vel)
        acc = self.delaystage.get_acceleration()
        self.ui.spinBoxAcceleration.setValue(acc)

    def change_settings(self):
        sender = self.sender()

        if sender == self.ui.spinBoxVelocity:
            new_vel = self.ui.spinBoxVelocity.value()
            self.delaystage.set_velocity(new_vel)
        else:
            new_acc = self.ui.spinBoxAcceleration.value()
            self.delaystage.set_acceleration(new_acc)

        self.populate_ui()

    def accept(self):
        super().accept()

    def reject(self):
        super().reject()

    def keyPressEvent(self, event):
        """ This prevents the enter button from accepting the dialog. Needed since I have a spinBox with editingFinished signal"""
        if self.ui.spinBoxVelocity.hasFocus() | self.ui.spinBoxAcceleration.hasFocus():
            self.ui.buttonBox.buttons()[0].setFocus()


class ESP301(AbstractStage):

    device_name = 'ESP 301 Stage'
    prefix = 'Delay'

    def __init__(self, com_port, baudrate=921600, **kwargs):
        super().__init__(com_port=com_port, baudrate=baudrate, **kwargs)

    def get_position(self, axis=1):
        if self.serial:
            pos = float(self._read_write('{}TP'.format(axis)))
            self.settings['position'] = pos
            return pos

    def set_position(self, pos, axis=1, read_after=True):
        self._write('{}PA {}'.format(axis, pos))
        if read_after:
            self.get_position()

    def set_home(self, axis=1):
        self._write('{}DH'.format(axis))

    def wait_till_done(self, n_iter=10, pause=0.1, let_settle=True, settle_pause=0.25, axis=1):
        for _ in range(n_iter):
            time.sleep(pause)
            line = self._read_write('{}MD?'.format(axis))
            # print('Is motion done? (0: NOT done; 1: done): {}'.format(line))
            if int(line) == 1:
                break
        if let_settle:
            for _ in range(n_iter):
                pos1 = self.get_position()
                time.sleep(settle_pause)
                pos2 = self.get_position()
                if round(pos1, 3) == round(pos2, 3):
                    break
        return None

    def open(self):
        print('Opening device: {}'.format(self.device_name))
        try:
            self.serial = serial.Serial(self.settings['com_port'], self.settings['baudrate'], timeout=1)
            self.motor_on()
            self.get_position()
            self.get_velocity()
        except Exception:
            print('Opening failed')
            print(traceback.format_exc())
        else:
            print('Opening succeeded')

    def motor_on(self):
        self._write('1MO_Set')
        self.settings['motor'] = 'on'

    def motor_off(self):
        self._write('1MF_Set')
        self.settings['motor'] = 'off'

    def close(self):
        print('Closing device: {}'.format(self.device_name))
        try:
            self.serial.close()
        except Exception:
            print('Closing failed')
            print(traceback.format_exc())
        else:
            print('Closing succeeded')
            self.serial = None

    def _read_write(self, write_command):
        self.serial.write('{}\r\n'.format(write_command).encode())
        output = self.serial.readline().decode().rstrip('\r\n')
        return output

    def _write(self, write_command):
        self.serial.write('{}\r\n'.format(write_command).encode())

    def set_velocity(self, vel, axis=1, read_after=True):
        self._write('{}VA {}'.format(axis, vel))
        if read_after:
            self.get_velocity()

    def get_velocity(self, axis=1):
        vel = float(self._read_write('{}VA?'.format(axis)))
        self.settings['velocity'] = vel
        return vel

    def set_acceleration(self, acc, axis=1, read_after=True):
        self._write('{}AC {}'.format(axis, acc))
        if read_after:
            self.get_acceleration()

    def get_acceleration(self, axis=1):
        acc = float(self._read_write('{}AC?'.format(axis)))
        self.settings['acceleration'] = acc
        return acc

    def get_max_velocity(self, axis=1):
        max_vel = float(self._read_write('1VU?'))
        self.settings['max_velocity'] = max_vel
        return max_vel

    def get_max_acceleration(self, axis=1):
        max_acc = float(self._read_write('1AU?'))
        self.settings['max_acceleration'] = max_acc
        return max_acc


if __name__ == '__main__':

    try_ui = True

    esp = ESP301(com_port='COM9')
    print('Open?: {}'.format(esp.is_open))
    esp.open()
    try:
        print(esp._write('1MO'))
        print(esp._read_write('1MO?'))
    except Exception:
        print('Failed: {}'.format(traceback.format_exc()))
    # print('Open?: {}'.format(esp.is_open))

    curr_pos = esp.get_position()

    print('Current position: {:.3f}'.format(curr_pos))

    try:
        print('Velocity: {}'.format(esp.get_velocity()))
        esp.set_velocity(1.0)
        print('Velocity: {}'.format(esp.get_velocity()))

        print('Max Velocity: {}'.format(esp.get_max_velocity()))
        print('Max Acceleration: {}'.format(esp.get_max_acceleration()))

        print('Acceleration: {}'.format(esp.get_acceleration()))
        esp.set_acceleration(1.0)
        print('Acceleration: {}'.format(esp.get_acceleration()))

    except Exception:
        print(traceback.format_exc())

    else:
        if try_ui:
            import sys
            from bcars_microscope import dark_style_sheet as stylesheet
            app = QApplication(sys.argv)
            app.setStyle("Fusion")
            app.setStyleSheet(stylesheet)

            window = DialogDelayStage(delaystage=esp)
            ret = window.exec_()
            print(ret)
    finally:
        esp.close()
        print('Open?: {}'.format(esp.is_open))
        print(esp.meta)

