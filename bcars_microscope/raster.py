"""
Window for taking a 2D raster scanned image

Started
-------

Not Started
-----------
TODO: Spectral axis selectable and calibratable to wavelength or wavenumber
TODO: Redo check-save messagebox text to be clearer
TODO: Set velocities and acceleration of ESP and Nanostage
TODO: H5 file meta data for Laser
"""

import sys
import traceback
from timeit import default_timer as timer
from time import sleep
import datetime

import h5py

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

import debugpy

from bcars_microscope import dark_style_sheet
stylesheet = dark_style_sheet
from bcars_microscope.multithread import Worker
from bcars_microscope.mpl import MplCanvas
from bcars_microscope.h5 import save_location_is_valid
from pipython import pitools

class ImageParams:
    """Container that describes a single image acqusition
    """    
    def __init__(self, name, nanoscan_params_list, delay, save=False, path_filename=None, groupname=None):
        """Container that describes a single image acqusition

        Parameters
        ----------
        name : str
            Name for image, such as a dataset name.
        ns_list : list
            List of NanoScan params in order [Fast, Slow, Fixed] axes.
        delay : _type_
            Delay stage setting for this image.
        path_filename : str
            Full path including HDF5 filename
        groupname : str
            Group name within HDF5 file. (Note: ImageParams.name will be the dataset name within group)
        """             
        self.ns_list = nanoscan_params_list
        self.delay = delay
        self.name = name
        self.path_filename = path_filename
        self.groupname = groupname
        self.save = save

    @property
    def meta(self):
        output = {}
        for ns in self.ns_list:
            output.update(ns.meta)
        return output

