import serial
import sys
import time
import traceback

from devices import AbstractDevice
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer

from ui.ui_bcars2_laser_setup import Ui_Dialog as Ui_Laser
from bcars_microscope import dark_style_sheet as stylesheet

QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)


class TopticaPro(AbstractDevice):
    device_name = 'Toptica NIR Pro and UCP'
    prefix = 'Laser'

    def __init__(self, com_port, baudrate=115200, **kwargs):
        """Toptica FemtoPro NIR + UCP dual laser system

        Parameters
        ----------
        com_port : str
            COM port (e.g., 'COM7')
        baudrate : int, optional
            COM port baud rate, by default 115200
        """
        super().__init__(com_port=com_port, baudrate=115200, **kwargs)

    def open(self):
        """Open device (via COM port).
        """
        print('Opening device: {}'.format(self.device_name))
        try:
            self.serial = serial.Serial(self.settings['com_port'], self.settings['baudrate'], timeout=10)
        except Exception:
            print('Opening failed')
            print(traceback.format_exc())
        else:
            print('Opening succeeded')

    def close(self):
        """Close device COM connection)
        """
        print('Closing device: {}'.format(self.device_name))
        try:
            self.serial.close()
        except Exception:
            print('Closing failed')
            print(traceback.format_exc())
        else:
            print('Closing succeeded')
            self.serial = None

    def _read_write(self, write_command, max_iter=10):
        """Write a command and read response

        Parameters
        ----------
        write_command : str
            Command to write
        max_iter : int, optional
            Maximum number of interations to try reading lines of returned info, by default 10

        Returns
        -------
        list
            List of responses from laser system. Each entry is a string representing 1 line of response.
        """
        self.serial.write('{}\r\n'.format(write_command).encode())
        output = []
        for i in range(max_iter):
            temp = self.serial.readline().decode().rstrip('\r\n').strip('>>>').strip()
            if temp == '':
                break
            output.append(temp)
        return output

    def _write(self, write_command):
        """Write a command

        Parameters
        ----------
        write_command : str
            Command
        """
        self.serial.write('{}\r\n'.format(write_command).encode())

    def check_all(self):
        """Check all laser settings as they currently are on the system.
        """
        self.probe_is_on()
        self.probe_amp_level()
        self.probe_prism_pos()
        self.sc_is_on()
        self.sc_amp_level()
        self.sc_pre_prism_pos()
        self.sc_post_prism_pos()

    def probe_is_on(self):
        """Get the ON/OFF status of probe laser

        Returns
        -------
        bool
            Is the laser ON?
        """

        k = 'ffpro.arm0.onoff'
        output = self._read_write(k)[1] == '1'
        self.settings[k] = output
        return output

    def sc_is_on(self):
        """Get the ON/OFF status of supercontinuum (SC) laser

        Returns
        -------
        bool
            Is the laser ON?
        """

        k = 'ffpro.arm1.onoff'
        output = self._read_write(k)[1] == '1'
        self.settings[k] = output
        return output

    def probe_amp_level(self):
        """Get the probe amplifier level setting [0.0,1.0]

        Returns
        -------
        float
            Amplifier relative level
        """

        k = 'ffpro.arm0.level'
        output = float(self._read_write(k)[1])
        self.settings[k] = output
        return output

    def sc_amp_level(self):
        """Get the SC amplifier level setting [0.0,1.0]

        Returns
        -------
        float
            Amplifier relative level
        """

        k = 'ffpro.arm1.level'
        output = float(self._read_write(k)[1])
        self.settings[k] = output
        return output

    def probe_prism_pos(self):
        """Get the probe Si prism position (mm)

        Returns
        -------
        float
            Prism position
        """

        k = 'ffpro.arm0.axSi.pos'
        output = float(self._read_write(k)[1])
        self.settings[k] = output
        return output

    def probe_set_prism_pos(self, value, read_after=True):
        self._read_write('ffpro.arm0.axSi.target={}'.format(value))
        if read_after:
            self.probe_prism_pos()

    def sc_set_pre_prism_pos(self, value, read_after=True):
        self._read_write('ffpro.arm1.axSi.target={}'.format(value))
        if read_after:
            self.sc_pre_prism_pos()

    def sc_set_post_prism_pos(self, value, read_after=True):
        self._read_write('ffpro.arm1.axSF10.target={}'.format(value))
        if read_after:
            self.sc_post_prism_pos()

    def probe_auto_opti_is_on(self):
        """Is probe laser autooptimize ON?

        Returns
        -------
        bool
            Auto-optimize is ON
        """

        k = 'ffpro.arm0.optimizer.auto'
        output = self._read_write(k)[1] == '1'
        self.settings[k] = output
        return output

    def probe_set_auto_opti(self, turn_on, read_after=True):
        if turn_on:
            k = 'ffpro.arm0.optimizer.auto=1'
        else:
            k = 'ffpro.arm0.optimizer.auto=0'
        self._read_write(k)
        if read_after:
            self.probe_auto_opti_is_on()

    def sc_pre_prism_pos(self):
        """Get the SC Si prism position (mm)

        Returns
        -------
        float
            Prism position
        """

        k = 'ffpro.arm1.axSi.pos'
        output = float(self._read_write(k)[1])
        self.settings[k] = output
        return output

    def sc_post_prism_pos(self):
        """Get the probe SF10 prism position (mm)

        Returns
        -------
        float
            Prism position
        """

        k = 'ffpro.arm1.axSF10.pos'
        output = float(self._read_write(k)[1])
        self.settings[k] = output
        return output

    def probe_opti_now(self, read_after=True):
        self._read_write('ffpro.arm0.optimizer.optimize()')
        if read_after:
            self.probe_prism_pos()


