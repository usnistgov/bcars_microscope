"""
Main controller for bcars microscope

TODO: Configure Stage
TODO: Configure Delay
TODO: Configure Laser

"""


import sys
import traceback

import numpy as np

from PySide2.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication
from PySide2.QtCore import QTimer, Qt
from PySide2 import QtCore
from PySide2.QtGui import QPalette, QColor

QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

from ui.ui_bcars2_main import Ui_MainWindow
from spectroscopy import MainWindow as WinSpectroscopy
from raster import MainWindow as WinRaster

from andor_ccd import AndorNewton970, DialogAndorConfig
from pipython import GCSDevice
from esp301 import ESP301

from bcars_microscope import dark_style_sheet
stylesheet = dark_style_sheet

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
        self.ui.pushButtonInitNanoStage.pressed.connect(self.init_nano_stage)
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

        #TODO: Use user-settings for init
        # Default to FVB spectroscopy
        if self.devices['CCD'] is None:

            self.devices['CCD'] = AndorNewton970(settings_kwargs={'exposure_time':0.0035,
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


    def init_nano_stage(self):
        """ Initialize nanostage"""
        self.devices['NanoStage'] = GCSDevice('E-545')
        self.devices['NanoStage'].ConnectUSB('PI E-517 Display and Interface SN 0114071272')
        # print('NanoStage ID: {}'.format(self.devices['NanoStage'].qIDN()))
        # Disable init button if CCD initialized just fine
        self.ui.pushButtonInitNanoStage.setEnabled(False)

        # Indicator light on
        self.ui.radioButtonNanoStage.setChecked(True)

    def init_delay_stage(self):
        """ Initialize delay stage"""
        self.devices['DelayStage'] = ESP301()
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
        window.setGeometry(screen_geo.width()/2 - app_geo.width()/2,
                           screen_geo.height()*0.05, app_geo.width(), app_geo.height())


        window.windows['Raster'].ui.spinBox_left_index.setValue(365)
        window.windows['Raster'].ui.spinBox_right_index.setValue(392)

        app.exec_()
    except Exception as e:
        print(traceback.format_exc())
    else:
        pass
    finally:
        print('Shutting Down All Devices...')
        if 'CCD' in window.devices:
            print('CCD...')
            window.devices['CCD'].shutdown()

        if 'NanoStage' in window.devices:
            print('NanoStage...')
            window.devices['NanoStage'].CloseConnection()

        if 'DelayStage' in window.devices:
            print('Delay Stage...')
            window.devices['DelayStage'].close()