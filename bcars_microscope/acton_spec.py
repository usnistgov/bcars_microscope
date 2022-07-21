
import serial
import traceback
from time import sleep
from devices import AbstractDevice
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtCore

from ui.ui_bcars2_spectrometer import Ui_Dialog as Ui_Spectrograph
QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)


class Acton2300i(AbstractDevice):
    device_name = 'Acton 2300i Spectrograph'
    grating_dict = {1: '300 g/mm BLZ = 750 nm',
                    2: '150 g/mm BLZ = 800 nm',
                    3: '300 g/mm BLZ = 500 nm'}
    def __init__(self, com_port, baudrate=921600, **kwargs):
        super().__init__(com_port=com_port, baudrate=baudrate, **kwargs)

    def open(self):
        print('Opening device: {}'.format(self.device_name))
        try:
            self.serial = serial.Serial(self.settings['com_port'], self.settings['baudrate'], timeout=1)

        except Exception:
            print('Opening failed: {}'.format(self.device_name))
            print(traceback.format_exc())
        else:
            print('Opening succeeded: {}'.format(self.device_name))

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
        self.serial.write('{}\r'.format(write_command).encode())
        output = self.serial.readline().decode().rsplit('ok')[0].strip()

        return output

    def _read(self):
        output = self.serial.readline().decode()
        return output

    def _read_wait(self, wait_for='ok', max_iter=30, wait_time_s=0.25):
        for num in range(max_iter):
            output = self.serial.readline().decode()
            if wait_for in output:
                break
            sleep(wait_time_s)
        return output

    def _write(self, write_command):
        self.serial.write('{}\r'.format(write_command).encode())

    def get_wavelength(self, axis=1):
        if self.serial:
            wl = float(self._read_write('?nm').rsplit('nm')[0].strip())

            return wl

    def set_wavelength(self, wavelength):
        new_wl = '{:.3f}'.format(wavelength)
        self._write('{} GOTO'.format(wavelength))
        out = self._read_wait()
        return out

    def get_grating(self):
        line = int(self._read_write('?GRATING'))
        return line


    def set_grating(self, grating_num):
        self._write('{} GRATING'.format(grating_num))
        out = self._read_wait()
        # print('Set Grating: {}'.format(out))


class DialogSpectrographConfig(QDialog):
    def __init__(self, spec):
        # Boilerplate stuff
        super().__init__()
        self.ui = Ui_Spectrograph()
        self.ui.setupUi(self)
        self.spec = spec

        if self.spec is not None:
            self.populate_ui()

        print('Buttons: {}'.format(self.ui.buttonBox.buttons()))
        for i in self.ui.buttonBox.buttons():
            print(i.text())
        self.ui.buttonBox.buttons()[0].setAutoDefault(False)
        self.ui.buttonBox.buttons()[0].setDefault(False)
        self.ui.buttonBox.buttons()[1].setAutoDefault(False)
        self.ui.buttonBox.buttons()[1].setDefault(False)

        # print('Buttons: {}'.format())
        # print('Buttons: {}'.format(self.ui.buttonBox.buttons()[0].setDefault(False)))

        self.ui.comboBoxGratings.currentIndexChanged.connect(self.change_settings)
        self.ui.spinBoxWL.editingFinished.connect(self.change_settings)

    def populate_ui(self):
        """ Populate the UI and set current values"""
        # Wavelength
        # self.ui.spinBoxCurrentWL.setValue(self.spec.get_wavelength())

        # Grating
        for k in self.spec.grating_dict:
            self.ui.comboBoxGratings.addItem(self.spec.grating_dict[k])

        # self.ui.comboBoxGratings.setCurrentIndex(self.spec.get_grating()-1)
        self.update_settings()

    def update_settings(self):
        self.ui.spinBoxWL.setValue(self.spec.get_wavelength())
        self.ui.comboBoxGratings.setCurrentIndex(self.spec.get_grating()-1)

    def change_settings(self):
        new_wl = self.ui.spinBoxWL.value()
        new_grating = self.ui.comboBoxGratings.currentIndex() + 1  # +1 b/c spectro NOT 0-index

        self.spec.set_grating(new_grating)
        self.spec.set_wavelength(new_wl)
        self.update_settings()


    def accept(self):
        # if self.ccd is not None:
        #     self.ccd.settings.update(self.dict_from_ui)
        #     self.ccd.init_camera()

        super().accept()

    def reject(self):
        super().reject()

    def keyPressEvent(self, event):
        """ This prevents the enter button from accepting the dialog. Needed since I have a spinBox with editingFinished signal"""
        if self.ui.spinBoxWL.hasFocus():
            self.ui.buttonBox.buttons()[0].setFocus()

if __name__ == '__main__':

    import sys
    from bcars_microscope import dark_style_sheet as stylesheet

    just_ui = False

    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setStyleSheet(stylesheet)

    if just_ui:
        window = DialogSpectrographConfig(spec=None)
        ret = window.exec_()
        print(ret)
        # out = app.exec_()
    else:
        spec = Acton2300i('COM4')

        try:
            ret = spec.open()
            window = DialogSpectrographConfig(spec=spec)
            ret = window.exec_()

        except:
            print(traceback.format_exc())
        finally:
            spec.close()

