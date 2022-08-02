
import serial
import traceback
from time import sleep
from bcars_microscope.devices import AbstractDevice
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtCore
import numpy as np

from bcars_microscope.ui.ui_bcars2_spectrometer import Ui_Dialog as Ui_Spectrograph
QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)


class Acton2300i(AbstractDevice):
    device_name = 'Acton 2300i Spectrograph'
    grating_dict = {1: '300 g/mm BLZ = 750 nm',
                    2: '150 g/mm BLZ = 800 nm',
                    3: '300 g/mm BLZ = 500 nm'}

    grating_calib_dict = {1: {'n_pix': 1600, 'ctr_wl0': 699.995, 'a_vec': [0.165513, 569.1], 'probe': 771.461},
                          2: {'n_pix': 1600, 'ctr_wl0': 699.995, 'a_vec': [0.3396953650, 411.1], 'probe': 771.461},
                          3: {'n_pix': 1600, 'ctr_wl0': 699.995, 'a_vec': [0.1669139120, 570.4], 'probe': 771.461}}

    prefix = 'Spectrometer'

    def __init__(self, com_port, baudrate=921600, calib_dict=None, **kwargs):
        super().__init__(com_port=com_port, baudrate=baudrate, **kwargs)
        if calib_dict:
            self.calib_dict = calib_dict
        self.calib_dict = None

    def update_calibration(self):
        if isinstance(self.calib_dict, dict):
            for k in self.calib_dict:
                self.settings['calib.{}'.format(k)] = self.calib_dict[k]

        self.spectral_vecs_dict = {}

        if not isinstance(self.calib_dict, dict):
            return None

        if 'n_pix' not in self.calib_dict:
            print('Number of pixels (n_pix) not in calibration dictionary')
            return None
        self.spectral_vecs_dict['pix_vec'] = np.arange(self.calib_dict['n_pix'])
        self.settings['calib.pix_vec'] = 1. * self.spectral_vecs_dict['pix_vec']

        if 'ctr_wl' not in self.calib_dict:
            print('Center wavelength (ctr_wl) not in calibration dictionary')
            return None

        if 'ctr_wl0' not in self.calib_dict:
            print('Calibrated center wavelength (ctr_wl0) not in calibration dictionary')
            return None

        if 'a_vec' not in self.calib_dict:
            print('Polynomial vector (a_vec) not in calibration dictionary')
            return None
        diff_wl = self.calib_dict['ctr_wl'] - self.calib_dict['ctr_wl0']
        self.spectral_vecs_dict['wl_vec'] = np.polyval(self.calib_dict['a_vec'], self.spectral_vecs_dict['pix_vec']) + diff_wl
        self.settings['calib.wl_vec'] = 1. * self.spectral_vecs_dict['wl_vec']

        if 'probe' not in self.calib_dict:
            print('Probe wavelength (probe) not in calibration dictionary')
            return None
        self.spectral_vecs_dict['wn_vec'] = 0.01 / (self.spectral_vecs_dict['wl_vec'] * 1e-9) - 0.01 / (self.calib_dict['probe'] * 1e-9)
        self.settings['calib.wn_vec'] = 1. * self.spectral_vecs_dict['wn_vec']

        if 'units' not in self.calib_dict:
            self.calib_dict['units'] = 'nm'

    def open(self):
        print('Opening device: {}'.format(self.device_name))
        try:
            self.serial = serial.Serial(self.settings['com_port'], self.settings['baudrate'], timeout=1)

        except Exception:
            print('Opening failed: {}'.format(self.device_name))
            print(traceback.format_exc())
        else:
            print('Opening succeeded: {}'.format(self.device_name))

            ng = self.get_grating()
            if self.calib_dict is None:
                self.calib_dict = self.grating_calib_dict[ng]
            ctr_wl = self.get_wavelength()
            self.calib_dict['ctr_wl'] = ctr_wl
            self.update_calibration()

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
            self.settings['ctr_wl'] = wl
            self.calib_dict['ctr_wl'] = wl
            return wl

    def set_wavelength(self, wavelength, read_after=True):
        new_wl = '{:.3f}'.format(wavelength)
        self._write('{} GOTO'.format(new_wl))
        _ = self._read_wait()  # Get the 'ok'
        if read_after:
            pass  # So vital, decided to make read_after unnecessary
        _ = self.get_wavelength()
        self.update_calibration()

    def get_grating(self):
        line = int(self._read_write('?GRATING'))
        self.settings['Grating Num'] = line
        self.settings['Grating'] = self.grating_dict[line]
        return line

    def set_grating(self, grating_num, read_after=True):
        self._write('{} GRATING'.format(grating_num))
        _ = self._read_wait()
        ng = self.get_grating()
        self.calib_dict = self.grating_calib_dict[ng]
        self.get_wavelength()
        self.update_calibration()
        if read_after:  # So necessary not limiting anything to read_after
            pass


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
        self.ui.spinBoxCalibIntercept.editingFinished.connect(self.change_settings)
        self.ui.spinBoxCalibProbe.editingFinished.connect(self.change_settings)
        self.ui.spinBoxCalibSlope.editingFinished.connect(self.change_settings)
        self.ui.spinBoxCalibWL.editingFinished.connect(self.change_settings)

    def populate_ui(self):
        """ Populate the UI and set current values"""
        # Wavelength
        # self.ui.spinBoxCurrentWL.setValue(self.spec.get_wavelength())

        # Grating
        for k in self.spec.grating_dict:
            self.ui.comboBoxGratings.addItem(self.spec.grating_dict[k])

        self.get_settings_from_spec()

    def get_settings_from_spec(self):
        self.ui.spinBoxWL.setValue(self.spec.get_wavelength())
        self.ui.comboBoxGratings.setCurrentIndex(self.spec.get_grating() - 1)
        self.ui.spinBoxCalibWL.setValue(self.spec.calib_dict['ctr_wl0'])
        self.ui.spinBoxCalibIntercept.setValue(self.spec.calib_dict['a_vec'][-1])
        self.ui.spinBoxCalibSlope.setValue(self.spec.calib_dict['a_vec'][0])
        self.ui.spinBoxCalibProbe.setValue(self.spec.calib_dict['probe'])

    def change_settings(self):
        sender = self.sender()

        if sender == self.ui.comboBoxGratings:
            ng = self.ui.comboBoxGratings.currentIndex()
            self.spec.set_grating(ng + 1)  # +1 b/c spectro NOT 0-index
            self.get_settings_from_spec()
        elif sender == self.ui.spinBoxWL:
            new_wl = self.ui.spinBoxWL.value()
            self.spec.set_wavelength(new_wl)
            self.get_settings_from_spec()
        elif (sender == self.ui.spinBoxCalibIntercept) | (sender == self.ui.spinBoxCalibSlope):
            intercept = self.ui.spinBoxCalibIntercept.value()
            slope = self.ui.spinBoxCalibSlope.value()
            self.spec.calib_dict['a_vec'] = [slope, intercept]
            self.spec.update_calibration()
            self.get_settings_from_spec()
        elif sender == self.ui.spinBoxCalibProbe:
            probe = self.ui.spinBoxCalibProbe.value()
            self.spec.calib_dict['probe'] = probe
            self.spec.update_calibration()
            self.get_settings_from_spec()
        elif sender == self.ui.spinBoxCalibWL:
            new_c_wl = self.ui.spinBoxCalibWL.value()
            self.spec.calib_dict['ctr_wl0'] = 1 * new_c_wl
            self.spec.update_calibration()
            self.get_settings_from_spec()

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

        except Exception:
            print(traceback.format_exc())
        finally:
            print(spec.meta)
            spec.close()
