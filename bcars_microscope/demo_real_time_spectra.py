import sys
import traceback

import matplotlib as mpl
mpl.use('Qt5Agg')
mpl.rcParams['font.size'] = 20
mpl.rcParams['axes.labelsize'] = 20

import numpy as np

from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication
from PyQt5.QtCore import QTimer, Qt
from PyQt5 import QtCore
from PyQt5.QtGui import QPalette, QColor

QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

from ui.ui_demo_2_threads import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure

try:
    from andor_ccd import AndorNewton970, andor_err_code_str
    from pyAndorSDK2 import atmcd_errors, atmcd_codes
    err_codes = atmcd_errors.Error_Codes
    from esp301 import ESP301

    from pipython import GCS2Commands, GCSDevice, pitools
except:
    pass
else:
    pass

from bcars_microscope import dark_style_sheet
stylesheet = dark_style_sheet


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)

class MainWindow(QMainWindow):
    def __init__(self):
        # Boilerplate stuff
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Create the maptlotlib FigureCanvas object,
        # which defines a single set of axes as self.axes.
        self.ui.mpl_canvas = MplCanvas(self, width=10, height=4, dpi=100)
        self.ui.plot_ref = None
        self.ui.std_ref = None
        self.ui.lgd_ref = None

        self.nrb_spectrum = None
        self.dark_spectrum = None

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar2QT(self.ui.mpl_canvas, self)
        toolbar.setStyleSheet('font: 20pt "Arial"; color: white')  # Work around to setting the nav toolbar coordinate font size

        # Averaging stuff
        self.reset_avg()

        layout = QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(self.ui.mpl_canvas)

        # Create a placeholder widget to hold our toolbar and canvas.
        self.ui.mpl_widget.setLayout(layout)
        self.ui.mpl_canvas.axes.set_xlabel('Pixel')
        self.ui.mpl_canvas.axes.set_ylabel('Counts')
        self.ui.mpl_canvas.axes.set_title('CCD Counts')
        self.ui.mpl_canvas.fig.set_tight_layout(True)
        self.ui.mpl_canvas.axes.autoscale(True)
        # f = Figure()
        # print(f.set_tight_layout())
        # self.ui.
        # self.setCentralWidget(widget)

        self.show()
        self.ui.mpl_canvas.draw()
        
        self.timer_update_plot = QTimer()
        self.timer_update_plot.setInterval(100)
        self.timer_update_plot.timeout.connect(self.update_plot)
        self.timer_update_plot.start()

        self.timer_update_pos = QTimer()
        self.timer_update_pos.setInterval(1000)
        self.timer_update_pos.timeout.connect(self.update_position)
        self.timer_update_pos.start()

        self.timer_update_delay_pos = QTimer()
        self.timer_update_delay_pos.setInterval(1000)
        self.timer_update_delay_pos.timeout.connect(self.update_delay_pos)
        self.timer_update_delay_pos.start()

        # Signals and Slots
        self.ui.pushButton_updatePosition.pressed.connect(self.update_position)
        self.ui.pushButton_setPos_getCurrent.pressed.connect(self.update_position)
        self.ui.pushButton_moveX.pressed.connect(self.inner_move_stage)
        self.ui.pushButton_moveY.pressed.connect(self.inner_move_stage)
        self.ui.pushButton_moveZ.pressed.connect(self.inner_move_stage)
        self.ui.pushButton_moveAll.pressed.connect(self.inner_move_stage)
        self.ui.pushButton_moveCenter.pressed.connect(self.inner_move_stage)
        self.ui.pushButton_moveCenter_Offset.pressed.connect(self.inner_move_stage)
        self.ui.checkBoxAvgOn.stateChanged.connect(self.reset_avg)
        self.ui.spinBoxNAverages.valueChanged.connect(self.reset_avg)
        
        self.ui.pushButtonStartAcq.pressed.connect(self.timer_update_plot.start)
        self.ui.pushButtonStopAcq.pressed.connect(self.timer_update_plot.stop)

        self.ui.pushButtonRecDark.pressed.connect(self.recordSpectrum)
        self.ui.pushButtonRecNRB.pressed.connect(self.recordSpectrum)

        self.ui.pushButtonTimeGoToPos.pressed.connect(self.move_delay)
        self.ui.pushButtonTimeGoToEarly.pressed.connect(self.move_delay)
        self.ui.pushButtonTimeGoToZero.pressed.connect(self.move_delay)
        self.ui.pushButtonTimeGoToLate.pressed.connect(self.move_delay)
        self.ui.pushButtonTimeGoToDark.pressed.connect(self.move_delay)
        self.ui.pushButtonTimeSetZero.pressed.connect(self.set_delay_home)

    def recordSpectrum(self):
        if self.sender() == self.ui.pushButtonRecDark:
            if self.ui.plot_ref is not None:
                self.dark_spectrum = 1*self.ui.plot_ref.get_ydata()
                self.ui.checkBoxSubtractDark.setEnabled(True)

        elif self.sender() == self.ui.pushButtonRecNRB:
            if self.ui.plot_ref is not None:
                self.nrb_spectrum = 1*self.ui.plot_ref.get_ydata()
                self.ui.checkBoxKK.setEnabled(True)

    def reset_avg(self):
        self._avg_on = self.ui.checkBoxAvgOn.isChecked()
        self._avg_num = self.ui.spinBoxNAverages.value()
        self._avg_ct = 0

        self._avg_spectrum_arr = None

        # self.ui.radioButtonAvgDone.setChecked(False)
        self.ui.radioButtonAvgDone.setStyleSheet('QRadioButton::indicator {background-color: rgb(100, 100, 100); border: 2px solid white}')

    def update_position(self):
        locs_dict = get_position()
        if self.sender() == self.ui.pushButton_setPos_getCurrent:
            self.ui.spinBox_x_setpos.setValue(locs_dict['X'])
            self.ui.spinBox_y_setpos.setValue(locs_dict['Y'])
            self.ui.spinBox_z_setpos.setValue(locs_dict['Z'])
        else: # Not from the set from current-position load button
            self.ui.spinBox_x_pos.setValue(locs_dict['X'])
            self.ui.spinBox_y_pos.setValue(locs_dict['Y'])
            self.ui.spinBox_z_pos.setValue(locs_dict['Z'])

    def update_delay_pos(self):
        delay = get_delay()
        self.ui.spinBoxTimeCurrPos.setValue(delay)

    def move_delay(self):
        if self.sender() == self.ui.pushButtonTimeGoToPos:
            new_delay = self.ui.spinBoxTimeGoToPos.value()
        elif self.sender() == self.ui.pushButtonTimeGoToEarly:
            new_delay = 0.01
        elif self.sender() == self.ui.pushButtonTimeGoToZero:
            new_delay = 0.0
        elif self.sender() == self.ui.pushButtonTimeGoToLate:
            new_delay = -0.29
        elif self.sender() == self.ui.pushButtonTimeGoToDark:
            new_delay = 0.3
                
        esp_device.set_pos(new_delay)
        # esp_device.wait_till_done()

    def set_delay_home(self):
        esp_device.set_home()
        
    def update_plot(self):
        xdata, new_spectrum = get_spectrum()

        if self._avg_on & (self._avg_ct == 0):
            self._avg_spectrum_arr = np.zeros((self._avg_num, xdata.size))

        if self._avg_on:
            ct = self._avg_ct % self._avg_num
            self._avg_spectrum_arr[ct, :] = 1*new_spectrum
            
            if self._avg_ct == 0:
                avg_spectrum = 1*new_spectrum
                std_spectrum = 0*new_spectrum
            elif (self._avg_ct > 0) & (self._avg_ct < self._avg_num - 1):
                avg_spectrum = self._avg_spectrum_arr[:self._avg_ct+1,:].mean(axis=0)
                std_spectrum = self._avg_spectrum_arr[:self._avg_ct+1,:].std(axis=0)
            else:
                # print('Average Full')
                # self.ui.radioButtonAvgDone.setChecked(True)
                self.ui.radioButtonAvgDone.setStyleSheet('QRadioButton::indicator {background-color: rgb(85, 255, 0); border: 2px solid white}')
                
                avg_spectrum = self._avg_spectrum_arr.mean(axis=0)
                std_spectrum = self._avg_spectrum_arr.std(axis=0)
            self._avg_ct += 1
        
        if self._avg_on:
            ydata = avg_spectrum
        else:
            ydata = new_spectrum

        if ydata is not None:
            if (self.ui.checkBoxSubtractDark.isChecked()) & (self.dark_spectrum is not None):
                ydata -= self.dark_spectrum

            if self.ui.plot_ref is None:
                self.ui.plot_ref = self.ui.mpl_canvas.axes.plot(xdata, ydata, lw=1, label='Spectrum')[0]
                
                if self._avg_on & self.ui.checkBoxShowStdDev.isChecked():

                    self.ui.std_ref = self.ui.mpl_canvas.axes.fill_between(xdata, ydata-std_spectrum, 
                                                                           ydata+std_spectrum, alpha=0.25,
                                                                           color='C0', label=r'$\pm$1 Std. Dev')
                    self.ui.plot_ref.set_label('Mean Spectrum ({})'.format(self._avg_num))
                    self.ui.lgd_ref = self.ui.mpl_canvas.axes.legend()
                
            else:
                self.ui.plot_ref.set_ydata(xdata)
                self.ui.plot_ref.set_ydata(ydata)
                
                if self._avg_on & self.ui.checkBoxShowStdDev.isChecked():
                    if self.ui.std_ref is not None:
                        self.ui.std_ref.remove()
                        self.ui.std_ref = None
                    self.ui.std_ref = self.ui.mpl_canvas.axes.fill_between(xdata, ydata-std_spectrum, 
                                                                           ydata+std_spectrum, alpha=0.25,
                                                                           color='C0', label=r'$\pm$1 Std. Dev')
                    self.ui.plot_ref.set_label('Mean Spectrum ({})'.format(self._avg_num))
                    if self.ui.lgd_ref is not None:
                        self.ui.lgd_ref.set_visible(True)
                    else:
                        self.ui.lgd_ref = self.ui.mpl_canvas.axes.legend()
                else:
                    if self.ui.std_ref is not None:
                        self.ui.std_ref.remove()
                        self.ui.std_ref = None

                if self.ui.lgd_ref is not None:
                    if not self._avg_on & self.ui.lgd_ref.get_visible():
                        self.ui.lgd_ref.set_visible(False)

            # self.ui.mpl_canvas.axes.set_ylim(bottom=ydata.min()-np.std(ydata), top=ydata.max()+np.std(ydata))
            self.ui.mpl_canvas.draw()
        

    def inner_move_stage(self):
        self.timer_update_pos.stop()
        if self.sender() == self.ui.pushButton_moveX:
            outer_move_stage({'X': self.ui.spinBox_x_setpos.value()})
        elif self.sender() == self.ui.pushButton_moveY:
            outer_move_stage({'Y': self.ui.spinBox_y_setpos.value()})
        elif self.sender() == self.ui.pushButton_moveZ:
            outer_move_stage({'Z': self.ui.spinBox_z_setpos.value()})
        elif self.sender() == self.ui.pushButton_moveAll:
            outer_move_stage({'X': self.ui.spinBox_x_setpos.value(),
                              'Y': self.ui.spinBox_y_setpos.value(),
                              'Z': self.ui.spinBox_z_setpos.value()})
        elif self.sender() == self.ui.pushButton_moveCenter:
            outer_move_stage({'X': 100., 'Y': 100., 'Z': 100.})
        elif self.sender() == self.ui.pushButton_moveCenter_Offset:
            outer_move_stage({'X': 100.,
                              'Y': 100.,
                              'Z': self.ui.spinBox_z_offset.value()})
                              

        else:
            raise ValueError('Move stage error (inner')
        self.timer_update_pos.start()