class DialogLaserConfig(QDialog):
    def __init__(self, laser):
        # Boilerplate stuff
        super().__init__()
        self.ui = Ui_Laser()
        self.ui.setupUi(self)
        self.laser = laser

        if self.laser is not None:
            self.update_settings()
            self.ui.spinBoxSCSetPost.setValue(self.ui.spinBoxSCReadPost.value())
            self.ui.spinBoxProbeSetPrism.setValue(self.ui.spinBoxProbeReadPrism.value())
            self.ui.spinBoxProbeSetAmp.setValue(self.ui.spinBoxProbeReadAmp.value())
            self.ui.spinBoxSCSetPre.setValue(self.ui.spinBoxSCReadPre.value())

        self.timer = QTimer()
        self.timer.setInterval(2000)
        self.timer.timeout.connect(self.update_settings)
        self.timer.start()

        # Signal 7 Slots
        if self.laser is not None:
            self.ui.pushButtonProbeOptiNow.pressed.connect(self.laser.probe_opti_now)
            self.ui.spinBoxProbeSetPrism.editingFinished.connect(self.change_prism)
            self.ui.spinBoxSCSetPre.editingFinished.connect(self.change_prism)
            self.ui.spinBoxSCSetPost.editingFinished.connect(self.change_prism)
            self.ui.checkBoxProbeAutoOpti.stateChanged.connect(self.change_auto_opti)

    def change_auto_opti(self):
        self.laser.probe_set_auto_opti(self.ui.checkBoxProbeAutoOpti.isChecked())

    def change_prism(self):
        sender = self.sender()
        
        if sender == self.ui.spinBoxProbeSetPrism:  # Probe prism
            self.laser.probe_set_prism_pos(self.ui.spinBoxProbeSetPrism.value())
        elif sender == self.ui.spinBoxSCSetPre:
            self.laser.sc_set_pre_prism_pos(self.ui.spinBoxSCSetPre.value())
        elif sender == self.ui.spinBoxSCSetPost:
            self.laser.sc_set_post_prism_pos(self.ui.spinBoxSCSetPost.value())

    def update_settings(self):
        time.sleep(0.1)
        try:
            # Probe Laser
            probe_on = self.laser.probe_is_on()
            if probe_on:
                self.ui.radioButtonProbeOn.setChecked(True)
            else:
                self.ui.radioButtonProbeOff.setChecked(True)

            auto_opti = self.laser.probe_auto_opti_is_on()
            self.ui.checkBoxProbeAutoOpti.setChecked(auto_opti)

            self.ui.spinBoxProbeReadAmp.setValue(self.laser.probe_amp_level())

            self.ui.spinBoxProbeReadPrism.setValue(self.laser.probe_prism_pos())
            
            # Superconitnuum
            sc_on = self.laser.sc_is_on()
            if sc_on:
                self.ui.radioButtonSCOn.setChecked(True)
            else:
                self.ui.radioButtonSCOff.setChecked(True)
            
            self.ui.spinBoxSCReadAmp.setValue(self.laser.sc_amp_level())
            self.ui.spinBoxSCSetAmp.setValue(self.laser.sc_amp_level())

            self.ui.spinBoxSCReadPre.setValue(self.laser.sc_pre_prism_pos())

            self.ui.spinBoxSCReadPost.setValue(self.laser.sc_post_prism_pos())

            # self.update_settings()
        except Exception:
            print(traceback.format_exc())

    def accept(self):
        super().accept()

    def reject(self):
        super().reject()

    def keyPressEvent(self, event):
        """ This prevents the enter button from accepting the dialog. Needed since I have a spinBox with editingFinished signal"""
        if self.ui.spinBoxProbeSetAmp.hasFocus():
            self.ui.buttonBox.buttons()[0].setFocus()
        elif self.ui.spinBoxProbeSetPrism.hasFocus():
            self.ui.buttonBox.buttons()[0].setFocus()
        elif self.ui.spinBoxSCSetAmp.hasFocus():
            self.ui.buttonBox.buttons()[0].setFocus()
        elif self.ui.spinBoxSCSetPre.hasFocus():
            self.ui.buttonBox.buttons()[0].setFocus()
        elif self.ui.spinBoxSCSetPost.hasFocus():
            self.ui.buttonBox.buttons()[0].setFocus()

    def hideEvent(self, ev):
        """ This happens when the window is hidden"""
        self.timer.stop()
        
        return QWidget.hideEvent(self, ev)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setStyleSheet(stylesheet)

    laser = TopticaPro(com_port='COM7')

    try:
        laser.open()
        window = DialogLaserConfig(laser=laser)
        ret = window.exec_()
    except Exception:
        print(traceback.format_exc())
    finally:
        laser.close()