class NanoScanAxisParams:
    """Container describing single-axis NanoScan (stage) settings (for a single image)
    """    
    def __init__(self, axis, start, stop, n_steps, prefix=''):
        """_summary_

        Parameters
        ----------
        axis : str
            X, Y, or Z
        start : float
            Starting position
        stop : float
            Stopping position
        n_steps : int
            Number of steps (minimum 2)
        prefix : str
            Prefix for parameter names such as "Raster.Fast." that will be used for metadata later.
        """        
        assert axis.upper() in ['X', 'Y', 'Z'], 'Axis need be specified as X, Y, or Z'
        self.axis = axis.upper()
        self.start = start
        self.stop = stop
        self.n_steps = n_steps
        self.prefix = prefix

    @property
    def step_vec(self):
        """Vector of steps

        Returns
        -------
        ndarray
            Vector with each step (ideal) position.
        """        
        return np.linspace(self.start, self.stop, self.n_steps)

    @property
    def step_size(self):
        """Step size

        Returns
        -------
        float
            Step size
        """        
        if self.n_steps == 1:
            return 0.0
        else:
            return (self.stop - self.start) / (self.n_steps-1)

    @property
    def meta(self):
        """Metadata

        Returns
        -------
        dict
            Dictionary containing metadata and settings
        """        
        output = {}

        output['{}Axis'.format(self.prefix)] = self.axis
        output['{}Start'.format(self.prefix)] = self.start
        output['{}Stop'.format(self.prefix)] = self.stop
        output['{}Steps'.format(self.prefix)] = self.n_steps
        output['{}StepSize'.format(self.prefix)] = self.step_size
        return output

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
        self.ui.comboBoxFast.currentIndexChanged.connect(self._update_step_sizes)
        self.ui.spinBox_fast_start.editingFinished.connect(self._update_step_sizes)
        self.ui.spinBox_fast_stop.editingFinished.connect(self._update_step_sizes)
        self.ui.spinBox_fast_steps.editingFinished.connect(self._update_step_sizes)

        self.ui.comboBoxSlow.currentIndexChanged.connect(self._update_step_sizes)
        self.ui.spinBox_slow_start.editingFinished.connect(self._update_step_sizes)
        self.ui.spinBox_slow_stop.editingFinished.connect(self._update_step_sizes)
        self.ui.spinBox_slow_steps.editingFinished.connect(self._update_step_sizes)

        self.ui.comboBoxFixed.currentIndexChanged.connect(self._update_step_sizes)
        self.ui.spinBox_fixed_start.editingFinished.connect(self._update_step_sizes)
        self.ui.spinBox_fixed_stop.editingFinished.connect(self._update_step_sizes)
        self.ui.spinBox_fixed_steps.editingFinished.connect(self._update_step_sizes)

        self.ui.spinBox_nrb_fast_start.editingFinished.connect(self._update_nrb_scan_params)
        self.ui.spinBox_nrb_fast_stop.editingFinished.connect(self._update_nrb_scan_params)
        self.ui.spinBox_nrb_fast_steps.editingFinished.connect(self._update_nrb_scan_params)
        self.ui.spinBox_nrb_slow_start.editingFinished.connect(self._update_nrb_scan_params)
        self.ui.spinBox_nrb_slow_stop.editingFinished.connect(self._update_nrb_scan_params)
        self.ui.spinBox_nrb_slow_steps.editingFinished.connect(self._update_nrb_scan_params)
        self.ui.spinBox_nrb_fixed_start.editingFinished.connect(self._update_nrb_scan_params)

        self.ui.pushButtonBrowseFiles.pressed.connect(self.select_save_file)
        self.ui.plainTextEditMemo.textChanged.connect(self.memo_changed_fcn)

        # Variables
        self.nanoscan_fast_params = None
        self.nanoscan_slow_params = None
        self.nanoscan_fixed_params = None
        self.nanoscan_nrb_fast_params = None
        self.nanoscan_nrb_slow_params = None
        self.nanoscan_nrb_fixed_params = None

        self._n_spectra_to_collect = 3
        self._reset_state()

        # Functional calls, final
        self._update_step_sizes()
        self._update_nrb_scan_params()

    def memo_changed_fcn(self):
        self.memo_altered_bool = True
        
    def select_save_file(self):
        fname,_ = QFileDialog.getSaveFileName(filter='HDF5/H5 (*.h5 *.hdf5)', options=QFileDialog.DontConfirmOverwrite)
        if fname:
            self.ui.lineEditPathFileName.setText(fname)



    @property
    def meta(self):

        output = {}
        output.update(self.nanoscan_fast_params.meta)
        output.update(self.nanoscan_slow_params.meta)
        output.update(self.nanoscan_fixed_params.meta)

        output.update(self.nanoscan_nrb_fast_params.meta)
        output.update(self.nanoscan_nrb_slow_params.meta)
        output.update(self.nanoscan_nrb_fixed_params.meta)

        return output

    def _update_nrb_scan_params(self):
        self.nanoscan_nrb_fast_params = NanoScanAxisParams(axis=self.ui.comboBox_nrb_fast_axis.currentText(),
                                              start=self.ui.spinBox_nrb_fast_start.value(),
                                              stop=self.ui.spinBox_nrb_fast_stop.value(),
                                              n_steps=self.ui.spinBox_nrb_fast_steps.value(),
                                              prefix='Raster.NRB.Fast.')
        self.nanoscan_nrb_slow_params = NanoScanAxisParams(axis=self.ui.comboBox_nrb_slow_axis.currentText(),
                                              start=self.ui.spinBox_nrb_slow_start.value(),
                                              stop=self.ui.spinBox_nrb_slow_stop.value(),
                                              n_steps=self.ui.spinBox_nrb_slow_steps.value(),
                                              prefix='Raster.NRB.Slow.')

        self.nanoscan_nrb_fixed_params = NanoScanAxisParams(axis=self.ui.comboBox_nrb_fixed_axis.currentText(),
                                              start=self.ui.spinBox_nrb_fixed_start.value(),
                                              stop=self.ui.spinBox_nrb_fixed_start.value(),
                                              n_steps=1,
                                              prefix='Raster.NRB.Fixed.')

    def _update_step_sizes(self):
        sender = self.sender()

        # 3 if's b/c if sender == None, want all 3 to run
        if sender in [self.ui.spinBox_fast_start, self.ui.spinBox_fast_stop, self.ui.spinBox_fast_steps, None]:
            self.nanoscan_fast_params = NanoScanAxisParams(axis=self.ui.comboBoxFast.currentText(),
                                              start=self.ui.spinBox_fast_start.value(),
                                              stop=self.ui.spinBox_fast_stop.value(),
                                              n_steps=self.ui.spinBox_fast_steps.value(),
                                              prefix='Raster.Fast.')
            self.ui.spinBox_fast_stepsize.setValue(self.nanoscan_fast_params.step_size)

        if sender in [self.ui.spinBox_slow_start, self.ui.spinBox_slow_stop, self.ui.spinBox_slow_steps, None]:
            self.nanoscan_slow_params = NanoScanAxisParams(axis=self.ui.comboBoxSlow.currentText(),
                                              start=self.ui.spinBox_slow_start.value(),
                                              stop=self.ui.spinBox_slow_stop.value(),
                                              n_steps=self.ui.spinBox_slow_steps.value(),
                                              prefix='Raster.Slow.')
            self.ui.spinBox_slow_stepsize.setValue(self.nanoscan_slow_params.step_size)

        if sender in [self.ui.spinBox_fixed_start, self.ui.spinBox_fixed_stop, self.ui.spinBox_fixed_steps, None]:
            self.nanoscan_fixed_params = NanoScanAxisParams(axis=self.ui.comboBoxFixed.currentText(),
                                              start=self.ui.spinBox_fixed_start.value(),
                                              stop=self.ui.spinBox_fixed_stop.value(),
                                              n_steps=self.ui.spinBox_fixed_steps.value(),
                                              prefix='Raster.Fixed.')
            self.ui.spinBox_fixed_stepsize.setValue(self.nanoscan_fixed_params.step_size)

    def _wait_till_not_running(self, predelay=1, delay_bw_polls=1):
        sleep(predelay)
        print('Waiting till running is done')
        while self.devices['running']:
            sleep(delay_bw_polls)

    def _reset_state(self):
        self._midscan_spectra = None  # N spectra that are recorded for each column
        self._midscan_plot_ref = None  # Right-side image array
        self._midscan_img_left = None  # Left-side image array
        self._acq_ct = -1  # How many image columns have been acquired
        self.memo_altered_bool = False  # Has the memo been changed

    def _midscan_update_plots(self):
        rows_to_skip = 1
        cols_to_skip = 2

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
                    if self._midscan_img_left[rows_to_skip:self._acq_ct,cols_to_skip:].size > 0:
                        minner = self._midscan_img_left[rows_to_skip:self._acq_ct,cols_to_skip:].min()
                        img = self.ui.mpl_canvas_left.axes.imshow(self._midscan_img_left[rows_to_skip:,cols_to_skip:], vmin=minner)  # Trim off first col
                        self.ui.mpl_canvas_left.cbar = self.ui.mpl_canvas_left.fig.colorbar(img)
                except Exception as e:
                    print('-------------ERROR-----------')
                    print(traceback.format_exc())
                    print(self._midscan_img_left.shape)
                    # print(self._midscan_img_left[1:,:self._acq_ct])
                    print(self._acq_ct)


                self.ui.mpl_canvas_left.draw()

    def is_ready(self):
        """Returns status information about instrument

        Returns
        -------
        list
            [bool_devices_init, bool_instrument_not_acquiring, description_str]
        """        
        devices_needed = ['CCD', 'NanoStage', 'DelayStage']

        devices_not_ready_list = [nd for nd in devices_needed if nd not in self.devices]
        devices_are_ready = len(devices_not_ready_list) == 0
        
        system_is_free = self.devices['running'] == False

        status_str = ''
        if not devices_are_ready:
            status_str += 'Not all necessary devices are initialized. Need: {}\n'.format(devices_not_ready_list)
        if not system_is_free:
            status_str += 'There is already another acquisition process running.'
        if devices_are_ready & system_is_free:
            status_str += 'The system is ready for acquisition'

        return devices_are_ready, system_is_free, status_str

    def double_check_save(self):
        """Double-check that user meant to NOT save the acquisition
        """        
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

    def start_acquisition(self):

        self.double_check_save()
        yes_save = self.ui.checkBoxSave.isChecked()
        
        if not yes_save:
            pfname = None  # path + filename
            dsetname = None  # dataset name
            grpname = None  # group name
            pth = None  # path
            fname = None  # filename
        else:
            pfname = self.ui.lineEditPathFileName.text()  # Path + filename
            dsetname = self.ui.lineEditDatasetName.text() + '_' + '{}'.format(self.ui.spinBoxDatasetIndex.value()) # Dataset name
            grpname = self.ui.lineEditGroupName.text().rstrip('/') + '/' + dsetname  # Groupname

            try:
                pth,fname = pfname.rsplit('/', 1)
            except:
                pth=None
                fname=None

            # NOTE: Has to write to a new group
            save_loc_valid, save_loc_str = save_location_is_valid(pth, fname, grpname)
            if not save_loc_valid:
                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Warning)
                msg.setText('Save location is not valid.')
                msg.setInformativeText(save_loc_str)
                msg.setWindowTitle('Save location not valid')
                msg.setStandardButtons(QMessageBox.Ok)
                # msg.setButtonText(0, 'A')
                msg.setDefaultButton(QMessageBox.Ok)
                out = msg.exec()
                del pth, fname, grpname, dsetname
                return
            else:
                del pth, fname

            if not self.memo_altered_bool:
                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Warning)
                msg.setText('The memo has not been changed for this acquisition. Continue?')
                msg.setWindowTitle('Memo not updated')
                msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
                # msg.setButtonText(0, 'A')
                msg.setDefaultButton(QMessageBox.Yes)
                out = msg.exec()
                if out == QMessageBox.No:
                    return
                
        devs, not_acq, status_str = self.is_ready()
        print(status_str)
        if not (devs & not_acq):  # System is NOT ready to acquire
            return
        
        # General image settings
        self.devices['CCD'].set_fast_external_trigger()  # External trigger
        pixel_time = self.devices['CCD'].net_acquisition_time  # Per-pixel est time
        wavegen_rate = int(np.ceil(pixel_time/40e-6)) # Set wavegen rate multiplier
        
        # Go ahead and set all axis wavegen rates
        for num in range(1,4):
            self.devices['NanoStage'].WTR(num, wavegen_rate, 0)
            print('Read Wavegen rates: Wavegen {}:{}'.format(num, self.devices['NanoStage'].qWTR(num)))
        print('Read All Wavegen rates: {}'.format(self.devices['NanoStage'].qWTR()))

        # Nanoscan parameter list for each image to be taken
        to_scan_img_list = []

        # NRB_early, Dark, NRB so that we END on the same delay we'll use for the main imaging
        if self.ui.comboBoxRecNRB.currentText() in ['Before', 'Both']:
            if self.ui.checkBoxCollectNRB_Early.isChecked():
                ns_param_list = [self.nanoscan_nrb_fast_params, self.nanoscan_nrb_slow_params, self.nanoscan_nrb_fixed_params]
                delay = self.ui.spinBoxDelayNRB_Early.value()
                to_scan_img_list.append(ImageParams('NRB_Early_Pre', ns_param_list, delay, save=yes_save, 
                                                    path_filename=pfname, groupname=grpname))

            if self.ui.checkBoxCollectDark.isChecked():
                ns_param_list = [self.nanoscan_nrb_fast_params, self.nanoscan_nrb_slow_params, self.nanoscan_nrb_fixed_params]
                delay = self.ui.spinBoxDelayDark.value()
                to_scan_img_list.append(ImageParams('Dark_Pre', ns_param_list, delay, save=yes_save,
                                                    path_filename=pfname, groupname=grpname))

            if self.ui.checkBoxCollectNRB.isChecked():
                ns_param_list = [self.nanoscan_nrb_fast_params, self.nanoscan_nrb_slow_params, self.nanoscan_nrb_fixed_params]
                delay = self.ui.spinBoxDelayNRB.value()
                to_scan_img_list.append(ImageParams('NRB_Pre', ns_param_list, delay, save=yes_save,
                                                    path_filename=pfname, groupname=grpname))

        ns_param_list = [self.nanoscan_fast_params, self.nanoscan_slow_params, self.nanoscan_fixed_params]
        delay = self.ui.spinBoxDelayImaging.value()
        to_scan_img_list.append(ImageParams(dsetname, ns_param_list, delay, save=yes_save,
                                            path_filename=pfname, groupname=grpname))

        # NRB, NRB_early, Dark, so we start at the same time as the main imaging
        if self.ui.comboBoxRecNRB.currentText() in ['After', 'Both']:
            if self.ui.checkBoxCollectNRB.isChecked():
                ns_param_list = [self.nanoscan_nrb_fast_params, self.nanoscan_nrb_slow_params, self.nanoscan_nrb_fixed_params]
                delay = self.ui.spinBoxDelayNRB.value()
                to_scan_img_list.append(ImageParams('NRB_Post', ns_param_list, delay, save=yes_save,
                                                    path_filename=pfname, groupname=grpname))

            if self.ui.checkBoxCollectNRB_Early.isChecked():
                ns_param_list = [self.nanoscan_nrb_fast_params, self.nanoscan_nrb_slow_params, self.nanoscan_nrb_fixed_params]
                delay = self.ui.spinBoxDelayNRB_Early.value()
                to_scan_img_list.append(ImageParams('NRB_Early_Post', ns_param_list, delay, save=yes_save,
                                                    path_filename=pfname, groupname=grpname))

            if self.ui.checkBoxCollectDark.isChecked():
                ns_param_list = [self.nanoscan_nrb_fast_params, self.nanoscan_nrb_slow_params, self.nanoscan_nrb_fixed_params]
                delay = self.ui.spinBoxDelayDark.value()
                to_scan_img_list.append(ImageParams('Dark_Post', ns_param_list, delay, save=yes_save,
                                                    path_filename=pfname, groupname=grpname))

        # Adjust timer for plotting so it's ~1 linescan delay
        # TODO Dynamically adjust plotting timer
        # self.timer_update_plots.setInterval(1.5 * pixel_time * self.acq_params['Raster.NRB.Fast.Steps'])
        self.timer_update_plots.setInterval(1)

        # Start QTimer for plotting
        self.timer_update_plots.start()

        self.worker_data_collect = Worker(self._data_collect_thread_run, to_scan_img_list)
        self.worker_data_collect.signals.finished.connect(self._data_collect_thread_finished)
        self.worker_data_collect.signals.progress.connect(self.progress_fn)

        # Execute Data collection
        self.threadpool.start(self.worker_data_collect)

    def _data_collect_thread_finished(self):
        # self.worker_data_collect.signals.progress.disconnect()
        self.stop_acquisition()
        self.devices['running'] = False

    def _data_collect_thread_run(self, img_list, progress_callback):
        try:
            debugpy.debug_this_thread()
        except ConnectionRefusedError:
            pass

        self.devices['running'] = True  # Need this for timing
        
        axis_str_to_num = {'X':1, 'Y':2, 'Z': 3}
        
        n_image_steps = len(img_list)  # may not be true if there are multiple fixed axes
        
        try:
            if img_list[0].save == True:
                fid = h5py.File(img_list[0].path_filename,'a')
                grp = fid.create_group(img_list[0].groupname)
                print('Data will be saved to group: {}'.format(img_list[0].groupname))
            else:
                fid = None
                grp = None
            
            for iter_imgs, img_inst in enumerate(img_list):

                # Delay position
                self.devices['DelayStage'].set_pos(img_inst.delay)


                # NANOSTAGE SETUP
                self.devices['NanoStage'].WAV_LIN(table=axis_str_to_num[img_inst.ns_list[0].axis],
                                                firstpoint=0, numpoints=img_inst.ns_list[0].n_steps,
                                                append='X', speedupdown=0,
                                                amplitude=img_inst.ns_list[0].stop-img_inst.ns_list[0].start,
                                                offset=img_inst.ns_list[0].start,
                                                seglength=img_inst.ns_list[0].n_steps)

                # Make sure delay stage is done moving
                self.devices['DelayStage'].wait_till_done(n_iter=10, pause=1, let_settle=True, settle_pause=0.25)

                n_fixed_steps = img_inst.ns_list[2].n_steps
                fixed_step_vec = img_inst.ns_list[2].step_vec

                for num_z_stack in range(n_fixed_steps):

                    curr_fixed_pos = fixed_step_vec[num_z_stack]

                    if img_inst.save == True:
                        if n_fixed_steps == 1:
                            dset_name = img_inst.name
                        else:
                            dset_name = img_inst.name + '_z{}'.format(num_z_stack)
                        dset = grp.create_dataset(dset_name, shape=(img_inst.ns_list[1].n_steps,img_inst.ns_list[0].n_steps,1600),
                                                dtype=np.uint16)
                        # WRITE ATTRIBUTES
                        dset.attrs.update(img_inst.meta)
                        dset.attrs.update(self.devices['CCD'].meta)
                        dset.attrs['TimeStage.Position'] = img_inst.delay
                        dset.attrs['Memo'] = self.ui.plainTextEditMemo.toPlainText()
                        dset.attrs['Date'] = '{}'.format(datetime.datetime.now())
                        dset.attrs[img_inst.ns_list[2].prefix + 'Position'] = curr_fixed_pos
                    else:
                        dset = None
                    
                    # Plotting setup
                    self._midscan_img_left = np.zeros((img_inst.ns_list[1].n_steps,img_inst.ns_list[0].n_steps), dtype=np.uint16)


                    # CCD Preparation
                    # TODO: consider moving outside of loop
                    self.devices['CCD'].sdk.PrepareAcquisition()

                    # 3. Move Slow, Fast, then Fixed
                    self.devices['NanoStage'].MOV({img_inst.ns_list[1].axis:img_inst.ns_list[1].start})
                    self.devices['NanoStage'].MOV({img_inst.ns_list[0].axis:img_inst.ns_list[0].start})
                    self.devices['NanoStage'].MOV({img_inst.ns_list[2].axis:curr_fixed_pos})

                    self._acq_ct = -1
                    for num in range(img_inst.ns_list[1].n_steps):
                        self._acq_ct += 1
                        tmr_per_loop = timer()
                        if num == 0: # 4. Start if 1st iter
                            self.devices['CCD'].start_acquisition()
                            sleep(0.001)

                        # 5. Wait
                        # maybe insert some sort of wait
                        # sleep(0.1)

                        # 6. WGO
                        self.devices['NanoStage'].WGO(1,mode=9)

                        # 7. Wait on Stage movement
                        tmr = timer()
                        sleep((2+img_inst.ns_list[0].n_steps)*self.devices['CCD'].net_acquisition_time)  # Wait an extra 2 pixels worth
                        # WaitOnTarget takes waaaaaay too long and is not stable
                        # pitools.waitontarget(self.devices['NanoStage'], timeout=10,
                        #                      predelay=self.acq_params['Raster.Fast.Steps']*pixel_time*1, polldelay=0.01)
                        tmr -= timer()

                        print('Waited {} sec'.format(-tmr))

                        # 8. Get new images
                        ret_code, n_images, first_img, last_img = self.devices['CCD'].get_num_new_images()
                        print('New Images: {}'.format(n_images))
                        (ret_code, arr, validfirst, validlast) = self.devices['CCD'].get_all_images16()
                        if n_images < img_inst.ns_list[0].n_steps:
                            print('TOO FEW IMAGES')
                            img_arr = np.zeros((img_inst.ns_list[0].n_steps,1600))
                        else:
                            img_arr = arr.reshape((n_images, -1))
                            # print(arr.dtype)
                        
                        if dset is not None:
                            dset[num,:,:] = 1*img_arr
                        # 9. Write slice

                        # 10. Graphical stuff
                        # print('Arr==0: {}'.format((img_arr[1:1+self._n_spectra_to_collect,:]==0).sum()))

                        # Idexes of evenly spaces spectra in a single line scan
                        sp_idxs = np.arange(2,img_inst.ns_list[0].n_steps-2+1,
                                            (img_inst.ns_list[0].n_steps-3)//(self._n_spectra_to_collect-1)).tolist()
                        self._midscan_spectra = img_arr[sp_idxs,:]

                        # print('Img_left shape:{}'.format(self._midscan_img_left.shape))
                        # print('Img Arr Shape: {}'.format(img_arr.shape))

                        self._midscan_img_left[num,:] = 1*img_arr[:,self.ui.spinBox_left_index.value()]


                        # 11. Move slow then fast to next position
                        if (num+1) < img_inst.ns_list[1].n_steps:
                            if np.abs(img_inst.ns_list[1].step_size) > 0.0:
                                next_pos = img_inst.ns_list[1].step_vec[num+1]
                                self.devices['NanoStage'].MOV({img_inst.ns_list[1].axis:next_pos})
                            if np.abs(img_inst.ns_list[0].step_size) > 0.0:
                                self.devices['NanoStage'].MOV({img_inst.ns_list[0].axis:img_inst.ns_list[0].start})

                        # Check for Stop Signal
                        # QtCore.QCoreApplication.processEvents()
                        if self.ui.pushButtonStopAcq.isChecked():
                            print('STOPPING...')
                            self.ui.pushButtonStopAcq.setChecked(False)
                            break

                        tmr_per_loop -= timer()
                        print('Time per loop: {} sec'.format(-tmr_per_loop))
                        progress_callback.emit(num+1, img_inst.ns_list[1].n_steps, 'Image columns complete: ')
                            # self.devices['CCD'].stop_acquisition()
                    # -- END LOOP
                    # 12. Move Z to end position
                    self.devices['NanoStage'].MOV({'Z':self.ui.spinBox_post_image_z_pos.value()})

                    # 13. Abort CCD and Free memory
                    self.devices['CCD'].stop_acquisition()
                    self.devices['CCD'].free_memory()
                    # 14. Close H5 file
                    progress_callback.emit(iter_imgs+1, n_image_steps, 'Fixed-Axis Imaging steps: ')

                progress_callback.emit(iter_imgs+1, n_image_steps, 'Imaging steps: ')
        except Exception as e:
            print(traceback.format_exc())
        finally:
            if fid is not None:
                print('Closing HDF5 file.')
                fid.close()

            # Increment image index if previous data was saved
            if img_inst.save:
                self.ui.spinBoxDatasetIndex.stepUp()
            # This is now in thread finished fcn
            # self.devices['running'] = False

    def progress_fn(self, num, num_of, desc):
        print('{} {} / {}'.format(desc, num, num_of))

    def stop_acquisition(self):
        self.timer_update_plots.stop()
        self.devices['CCD'].stop_acquisition()
        self.devices['CCD'].free_memory()
        self._reset_state()

if __name__ == '__main__':
    from andor_ccd import AndorNewton970
    from pipython import GCSDevice
    from esp301 import ESP301

    just_ui = False

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

            devices['DelayStage'] = ESP301(com_port='COM9')
        window = MainWindow(devices=devices)
        # print('Meta data:')
        # print(window.meta)

        window.ui.spinBox_slow_steps.setValue(12)
        window.ui.spinBox_slow_steps.editingFinished.emit()
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

        if 'DelayStage' in window.devices:
            print('Delay Stage...')
            window.devices['DelayStage'].close()