# def get_position():
#     vals = 2*100*np.random.rand(3)
#     return {'X':vals[0], 'Y':vals[1], 'Z':vals[2]}

if __name__ == '__main__':
    test_mode = False

    if test_mode:
        from scipy.interpolate import interp1d
        pos = {'X':100, 'Y':101, 'Z':102}

        def get_spectrum(n=1600):
            x = [0,100,100, 200, 200, 400, 400, 600, 600, 500, 500, 900, 700, 700, 1000]
            y = [0,0,1000, 0, 1000, 1000, 0, 0, 500, 500, 1000, 1000, 1000, 0, 0]

            x2 = np.hstack((np.arange(101), np.array([100]), np.arange(100,201), np.array(101*[200]),
                            np.arange(200,301), np.array(101*[300]), np.arange(300, 501), np.array(50*[500]),
                            np.arange(500,400-1,-1), np.array(50*[400]), np.arange(400,801), np.arange(800,599,-1),
                            np.array(101*[600]), np.arange(600,901)))
            y2 = np.hstack((np.array(101*[0]), np.array([1000]), np.linspace(1000,0,101), np.linspace(0,1000,101),
                            np.array(101*[1000]), np.linspace(1000,0,101), np.array(201*[0]),
                            np.linspace(0,500,50), np.array(101*[500]), np.linspace(500,1000,50), np.array(401*[1000]),
                            np.array(201*[1000]), np.linspace(1000,0,101), np.array(301*[0])))
            
            return x2, y2 + 30*np.random.randn(y2.size)

        def get_position():
            return pos
        def outer_move_stage(mov_dict):
            pos.update(mov_dict)
            return None
        
        app = QApplication(sys.argv)
        app.setStyle("Fusion")
        app.setStyleSheet(stylesheet)
        window = MainWindow()
        window.show()
        app.exec_()
        
    if not test_mode:
        try:
            ccd = AndorNewton970(settings_kwargs=AndorNewton970.default_fvb)
            ccd.init_sdk()
            ccd.init_camera()
            ccd.sdk.PrepareAcquisition()
            if ccd.is_fvb_or_sgl_track == True:
                    sgl_image_size = ccd.n_cols
            else:
                sgl_image_size = ccd.n_rows * ccd.n_cols

            def get_spectrum():
                sp = ccd.get_last_n_images16()[1]
                return np.arange(sp.size), sp

            pidevice = GCSDevice('E-545')
            try:
                pidevice.ConnectUSB('PI E-517 Display and Interface SN 0114071272')
                print(pidevice.qIDN())
                pidevice.MOV({'X':100.0, 'Y':100.0, 'Z':130.})
            except:
                print(traceback.format_exc())
                pidevice.CloseConnection()
            else:
                def get_position():
                    return pidevice.qPOS()
                def outer_move_stage(mov_dict):
                    pidevice.MOV(mov_dict)
                    return None

            try:
                esp_device = ESP301()
            except Exception as e:
                print(traceback.format_exc())
            else:
                def get_delay():
                    return esp_device.get_pos()



        except Exception as e:
            print('ERROR: {}'.format(traceback.format_exc()))
        else:
            ret_code = ccd.sdk.StartAcquisition()
            print('Starting Acquisition: {} -- {}'.format(ret_code, andor_err_code_str(ret_code)))
            

            app = QApplication(sys.argv)
            app.setStyle("Fusion")
            app.setStyleSheet(stylesheet)
            window = MainWindow()
            window.ui.pushButtonStartAcq.pressed.connect(ccd.start_acquisition)
            window.ui.pushButtonStopAcq.pressed.connect(ccd.stop_acquisition)

            window.show()
            app.exec_()
        finally:
            ccd.sdk.AbortAcquisition()
            ret_code = ccd.sdk.ShutDown()
            print("Function Shutdown returned {}: {}".format(ret_code, err_codes(ret_code).name))
            pidevice.CloseConnection()
            esp_device.close()