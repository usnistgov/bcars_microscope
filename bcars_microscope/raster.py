import sys
import traceback
from timeit import default_timer as timer
from time import sleep

import matplotlib as mpl
import matplotlib.style
mpl.style.use('seaborn-dark-palette')
mpl.use('Qt5Agg')
mpl.rcParams['font.size'] = 11

TEXT_COLOR = 'white'
mpl.rcParams['text.color'] = TEXT_COLOR
mpl.rcParams['axes.labelcolor'] = TEXT_COLOR
mpl.rcParams['axes.edgecolor'] = TEXT_COLOR
mpl.rcParams['xtick.color'] = TEXT_COLOR
mpl.rcParams['ytick.color'] = TEXT_COLOR

mpl.rcParams['axes.labelsize'] = 11
# print(mpl.rcParams)

MPL_BG_COLOR = (53/255,53/255,53/255)
mpl.rcParams['figure.facecolor'] = MPL_BG_COLOR
mpl.rcParams['axes.facecolor'] = MPL_BG_COLOR
# print(mpl.style.available)

mpl.rcParams['lines.linewidth'] = 0.5
from cycler import cycler
mpl.rcParams['axes.prop_cycle'] = cycler(color=['white', '#FF911F', '#00A3BF', '#A239A0','#DE350B', '#36B37E'])


import numpy as np

from PySide2.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication
from PySide2.QtCore import QTimer, Qt

from PySide2 import QtCore

from PySide2.QtGui import QPalette, QColor

QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

from ui.ui_bcars2_raster import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure

from bcars_microscope import dark_style_sheet
stylesheet = dark_style_sheet

from pipython import pitools

class MplCanvas(FigureCanvasQTAgg):
    """ Matplotlib Canvas """
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)

