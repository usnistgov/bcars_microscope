import sys
import traceback
from timeit import default_timer as timer
from time import sleep

import matplotlib as mpl
import matplotlib.style
from sympy import N
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
mpl.rcParams['image.interpolation'] = 'none'
mpl.rcParams['image.aspect'] = 'auto'
mpl.rcParams['image.origin'] = 'lower'

import numpy as np

from PySide2.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication, QFileDialog, QMessageBox
from PySide2.QtCore import QTimer, Qt, QThreadPool, QRunnable, QObject, Signal, Slot

from PySide2 import QtCore

from PySide2.QtGui import QPalette, QColor

QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

from ui.ui_bcars2_raster import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure

from bcars_microscope import dark_style_sheet
stylesheet = dark_style_sheet
from bcars_microscope.multithread import Worker
from bcars_microscope.mpl import MplCanvas
from pipython import pitools




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
        toolbar_left.setStyleSheet('font: 14pt "Arial"; color: white')  # Work around to setting the nav toolbar coordinate font size
        toolbar_right = NavigationToolbar2QT(self.ui.mpl_canvas_right, self)
        toolbar_right.setStyleSheet('font: 14pt "Arial"; color: white')  # Work around to setting the nav toolbar coordinate font size
        toolbar_spectra = NavigationToolbar2QT(self.ui.mpl_canvas_spectra, self)
        toolbar_spectra.setStyleSheet('font: 14pt "Arial"; color: white')  # Work around to setting the nav toolbar coordinate font size

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
        # self.ui.mpl_canvas_left.axes.axis('square')
        self.ui.mpl_canvas_left.fig.set_tight_layout(True)
        self.ui.mpl_canvas_left.axes.autoscale(True)
        self.ui.mpl_canvas_left.axes.axis([0,200,0,200])

        # self.ui.mpl_canvas_right.axes.axis('square')
        self.ui.mpl_canvas_right.fig.set_tight_layout(True)
        self.ui.mpl_canvas_right.axes.autoscale(True)
        self.ui.mpl_canvas_right.axes.axis([0,200,0,200])
        

        self.ui.mpl_canvas_left.draw()
        self.ui.mpl_canvas_right.draw()
        self.ui.mpl_canvas_spectra.draw()
        
        # Setup QTimers and threadpool here
        # Intra-imaging spectra and image plotting
        self.timer_update_plots = QTimer()
        self.timer_update_plots.setInterval(1000)
        self.timer_update_plots.timeout.connect(self._midscan_update_plots)
        
        # Threadpool where data collection working will be sent to
        # (see within start_acquisition method)
        self.threadpool = QThreadPool()

        # Signals and Slots
        self.ui.pushButtonStartAcq.pressed.connect(self.start_acquisition)
        # self.ui.pushButtonStopAcq.pressed.connect(self.stop_acquisition)  # Called from within start_acquisition for loop
        self.ui.spinBox_fast_start.editingFinished.connect(self._update_step_sizes)
        self.ui.spinBox_fast_stop.editingFinished.connect(self._update_step_sizes)
        self.ui.spinBox_fast_steps.editingFinished.connect(self._update_step_sizes)

        self.ui.spinBox_slow_start.editingFinished.connect(self._update_step_sizes)
        self.ui.spinBox_slow_stop.editingFinished.connect(self._update_step_sizes)
        self.ui.spinBox_slow_steps.editingFinished.connect(self._update_step_sizes)

        self.ui.spinBox_fixed_start.editingFinished.connect(self._update_step_sizes)
        self.ui.spinBox_fixed_stop.editingFinished.connect(self._update_step_sizes)
        self.ui.spinBox_fixed_steps.editingFinished.connect(self._update_step_sizes)

        self.ui.pushButtonBrowseFiles.pressed.connect(self.select_save_file)

        # Variables
        self._n_spectra_to_collect = 3
        self._reset_state()

        # Functional calls, final
        self._update_step_sizes()

    def select_save_file(self):
        fname,_ = QFileDialog.getSaveFileName(filter='HDF5/H5 (*.h5 *.hdf5)')
        if fname:
            self.ui.lineEditPathFileName.setText(fname)

    @property
    def meta(self):

        output = {}
        output['Raster.Fast.Axis'] = self.ui.comboBoxFast.currentText()
        output['Raster.Fast.Start'] = self.ui.spinBox_fast_start.value()
        output['Raster.Fast.Stop'] = self.ui.spinBox_fast_stop.value()
        output['Raster.Fast.Steps'] = self.ui.spinBox_fast_steps.value()
        output['Raster.Fast.StepSize'] = self._step_size(output['Raster.Fast.Start'],
                                                                output['Raster.Fast.Stop'],
                                                                output['Raster.Fast.Steps'])

        output['Raster.Slow.Axis'] = self.ui.comboBoxSlow.currentText()
        output['Raster.Slow.Start'] = self.ui.spinBox_slow_start.value()
        output['Raster.Slow.Stop'] = self.ui.spinBox_slow_stop.value()
        output['Raster.Slow.Steps'] = self.ui.spinBox_slow_steps.value()
        output['Raster.Slow.StepSize'] = self._step_size(output['Raster.Slow.Start'],
                                                                output['Raster.Slow.Stop'],
                                                                output['Raster.Slow.Steps'])
                            

        output['Raster.Fixed.Axis'] = self.ui.comboBoxFixed.currentText()
        output['Raster.Fixed.Start'] = self.ui.spinBox_fixed_start.value()
        output['Raster.Fixed.Stop'] = self.ui.spinBox_fixed_stop.value()
        output['Raster.Fixed.Steps'] = self.ui.spinBox_fixed_steps.value()
        output['Raster.Fixed.StepSize'] = self._step_size(output['Raster.Fixed.Start'],
                                                                 output['Raster.Fixed.Stop'],
                                                                 output['Raster.Fixed.Steps'])

        return output


    def _update_step_sizes(self):
        sender = self.sender()

        # 3 if's b/c if sender == None, want all 3 to run
        if sender in [self.ui.spinBox_fast_start, self.ui.spinBox_fast_stop, self.ui.spinBox_fast_steps, None]:
            starter = self.ui.spinBox_fast_start.value()
            stopper = self.ui.spinBox_fast_stop.value()
            steps = self.ui.spinBox_fast_steps.value()
            step_size = self._step_size(starter, stopper, steps)
            self.ui.spinBox_fast_stepsize.setValue(step_size)
        if sender in [self.ui.spinBox_slow_start, self.ui.spinBox_slow_stop, self.ui.spinBox_slow_steps, None]:
            starter = self.ui.spinBox_slow_start.value()
            stopper = self.ui.spinBox_slow_stop.value()
            steps = self.ui.spinBox_slow_steps.value()
            step_size = self._step_size(starter, stopper, steps)
            self.ui.spinBox_slow_stepsize.setValue(step_size)
        if sender in [self.ui.spinBox_fixed_start, self.ui.spinBox_fixed_stop, self.ui.spinBox_fixed_steps, None]:
            starter = self.ui.spinBox_fixed_start.value()
            stopper = self.ui.spinBox_fixed_stop.value()
            steps = self.ui.spinBox_fixed_steps.value()
            step_size = self._step_size(starter, stopper, steps)
            self.ui.spinBox_fixed_stepsize.setValue(step_size)


    def _reset_state(self):
        self._midscan_spectra = None  # N spectra that are recorded for each column
        self._midscan_plot_ref = None  # Right-side image array
        self._midscan_img_left = None  # Left-side image array
        self._acq_ct = -1  # How many image columns have been acquired

    def _midscan_update_plots(self):
        if self._acq_ct > 0:
            if self._midscan_spectra is not None:
                if self._midscan_plot_ref is None:
                    self.ui.mpl_canvas_spectra.axes.cla()
                    self._midscan_plot_ref = self.ui.mpl_canvas_spectra.axes.plot(self._midscan_spectra.T)
                else:
                    for entry, new_sp in zip(self._midscan_plot_ref, self._midscan_spectra):
                        entry.set_ydata(new_sp)
                self.ui.mpl_canvas_spectra.draw()

            if self._midscan_img_left is not None:
                self.ui.mpl_canvas_left.axes.cla()
                if self.ui.mpl_canvas_left.cbar is not None: 
                    self.ui.mpl_canvas_left.cbar.remove()
                    self.ui.mpl_canvas_left.cbar = None
                try:
                    minner = self._midscan_img_left[1:,:self._acq_ct].min()
                    img = self.ui.mpl_canvas_left.axes.imshow(self._midscan_img_left[2:,:], vmin=minner)  # Trim off first row
                    self.ui.mpl_canvas_left.cbar = self.ui.mpl_canvas_left.fig.colorbar(img)
                except Exception as e:
                    print('-------------ERROR-----------')
                    print(traceback.format_exc())
                    print(self._midscan_img_left.shape)
                    print(self._midscan_img_left[1:,:self._acq_ct])
                    print(self._acq_ct)
                
                
                self.ui.mpl_canvas_left.draw()
            
    def start_acquisition(self):
        if not self.ui.checkBoxSave.isChecked():
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText('Save NOT selected. Are you sure?')
            msg.setWindowTitle('Not Saving?')
            msg.setInformativeText('YES will not save the data. NO will select save.')
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            # msg.setButtonText(0, 'A')
            msg.setDefaultButton(QMessageBox.Yes)
            out = msg.exec()

            if out == QMessageBox.Yes:
                pass
            else:
                self.ui.checkBoxSave.setChecked(True)

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
            
            self.acq_params = self.meta

            print(self.acq_params)
            self._midscan_img_left = np.zeros((self.acq_params['Raster.Fast.Steps'],self.acq_params['Raster.Slow.Steps']), dtype=np.uint16)

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

            
            self.devices['CCD'].sdk.PrepareAcquisition()
                       
            # Adjust timer for plotting so it's ~1 linescan delay
            self.timer_update_plots.setInterval(1.5 * pixel_time * self.acq_params['Raster.Fast.Steps'])
            # Start QTimer for plotting
            self.timer_update_plots.start()

            self.worker_data_collect = Worker(self._data_collect_thread_run)
            self.worker_data_collect.signals.finished.connect(self._data_collect_thread_finished)

            # Execute Data collection
            self.threadpool.start(self.worker_data_collect)

            
    def _data_collect_thread_finished(self):
        # print('Here - finished')
        self.timer_update_plots.stop()
        self.stop_acquisition()

    def _data_collect_thread_run(self, progress_callback):
        pixel_time = self.devices['CCD'].net_acquisition_time  # Net pixel time estimate
        wait_for_list = []
        slow_step_vec = np.linspace(self.acq_params['Raster.Slow.Start'],
                                    self.acq_params['Raster.Slow.Stop'],
                                    self.acq_params['Raster.Slow.Steps'])

        

        # -- START LOOP
        self._acq_ct = -1
        for num in range(self.acq_params['Raster.Slow.Steps']):
            self._acq_ct += 1
            tmr_per_loop = timer()
            # print('{}/{}'.format(num+1, self.acq_params['Raster.Slow.Steps']))
            if num == 0: # 4. Start if 1st iter
                self.devices['running'] = True
                self.devices['CCD'].start_acquisition()
                sleep(0.001)
                            
            # 5. Wait
            # maybe insert some sort of wait
            # sleep(0.1)

            # 6. WGO
            self.devices['NanoStage'].WGO(1,mode=9)

            # 7. Wait on Stage movement
            tmr = timer()
            sleep((2+self.acq_params['Raster.Fast.Steps'])*pixel_time)  # Wait an extra 2 pixels worth
            # WaitOnTarget takes waaaaaay too long and is not stable
            # pitools.waitontarget(self.devices['NanoStage'], timeout=10, 
            #                      predelay=self.acq_params['Raster.Fast.Steps']*pixel_time*1, polldelay=0.01)
            tmr -= timer()
            
            # temp = self.devices['NanoStage'].gcscommands.IsMoving()
            # print('Is moving: {}. Waited {} sec'.format(any([temp[t] for t in temp]), -tmr))
            print('Waited {} sec'.format(-tmr))
            
            wait_for_list.append(-tmr)
            # 8. Get new images
            ret_code, n_images, first_img, last_img = self.devices['CCD'].get_num_new_images()
            print('New Images: {}'.format(n_images))
            (ret_code, arr, validfirst, validlast) = self.devices['CCD'].get_all_images16()
            if n_images < self.acq_params['Raster.Fast.Steps']:
                print('TOO FEW IMAGES')
                img_arr = np.zeros((self.acq_params['Raster.Fast.Steps'],1600))
            else:
                img_arr = arr.reshape((n_images, -1))
                # print(arr.dtype)

            # 9. Write slice

            # 10. Graphical stuff
            # print('Arr==0: {}'.format((img_arr[1:1+self._n_spectra_to_collect,:]==0).sum()))

            # Idexes of evenly spaces spectra in a single line scan
            sp_idxs = np.arange(2,self.acq_params['Raster.Fast.Steps']-2+1,
                                (self.acq_params['Raster.Fast.Steps']-3)//(self._n_spectra_to_collect-1)).tolist()
            self._midscan_spectra = img_arr[sp_idxs,:]
            self._midscan_img_left[:,num] = 1*img_arr[:,self.ui.spinBox_left_index.value()]
            
        
            # 11. Move slow then fast to next position
            if (num+1) < self.acq_params['Raster.Slow.Steps']:
                if np.abs(self.acq_params['Raster.Slow.StepSize']) > 0.0:
                    next_pos = slow_step_vec[num+1]
                    self.devices['NanoStage'].MOV({self.acq_params['Raster.Slow.Axis']:next_pos})
                if np.abs(self.acq_params['Raster.Fast.StepSize']) > 0.0:
                    self.devices['NanoStage'].MOV({self.acq_params['Raster.Fast.Axis']:self.acq_params['Raster.Fast.Start']})
        
            # Check for Stop Signal
            # QtCore.QCoreApplication.processEvents()
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

       
        # When everything is done
        self.devices['CCD'].stop_acquisition()
        self.devices['running'] = False

    def _step_size(self, start, stop, steps):
        if steps == 1:
            return 0.0
        else:
            return (stop - start) / (steps-1)
  
    def stop_acquisition(self):
        self.timer_update_plots.stop()
        self.devices['CCD'].stop_acquisition()
        self.devices['running'] = False
        print(self.meta)
        self._reset_state()

if __name__ == '__main__':
    from andor_ccd import AndorNewton970
    from pipython import GCSDevice

    just_ui = True

    try:
        # Boilerplate
        app = QApplication(sys.argv)
        app.setStyle("Fusion")
        app.setStyleSheet(stylesheet)

        devices = {}

        if not just_ui:
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
    