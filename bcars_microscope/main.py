"""
Main controller for bcars microscope

TODO: Configure Stage
TODO: Configure Delay
TODO: Configure Laser

"""


import sys
import traceback

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore

from ui.ui_bcars2_main import Ui_MainWindow
from spectroscopy import MainWindow as WinSpectroscopy
from raster import MainWindow as WinRaster

from andor_ccd import AndorNewton970, DialogAndorConfig
from esp301 import ESP301
from pi_nano_stage import NanoStage
from pi_micro_stage import MicroStage
from acton_spec import Acton2300i, DialogSpectrographConfig

from bcars_microscope import dark_style_sheet
stylesheet = dark_style_sheet
QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)


class MainWindow(QMainWindow):
    def __init__(self):
        # Boilerplate stuff
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.devices = {}
        self.devices['CCD'] = None
        self.devices['running'] = False

        # Signals and Slots
        self.ui.pushButtonInitCCD.pressed.connect(self.init_ccd)
        self.ui.pushButtonInitSpectrograph.pressed.connect(self.init_spectrograph)
        self.ui.pushButtonInitNanoStage.pressed.connect(self.init_nano_stage)
        self.ui.pushButtonInitMicroStage.pressed.connect(self.init_micro_stage)
        self.ui.pushButtonInitDelayStage.pressed.connect(self.init_delay_stage)
        self.windows = {}
        self.windows['Spectroscopy'] = WinSpectroscopy(self.devices)
        self.windows['Spectroscopy'].hide()
        self.ui.pushButtonWinSpectroscopy.pressed.connect(self.windows['Spectroscopy'].show)

        self.windows['Raster'] = WinRaster(self.devices)
        self.windows['Raster'].hide()
        self.ui.pushButtonWinRaster.pressed.connect(self.windows['Raster'].show)

    def closeEvent(self, ev):
        print('Close')
        del self.windows  # If you close main window, should close all other windows and exit
        return super().closeEvent(ev)

    def init_ccd(self):
        """ Initialize CCD camera """

        # Disable init button during initialization
        self.ui.pushButtonInitCCD.setEnabled(False)

        # TODO: Use user-settings for init
        # Default to FVB spectroscopy
        if self.devices['CCD'] is None:

            self.devices['CCD'] = AndorNewton970(settings_kwargs={'exposure_time': 0.0035,
                                                                  'readout_mode': 'FULL_VERTICAL_BINNING',
                                                                  'trigger_mode': 'EXTERNAL'})

            ret = self.devices['CCD'].init_all()
            self.devices['CCD'].set_fast_external_trigger()

            # Indicator light on
            self.ui.radioButtonCCD.setChecked(ret)

        dlg = DialogAndorConfig(ccd=self.devices['CCD'])
        ret = dlg.exec_()
        if ret == 1:
            print('Settings OKd')
        else:
            print('Settings Canceled')

        # Re-enable init button
        self.ui.pushButtonInitCCD.setEnabled(True)

    def init_spectrograph(self):
        """ Initialize Spectrograph """

        # Disable init button during initialization
        self.ui.pushButtonInitSpectrograph.setEnabled(False)

        if 'Spectrograph' not in self.devices:
            self.devices['Spectrograph'] = Acton2300i('COM4')
            self.devices['Spectrograph'].open()
            # Indicator light on
            self.ui.radioButtonSpectrograph.setChecked(True)
        elif self.devices['Spectrograph'] is None:
            self.devices['Spectrograph'] = Acton2300i('COM4')
            self.devices['Spectrograph'].open()
            # Indicator light on
            self.ui.radioButtonSpectrograph.setChecked(True)

        dlg = DialogSpectrographConfig(spec=self.devices['Spectrograph'])
        ret = dlg.exec_()
        if ret == 1:
            print('Settings OKd')
        else:
            print('Settings Canceled')

        # Re-enable init button
        self.ui.pushButtonInitSpectrograph.setEnabled(True)

    def init_nano_stage(self):
        """ Initialize nanostage"""
        self.devices['NanoStage'] = NanoStage()
        self.devices['NanoStage'].open()
        # Disable init button if initialized just fine
        # TODO: Make a small UI to set velocity and acceleration once already initialized
        self.ui.pushButtonInitNanoStage.setEnabled(False)

        # Indicator light on
        self.ui.radioButtonNanoStage.setChecked(True)

    def init_micro_stage(self):
        """Initialize micro stage"""
        self.devices['MicroStage'] = MicroStage()
        self.devices['MicroStage'].open()
        # Disable init button if initialized just fine
        # TODO: Make a small UI to set velocity and acceleration once already initialized
        self.ui.pushButtonInitMicroStage.setEnabled(False)

        # Indicator light on
        self.ui.radioButtonMicroStage.setChecked(True)

    def init_delay_stage(self):
        """ Initialize delay stage"""
        self.devices['DelayStage'] = ESP301(com_port='COM9')
        self.devices['DelayStage'].open()
        # Disable init button if CCD initialized just fine
        self.ui.pushButtonInitDelayStage.setEnabled(False)

        # Indicator light on
        self.ui.radioButtonDelayStage.setChecked(True)


if __name__ == '__main__':
    def blink_light(wdgt):
        wdgt.setChecked(not wdgt.isChecked())

    try:
        # Boilerplate
        app = QApplication(sys.argv)
        app.setStyle("Fusion")
        app.setStyleSheet(stylesheet)
        window = MainWindow()
        screen_geo = app.screens()[0].availableGeometry()
        app_geo = window.geometry()

        window.show()
        window.setGeometry(screen_geo.width() / 2 - app_geo.width() / 2,
                           screen_geo.height() * 0.05, app_geo.width(), app_geo.height())

        window.windows['Raster'].ui.spinBox_left_index.setValue(365)
        window.windows['Raster'].ui.spinBox_right_index.setValue(392)

        app.exec_()
    except Exception:
        print(traceback.format_exc())
    else:
        pass
    finally:
        print('Shutting Down All Devices...')
        if window.devices['CCD']:
            print('CCD...')
            window.devices['CCD'].shutdown()

        if 'NanoStage' in window.devices:
            print('NanoStage...')
            window.devices['NanoStage'].close()

        if 'MicroStage' in window.devices:
            print('MicroStage...')
            window.devices['MicroStage'].close()

        if 'DelayStage' in window.devices:
            print('Delay Stage...')
            window.devices['DelayStage'].close()