class MainWindow(QMainWindow):
    def __init__(self, devices={}):
        # Boilerplate stuff
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.devices = devices
        self.devices['running'] = False

        # Create the maptlotlib FigureCanvas object,
        # which defines a single set of axes as self.axes.
        self.ui.mpl_canvas_left = MplCanvas(self, width=10, height=4, dpi=100)
        self.ui.mpl_canvas_right = MplCanvas(self, width=10, height=4, dpi=100)
        self.ui.mpl_canvas_spectra = MplCanvas(self, width=10, height=4, dpi=100)
        
        # MPL Stuff
        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar_left = NavigationToolbar2QT(self.ui.mpl_canvas_left, self)
        toolbar_left.setStyleSheet('font: 16pt "Arial"; color: white')  # Work around to setting the nav toolbar coordinate font size
        toolbar_right = NavigationToolbar2QT(self.ui.mpl_canvas_right, self)
        toolbar_right.setStyleSheet('font: 16pt "Arial"; color: white')  # Work around to setting the nav toolbar coordinate font size
        toolbar_spectra = NavigationToolbar2QT(self.ui.mpl_canvas_spectra, self)
        toolbar_spectra.setStyleSheet('font: 16pt "Arial"; color: white')  # Work around to setting the nav toolbar coordinate font size

        # Create a layout to house our MPL widget
        layout_left = QVBoxLayout()
        layout_left.addWidget(toolbar_left)
        layout_left.addWidget(self.ui.mpl_canvas_left)
        layout_right = QVBoxLayout()
        layout_right.addWidget(toolbar_right)
        layout_right.addWidget(self.ui.mpl_canvas_right)
        layout_spectra = QVBoxLayout()
        layout_spectra.addWidget(toolbar_spectra)
        layout_spectra.addWidget(self.ui.mpl_canvas_spectra)


        # Using the placeholder widget (mpl_widget) to hold our toolbar and canvas.
        self.ui.mpl_widget_left.setLayout(layout_left)
        self.ui.mpl_widget_right.setLayout(layout_right)
        self.ui.mpl_widget_spectra.setLayout(layout_spectra)
        # self.ui.mpl_canvas.axes.set_xlabel('Pixel')
        # self.ui.mpl_canvas.axes.set_ylabel('Counts')
        # self.ui.mpl_canvas.axes.set_title('CCD Counts')
        self.ui.mpl_canvas_left.axes.axis('square')
        self.ui.mpl_canvas_left.fig.set_tight_layout(True)
        self.ui.mpl_canvas_left.axes.autoscale(True)
        self.ui.mpl_canvas_left.axes.axis([0,200,0,200])

        self.ui.mpl_canvas_right.axes.axis('square')
        self.ui.mpl_canvas_right.fig.set_tight_layout(True)
        self.ui.mpl_canvas_right.axes.autoscale(True)
        self.ui.mpl_canvas_right.axes.axis([0,200,0,200])
        

        self.ui.mpl_canvas_left.draw()
        self.ui.mpl_canvas_right.draw()
        self.ui.mpl_canvas_spectra.draw()
        
        # Setup QTimers here

        # Signals and Slots
        self.ui.pushButtonStartAcq.pressed.connect(self.start_acquisition)
        
    # def showEvent(self, ev):
    #     """ This happens when the window is shown"""
    #     self.timer_update_pos.start()
    #     self.timer_update_delay_pos.start()
    #     return QWidget.showEvent(self, ev)

    # def hideEvent(self, ev):
    #     """ This happens when the window is hidden"""
    #     self.timer_update_pos.stop()
    #     self.timer_update_delay_pos.stop()
    #     return QWidget.hideEvent(self, ev)

    def start_acquisition(self):
        check_devices = 'CCD' in self.devices
        check_devices &= 'NanoStage' in self.devices
        check_devices &= 'DelayStage' in self.devices

        check_nothing_running = (self.devices['running'] == False)
        
        if not check_devices:
            print('Not all necessary devices are initialized')
        elif not check_nothing_running:
            print('Another process is acquiring data at the moment. Stop it and try again.')
        elif check_devices & check_nothing_running:
            if self.devices['CCD'].is_internal_trigger:
                self.devices['CCD'].set_fast_external_trigger()
            
            # self.timer_update_plot.start()

            self.acq_params = {}
            self.acq_params['Raster.Fast.Axis'] = self.ui.comboBoxFast.currentText()
            self.acq_params['Raster.Fast.Start'] = self.ui.spinBox_fast_start.value()
            self.acq_params['Raster.Fast.Stop'] = self.ui.spinBox_fast_stop.value()
            self.acq_params['Raster.Fast.Steps'] = self.ui.spinBox_fast_steps.value()
            self.acq_params['Raster.Fast.StepSize'] = self._step_size(self.acq_params['Raster.Fast.Start'],
                                                                      self.acq_params['Raster.Fast.Stop'],
                                                                      self.acq_params['Raster.Fast.Steps'])

            self.acq_params['Raster.Slow.Axis'] = self.ui.comboBoxSlow.currentText()
            self.acq_params['Raster.Slow.Start'] = self.ui.spinBox_slow_start.value()
            self.acq_params['Raster.Slow.Stop'] = self.ui.spinBox_slow_stop.value()
            self.acq_params['Raster.Slow.Steps'] = self.ui.spinBox_slow_steps.value()
            self.acq_params['Raster.Slow.StepSize'] = self._step_size(self.acq_params['Raster.Slow.Start'],
                                                                      self.acq_params['Raster.Slow.Stop'],
                                                                      self.acq_params['Raster.Slow.Steps'])
            slow_step_vec = np.linspace(self.acq_params['Raster.Slow.Start'],
                                        self.acq_params['Raster.Slow.Stop'],
                                        self.acq_params['Raster.Slow.Steps'])                   

            self.acq_params['Raster.Fixed.Axis'] = self.ui.comboBoxFixed.currentText()
            self.acq_params['Raster.Fixed.Start'] = self.ui.spinBox_fixed_start.value()
            self.acq_params['Raster.Fixed.Stop'] = self.ui.spinBox_fixed_stop.value()
            self.acq_params['Raster.Fixed.Steps'] = self.ui.spinBox_fixed_steps.value()
            self.acq_params['Raster.Fixed.StepSize'] = self._step_size(self.acq_params['Raster.Fixed.Start'],
                                                                       self.acq_params['Raster.Fixed.Stop'],
                                                                       self.acq_params['Raster.Fixed.Steps'])
            print(self.acq_params)

            axis_str_to_num = {'X':1, 'Y':2, 'Z': 3}

            self.devices['NanoStage'].WAV_LIN(table=axis_str_to_num[self.acq_params['Raster.Fast.Axis']],
                                              firstpoint=0, numpoints=self.acq_params['Raster.Fast.Steps'], 
                                              append='X', speedupdown=0, 
                                              amplitude=self.acq_params['Raster.Fast.Stop']-self.acq_params['Raster.Fast.Start'], 
                                              offset=self.acq_params['Raster.Fast.Start'], 
                                              seglength=self.acq_params['Raster.Fast.Steps'])

            # Set wavegen rate multiplier
            pixel_time = self.devices['CCD'].net_acquisition_time  # Net pixel time estimate
            wavegen_rate = int(np.ceil(pixel_time/40e-6))
            self.devices['NanoStage'].WTR(axis_str_to_num[self.acq_params['Raster.Fast.Axis']], wavegen_rate, 0)
            print('Wave generator ({}) multiplier: {}'.format(axis_str_to_num[self.acq_params['Raster.Fast.Axis']], wavegen_rate))
            
            # From LabView
            # 1. Open H5 stuff
            # 2. Write attributes
            # 3. Move Slow, Fast, then Fixed
            self.devices['NanoStage'].MOV({self.acq_params['Raster.Slow.Axis']:self.acq_params['Raster.Slow.Start']})
            self.devices['NanoStage'].MOV({self.acq_params['Raster.Fast.Axis']:self.acq_params['Raster.Fast.Start']})
            self.devices['NanoStage'].MOV({self.acq_params['Raster.Fixed.Axis']:self.acq_params['Raster.Fixed.Start']})

            # -- START LOOP

            wait_for_list = []
            for num in range(self.acq_params['Raster.Slow.Steps']):
                tmr_per_loop = timer()
                # print('{}/{}'.format(num+1, self.acq_params['Raster.Slow.Steps']))
                if num == 0: # 4. Start if 1st iter
                    self.devices['running'] = True
                    self.devices['CCD'].start_acquisition()
                                
                # 5. Wait
                # maybe insert some sort of wait
                # sleep(0.1)

                # 6. WGO
                self.devices['NanoStage'].WGO(1,mode=9)

                # 7. Wait on Stage movement
                tmr = timer()
                sleep(self.acq_params['Raster.Fast.Steps']*pixel_time)
                # WaitOnTarget takes waaaaaay too long and is not stable
                # pitools.waitontarget(self.devices['NanoStage'], timeout=10, 
                #                      predelay=self.acq_params['Raster.Fast.Steps']*pixel_time*1, polldelay=0.01)
                tmr -= timer()
                temp = self.devices['NanoStage'].gcscommands.IsMoving()
                print('Is moving: {}. Waited {} sec'.format(any([temp[t] for t in temp]), -tmr))
                print(self.devices['NanoStage'].qPOS())
                wait_for_list.append(-tmr)
                # 8. Get new images
                ret_code, n_images, first_img, last_img = self.devices['CCD'].get_num_new_images()
                print('New Images: {}'.format(n_images))
                (ret_code, arr, validfirst, validlast) = self.devices['CCD'].get_all_images16()
                if validfirst == 0:
                    pass
                    # n_images = validlast-validfirst
                else:
                    n_images = validlast-validfirst + 1
                    img_arr = arr.reshape((n_images, -1))
                    # print(img_arr.shape)

                # 9. Write slice
                # 10. Graphical stuff
                # self.ui.mpl_canvas_spectra.axes.cla()
                # self.ui.mpl_canvas_spectra.axes.plot(np.arange(img_arr.shape[-1]), img_arr[:4,:].T)
                # self.ui.mpl_canvas_spectra.draw()

                # 11. Move slow then fast to next position
                if (num+1) < self.acq_params['Raster.Slow.Steps']:
                    if np.abs(self.acq_params['Raster.Slow.StepSize']) > 0.0:
                        next_pos = slow_step_vec[num+1]
                        self.devices['NanoStage'].MOV({self.acq_params['Raster.Slow.Axis']:next_pos})
                    if np.abs(self.acq_params['Raster.Fast.StepSize']) > 0.0:
                        self.devices['NanoStage'].MOV({self.acq_params['Raster.Fast.Axis']:self.acq_params['Raster.Fast.Start']})
            
                # Check for Stop Signal
                QtCore.QCoreApplication.processEvents()
                if self.ui.pushButtonStopAcq.isChecked():
                    print('STOPPING...')
                    self.ui.pushButtonStopAcq.setChecked(False)
                    break

                tmr_per_loop -= timer()
                print('Time per loop: {} sec'.format(-tmr_per_loop))

                # self.devices['CCD'].stop_acquisition()
            # -- END LOOP
            # 12. Move Z to end position
            self.devices['NanoStage'].MOV({'Z':self.ui.spinBox_post_image_z_pos.value()})

            # 13. Abort CCD and Free memory
            self.devices['CCD'].stop_acquisition()
            self.devices['CCD'].free_memory()

            # 14. Close H5 file

            print(self.devices['NanoStage'].qPOS())
            self.ui.mpl_canvas_spectra.axes.plot(wait_for_list)

       
        # When everything is done
        self.devices['CCD'].stop_acquisition()
        self.devices['running'] = False

    def _step_size(self, start, stop, steps):
        if steps == 1:
            return 0.0
        else:
            return (stop - start) / (steps-1)
    # def _wav_str_fast(self):
    #     
    #     axis = axis_str_to_num[self.acq_params['Raster.Fast.Axis']]
    #     start = self.acq_params['Raster.Fast.Start']
    #     stop = self.acq_params['Raster.Fast.Stop']
    #     steps = self.acq_params['Raster.Fast.Steps']

    #     output = 'WAV {} X LIN {} {} {} {} 0 0'.format(axis, steps, stop-start, start, steps)
    #     return output
    # def stop_acquisition(self):
    #     if 'CCD' in self.devices:
    #         self.devices['CCD'].stop_acquisition()
    #         self.devices['running'] = False
    #         self.timer_update_plot.stop()

    # def get_spectrum(self):
    #     if 'CCD' in self.devices:
    #         sp = 1.*self.devices['CCD'].get_last_n_images16()[1]
    #         return np.arange(sp.size), sp

    # def get_position(self):
    #     if 'NanoStage' in self.devices:
    #         return self.devices['NanoStage'].qPOS()

    
    # def move_delay(self):
    #     if 'DelayStage' in self.devices:
    #         if self.sender() == self.ui.pushButtonTimeGoToPos:
    #             new_delay = self.ui.spinBoxTimeGoToPos.value()
    #         elif self.sender() == self.ui.pushButtonTimeGoToEarly:
    #             new_delay = 0.01
    #         elif self.sender() == self.ui.pushButtonTimeGoToZero:
    #             new_delay = 0.0
    #         elif self.sender() == self.ui.pushButtonTimeGoToLate:
    #             new_delay = -0.29
    #         elif self.sender() == self.ui.pushButtonTimeGoToDark:
    #             new_delay = 0.3
                
    #         self.devices['DelayStage'].set_pos(new_delay)
        

    # def move_nano_stage(self):
    #     if 'NanoStage' in self.devices:
    #         self.timer_update_pos.stop()
    #         if self.sender() == self.ui.pushButton_moveX:
    #             self.devices['NanoStage'].MOV({'X': self.ui.spinBox_x_setpos.value()})
    #         elif self.sender() == self.ui.pushButton_moveY:
    #             self.devices['NanoStage'].MOV({'Y': self.ui.spinBox_y_setpos.value()})
    #         elif self.sender() == self.ui.pushButton_moveZ:
    #             self.devices['NanoStage'].MOV({'Z': self.ui.spinBox_z_setpos.value()})
    #         elif self.sender() == self.ui.pushButton_moveAll:
    #             self.devices['NanoStage'].MOV({'X': self.ui.spinBox_x_setpos.value(),
    #                             'Y': self.ui.spinBox_y_setpos.value(),
    #                             'Z': self.ui.spinBox_z_setpos.value()})
    #         elif self.sender() == self.ui.pushButton_moveCenter:
    #             self.devices['NanoStage'].MOV({'X': 100., 'Y': 100., 'Z': 100.})
    #         elif self.sender() == self.ui.pushButton_moveCenter_Offset:
    #             self.devices['NanoStage'].MOV({'X': 100.,
    #                             'Y': 100.,
    #                             'Z': self.ui.spinBox_z_offset.value()})
                                

    #         else:
    #             raise ValueError('Move stage error (inner')
    #         self.timer_update_pos.start()

        

if __name__ == '__main__':
    from andor_ccd import AndorNewton970
    from pipython import GCSDevice

    try:
        # Boilerplate
        app = QApplication(sys.argv)
        app.setStyle("Fusion")
        app.setStyleSheet(stylesheet)

        devices = {}
        devices['CCD'] = AndorNewton970(settings_kwargs={'exposure_time':0.0035,'read_mode': 'FULL_VERTICAL_BINNING',
                                                          'trigger_mode': 'EXTERNAL'})
        
        devices['CCD'].init_all()
        devices['CCD'].set_fast_external_trigger()

        devices['NanoStage'] = GCSDevice('E-545')
        devices['NanoStage'].ConnectUSB('PI E-517 Display and Interface SN 0114071272')

        devices['DelayStage'] = -1
        window = MainWindow(devices=devices)
        
        window.show()

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

        # if 'DelayStage' in window.devices:
        #     print('Delay Stage...')
        #     window.devices['DelayStage'].close()
    