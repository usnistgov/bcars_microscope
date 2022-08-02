
"""
Window for taking a 2D raster scanned image

Started
-------

Not Started
-----------
TODO: Spectral axis selectable and calibratable to wavelength or wavenumber
TODO: Redo check-save messagebox text to be clearer
TODO: H5 file meta data for Laser
TODO: Clear plots (or reference) before a 2nd scan
QUESTION: Does acceleration affect over- and under-scanning?
"""

import datetime
from timeit import default_timer as timer
from cycler import cycler
from time import sleep
import h5py
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QTimer, QThreadPool
from PyQt5 import QtCore
from ui.ui_bcars2_macro import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from bcars_microscope import dark_style_sheet
# from bcars_microscope.multithread import Worker
from bcars_microscope.mpl import MplCanvas
from bcars_microscope.h5 import save_location_is_valid
from bcars_microscope.raster import NanoScanAxisParams
from bcars_microscope.devices import AbstractDevice

import sys
import traceback
# import datetime
# import h5py
import matplotlib as mpl
import matplotlib.style
import numpy as np
from scipy.interpolate import interp1d
# import debugpy

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

MPL_BG_COLOR = (53 / 255, 53 / 255, 53 / 255)
mpl.rcParams['figure.facecolor'] = MPL_BG_COLOR
mpl.rcParams['axes.facecolor'] = MPL_BG_COLOR
# print(mpl.style.available)

mpl.rcParams['lines.linewidth'] = 0.5
mpl.rcParams['axes.prop_cycle'] = cycler(color=['white', '#FF911F', '#00A3BF',
                                                '#A239A0', '#DE350B',
                                                '#36B37E'])
mpl.rcParams['image.interpolation'] = 'none'
mpl.rcParams['image.aspect'] = 'auto'
mpl.rcParams['image.origin'] = 'lower'

QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

stylesheet = dark_style_sheet


class MacroImageParams:
    """Container that describes a single image acqusition
    """
    def __init__(self, name, macroscan_params_list, nanoscan_params_list, delay, save=False, path_filename=None, groupname=None):
        """Container that describes a single image acqusition using the large area stage

        Parameters
        ----------
        name : str
            Name for image, such as a dataset name.
        macro_list : list
            List of NanoScan params in order [Fast, Slow, Fixed] axes.
        ns_list : list
            List of NanoScan params in order [Fast, Slow, Fixed] axes.
        delay : _type_
            Delay stage setting for this image.
        path_filename : str
            Full path including HDF5 filename
        groupname : str
            Group name within HDF5 file. (Note: MacroImageParams.name will be the dataset name within group)
        """
        self.macro_list = macroscan_params_list
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


class MacroScanAxisParams:
    """Container describing single-axis MacroScan (stage) settings (for a single image)
    """
    def __init__(self, axis, start, stop, n_steps, dwell_time, velocity=1., is_fast=False, prefix=''):
        """_summary_

        Parameters
        ----------
        axis : str
            X, Y
        start : float
            Starting position
        stop : float
            Stopping position
        n_steps : int
            Number of steps (minimum 2)
        dwell_time : float
            Time per pixel (s)
        velocity : float
            Velocity of axis (mm/s)
        is_fast : bool
            Is this the fast axis.
        prefix : str
            Prefix for parameter names such as "Raster.Fast." that will be used for metadata later.
        """
        assert axis.upper() in ['X', 'Y'], 'Axis need be specified as X, Y'
        self.is_fast = None
        self.prefix = prefix
        self.dt = dwell_time
        self._velocity = velocity

        self._start = None
        self._stop = None
        self._n_steps = None

        self.axis = axis.upper()
        self.start = start
        self.stop = stop
        self.n_steps = n_steps
        self.is_fast = is_fast
        self.update_velocity()

    @property
    def velocity(self):
        return self._velocity

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        self._start = value
        self.update_velocity()

    @property
    def stop(self):
        return self._stop

    @stop.setter
    def stop(self, value):
        self._stop = value
        self.update_velocity()

    @property
    def n_steps(self):
        return self._n_steps

    @n_steps.setter
    def n_steps(self, value):
        self._n_steps = value
        self.update_velocity()

    @property
    def dt(self):
        return self._dt

    @dt.setter
    def dt(self, value):
        self._dt = value
        self.update_velocity()

    def update_velocity(self):
        if self.is_fast:
            ss = self.step_size
            # From p 59 (or 55) of the C867 manual
            # maximum velocity = Stepsize * 20 kHz / 2
            velocity = ss / self.dt  # mm/s
            self._velocity = velocity
            print(self._velocity)
            if (velocity >= ss * 20e3 / 2):
                raise Warning('Under these conditions, velocity need be < {:.3f} mm/s'.format(ss * 20e3 / 2))
            elif velocity > 100:
                raise Warning('Velocity must be < 100 mm/s')

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

            ss = (self.stop - self.start) / (self.n_steps - 1)
            # print(self.start)
            # print(self.stop)
            # print(self.n_steps)
            # print('Step Size: {}'.format(ss))
            return ss

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
        output['{}Velocity'.format(self.prefix)] = self.velocity
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
        # self.ui.mpl_canvas_left.axes.axis([0, 200, 0, 200])

        # self.ui.mpl_canvas_right.axes.axis('square')
        self.ui.mpl_canvas_right.fig.set_tight_layout(True)
        self.ui.mpl_canvas_right.axes.autoscale(True)
        # self.ui.mpl_canvas_right.axes.axis([0, 200, 0, 200])

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

        # self.ui.comboBoxFast.currentIndexChanged.connect(self._update_step_sizes)
        self.ui.spinBoxMacroFastStart.editingFinished.connect(self._update_step_sizes)
        self.ui.spinBoxMacroFastStop.editingFinished.connect(self._update_step_sizes)
        self.ui.spinBoxMacroFastSteps.editingFinished.connect(self._update_step_sizes)

        # self.ui.comboBoxSlow.currentIndexChanged.connect(self._update_step_sizes)
        self.ui.spinBoxMacroSlowStart.editingFinished.connect(self._update_step_sizes)
        self.ui.spinBoxMacroSlowStop.editingFinished.connect(self._update_step_sizes)
        self.ui.spinBoxMacroSlowSteps.editingFinished.connect(self._update_step_sizes)

        # self.ui.comboBoxFixed.currentIndexChanged.connect(self._update_step_sizes)
        self.ui.spinBoxFixedStart.editingFinished.connect(self._update_step_sizes)
        self.ui.spinBoxFixedStop.editingFinished.connect(self._update_step_sizes)
        self.ui.spinBoxFixedSteps.editingFinished.connect(self._update_step_sizes)

        # self.ui.spinBox_nrb_fast_start.editingFinished.connect(self._update_nrb_scan_params)
        # self.ui.spinBox_nrb_fast_stop.editingFinished.connect(self._update_nrb_scan_params)
        # self.ui.spinBox_nrb_fast_steps.editingFinished.connect(self._update_nrb_scan_params)
        # self.ui.spinBox_nrb_slow_start.editingFinished.connect(self._update_nrb_scan_params)
        # self.ui.spinBox_nrb_slow_stop.editingFinished.connect(self._update_nrb_scan_params)
        # self.ui.spinBox_nrb_slow_steps.editingFinished.connect(self._update_nrb_scan_params)
        # self.ui.spinBox_nrb_fixed_start.editingFinished.connect(self._update_nrb_scan_params)

        self.ui.pushButtonBrowseFiles.pressed.connect(self.select_save_file)
        # self.ui.plainTextEditMemo.textChanged.connect(self.memo_changed_fcn)

        # self.ui.pushButtonMacroXY.pressed.connect(self.update_macro)
        # self.ui.pushButtonMacroXZ.pressed.connect(self.update_macro)
        # self.ui.pushButtonMacroLowRes.pressed.connect(self.update_macro)
        # self.ui.pushButtonMacroHighRes.pressed.connect(self.update_macro)
        # self.ui.pushButtonMacroXYRange.pressed.connect(self.update_macro)
        # self.ui.pushButtonMacroXZRange.pressed.connect(self.update_macro)

        # Variables
        # self.nanoscan_fast_params = None
        # self.nanoscan_slow_params = None
        # self.nanoscan_fixed_params = None
        # self.nanoscan_nrb_fast_params = None
        # self.nanoscan_nrb_slow_params = None
        # self.nanoscan_nrb_fixed_params = None

        self._n_spectra_to_collect = 3
        self._reset_state()

        # Functional calls, final
        self._update_step_sizes()
        # self._update_nrb_scan_params()

    def memo_changed_fcn(self):
        self.memo_altered_bool = True

    def select_save_file(self):
        fname, _ = QFileDialog.getSaveFileName(filter='HDF5/H5 (*.h5 *.hdf5)',
                                               options=QFileDialog.DontConfirmOverwrite)
        if fname:
            self.ui.lineEditPathFileName.setText(fname)

    def update_macro(self):
        """ Run when macro buttons are pressed """
        sender = self.sender()

        if sender == self.ui.pushButtonMacroXY:
            self.ui.comboBoxFast.setCurrentIndex(0)
            self.ui.comboBoxSlow.setCurrentIndex(1)
            self.ui.comboBoxFixed.setCurrentIndex(2)
            self._update_step_sizes(ignore_sender=True)
        elif sender == self.ui.pushButtonMacroXZ:
            self.ui.comboBoxFast.setCurrentIndex(0)
            self.ui.comboBoxSlow.setCurrentIndex(2)
            self.ui.comboBoxFixed.setCurrentIndex(1)
            self._update_step_sizes(ignore_sender=True)
        elif sender == self.ui.pushButtonMacroLowRes:
            self.ui.spinBox_fast_steps.setValue(50)
            self.ui.spinBox_slow_steps.setValue(50)
            self._update_step_sizes(ignore_sender=True)
        elif sender == self.ui.pushButtonMacroHighRes:
            self.ui.spinBox_fast_steps.setValue(300)
            self.ui.spinBox_slow_steps.setValue(300)
            self._update_step_sizes(ignore_sender=True)
        elif sender == self.ui.pushButtonMacroXYRange:
            self.ui.spinBox_fast_start.setValue(1)
            self.ui.spinBox_fast_stop.setValue(199)
            self.ui.spinBox_slow_start.setValue(1)
            self.ui.spinBox_slow_stop.setValue(199)
            self._update_step_sizes(ignore_sender=True)
        elif sender == self.ui.pushButtonMacroXZRange:
            self.ui.spinBox_fast_start.setValue(1)
            self.ui.spinBox_fast_stop.setValue(199)
            self.ui.spinBox_slow_start.setValue(70)
            self.ui.spinBox_slow_stop.setValue(130)
            self._update_step_sizes(ignore_sender=True)
        # print(self.nanoscan_slow_params.__dict__)

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

    # def _update_nrb_scan_params(self):
    #     self.nanoscan_nrb_fast_params = NanoScanAxisParams(axis=self.ui.comboBox_nrb_fast_axis.currentText(),
    #                                           start=self.ui.spinBox_nrb_fast_start.value(),
    #                                           stop=self.ui.spinBox_nrb_fast_stop.value(),
    #                                           n_steps=self.ui.spinBox_nrb_fast_steps.value(),
    #                                           prefix='Raster.NRB.Fast.')
    #     self.nanoscan_nrb_slow_params = NanoScanAxisParams(axis=self.ui.comboBox_nrb_slow_axis.currentText(),
    #                                           start=self.ui.spinBox_nrb_slow_start.value(),
    #                                           stop=self.ui.spinBox_nrb_slow_stop.value(),
    #                                           n_steps=self.ui.spinBox_nrb_slow_steps.value(),
    #                                           prefix='Raster.NRB.Slow.')

    #     self.nanoscan_nrb_fixed_params = NanoScanAxisParams(axis=self.ui.comboBox_nrb_fixed_axis.currentText(),
    #                                           start=self.ui.spinBox_nrb_fixed_start.value(),
    #                                           stop=self.ui.spinBox_nrb_fixed_start.value(),
    #                                           n_steps=1,
    #                                           prefix='Raster.NRB.Fixed.')

    def _update_step_sizes(self, ignore_sender=False):
        # dt = self.devices['CCD'].net_acquisition_time
        dt = self.devices['CCD'].settings['exposure_time']

        if not ignore_sender:
            sender = self.sender()
        else:
            sender = None
        # print('Sender: {}'.format(sender))

        # 3 if's b/c if sender == None, want all 3 to run
        if sender in [self.ui.spinBoxMacroFastStart, self.ui.spinBoxMacroFastStop, self.ui.spinBoxMacroFastSteps, None]:
            try:
                self.macroscan_fast_params = MacroScanAxisParams(axis=self.ui.comboBoxFast.currentText(),
                                                                 start=self.ui.spinBoxMacroFastStart.value(),
                                                                 stop=self.ui.spinBoxMacroFastStop.value(),
                                                                 n_steps=self.ui.spinBoxMacroFastSteps.value(),
                                                                 dwell_time=dt,
                                                                 is_fast=True,
                                                                 prefix='Macro.Raster.Fast.')
            except Warning as e:
                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Warning)
                msg.setText('{}'.format(e))
                msg.setWindowTitle('Velocity too large')
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.exec()
                print('Warning: {}'.format(e))
                self.ui.spinBoxMacroFastStart.setValue(self.macroscan_fast_params.start)
                self.ui.spinBoxMacroFastStop.setValue(self.macroscan_fast_params.stop)
                self.ui.spinBoxMacroFastSteps.setValue(self.macroscan_fast_params.n_steps)
            finally:
                self.ui.spinBoxMacroFastStepSize.setValue(self.macroscan_fast_params.step_size)
                self.ui.spinBoxMacroFastVelocity.setValue(self.macroscan_fast_params.velocity)

        if sender in [self.ui.spinBoxMacroSlowStart, self.ui.spinBoxMacroSlowStop, self.ui.spinBoxMacroSlowSteps, None]:
            self.macroscan_slow_params = MacroScanAxisParams(axis=self.ui.comboBoxSlow.currentText(),
                                                             start=self.ui.spinBoxMacroSlowStart.value(),
                                                             stop=self.ui.spinBoxMacroSlowStop.value(),
                                                             n_steps=self.ui.spinBoxMacroSlowSteps.value(),
                                                             dwell_time=dt,
                                                             prefix='Macro.Raster.Slow.')
            self.ui.spinBoxMacroSlowStepSize.setValue(self.macroscan_slow_params.step_size)

        if sender in [self.ui.spinBoxFixedStart, self.ui.spinBoxFixedStop, self.ui.spinBoxFixedSteps, None]:
            self.nanoscan_fixed_params = NanoScanAxisParams(axis=self.ui.comboBoxFixed.currentText(),
                                                            start=self.ui.spinBoxFixedStart.value(),
                                                            stop=self.ui.spinBoxFixedStop.value(),
                                                            n_steps=self.ui.spinBoxFixedSteps.value(),
                                                            prefix='Macro.Raster.Fixed.')
            self.ui.spinBoxFixedStepSize.setValue(self.nanoscan_fixed_params.step_size)

    def _wait_till_not_running(self, predelay=1, delay_bw_polls=1):
        sleep(predelay)
        print('Waiting till running is done')
        while self.devices['running']:
            sleep(delay_bw_polls)

    def _reset_state(self):
        self._midscan_spectra = None  # N spectra that are recorded for each column
        self._midscan_plot_ref = None  # Reference to spectral plot
        self._midscan_img_left = None  # Left-side image array
        self._midscan_img_right = None  # Right-side image array
        self._acq_ct = -1  # How many image columns have been acquired
        self.memo_altered_bool = False  # Has the memo been changed

    def _midscan_update_plots(self):
        rows_to_skip = 0
        cols_to_skip = 0

        extent = [self.nanoscan_fast_params.start, self.nanoscan_fast_params.stop,
                  self.nanoscan_slow_params.start, self.nanoscan_slow_params.stop]

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
                    if self._midscan_img_left[rows_to_skip:self._acq_ct, cols_to_skip:].size > 0:
                        minner = self._midscan_img_left[rows_to_skip:self._acq_ct, cols_to_skip:].min()
                        img = self.ui.mpl_canvas_left.axes.imshow(self._midscan_img_left[rows_to_skip:, cols_to_skip:], vmin=minner, extent=extent)  # Trim off first col
                        self.ui.mpl_canvas_left.cbar = self.ui.mpl_canvas_left.fig.colorbar(img)
                except Exception:
                    print('-------------ERROR-----------')
                    print(traceback.format_exc())
                    print(self._midscan_img_left.shape)
                    # print(self._midscan_img_left[1:, :self._acq_ct])
                    print(self._acq_ct)

                self.ui.mpl_canvas_left.draw()

            if self._midscan_img_right is not None:
                self.ui.mpl_canvas_right.axes.cla()
                if self.ui.mpl_canvas_right.cbar is not None:
                    self.ui.mpl_canvas_right.cbar.remove()
                    self.ui.mpl_canvas_right.cbar = None
                try:
                    if self._midscan_img_right[rows_to_skip:self._acq_ct, cols_to_skip:].size > 0:
                        minner = self._midscan_img_right[rows_to_skip:self._acq_ct, cols_to_skip:].min()
                        img = self.ui.mpl_canvas_right.axes.imshow(self._midscan_img_right[rows_to_skip:, cols_to_skip:], vmin=minner, extent=extent)  # Trim off first col
                        self.ui.mpl_canvas_right.cbar = self.ui.mpl_canvas_right.fig.colorbar(img)
                except Exception:
                    print('-------------ERROR-----------')
                    print(traceback.format_exc())
                    print(self._midscan_img_right.shape)
                    # print(self._midscan_img_right[1:, :self._acq_ct])
                    print(self._acq_ct)

                self.ui.mpl_canvas_right.draw()

    def is_ready(self):
        """Returns status information about instrument

        Returns
        -------
        list
            [bool_devices_init, bool_instrument_not_acquiring, description_str]
        """
        devices_needed = ['CCD', 'NanoStage', 'DelayStage', 'MicroStage']

        devices_not_ready_list = [nd for nd in devices_needed if nd not in self.devices]
        devices_are_ready = len(devices_not_ready_list) == 0

        system_is_free = self.devices['running'] is False

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
            msg.buttons()[0].setText('Don\'t Save')
            msg.buttons()[1].setText('Yes, Save')
            # msg.buttons[0].setText('TEST')
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
            dsetname = self.ui.lineEditDatasetName.text() + '_' + '{}'.format(self.ui.spinBoxDatasetIndex.value())  # Dataset name
            grpname = self.ui.lineEditGroupName.text().rstrip('/') + '/' + dsetname  # Groupname

            try:
                pth, fname = pfname.rsplit('/', 1)
            except Exception:
                pth = None
                fname = None

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
                _ = msg.exec()
                del pth, fname, grpname, dsetname
                return
            else:
                del pth, fname

        #     if not self.memo_altered_bool:
        #         msg = QMessageBox(self)
        #         msg.setIcon(QMessageBox.Warning)
        #         msg.setText('The memo has not been changed for this acquisition. Continue?')
        #         msg.setWindowTitle('Memo not updated')
        #         msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        #         # msg.setButtonText(0, 'A')
        #         msg.setDefaultButton(QMessageBox.Yes)
        #         out = msg.exec()
        #         if out == QMessageBox.No:
        #             return

        devs, not_acq, status_str = self.is_ready()
        print(status_str)
        if not (devs & not_acq):  # System is NOT ready to acquire
            return

        # General image settings
        self.devices['CCD'].set_internal_trigger()  # Internal trigger
        self.devices['CCD'].sdk.PrepareAcquisition()
        self.do_acquire()

    def do_acquire(self):
        yes_save = self.ui.checkBoxSave.isChecked()

        if not yes_save:
            pfname = None  # path + filename
            dsetname_prefix = None  # dataset name
            grpname = None  # group name
            pth = None  # path
            fname = None  # filename
        else:
            pfname = self.ui.lineEditPathFileName.text()  # Path + filename
            dsetname_prefix = self.ui.lineEditDatasetName.text() + '_' + '{}'.format(self.ui.spinBoxDatasetIndex.value())  # Dataset name
            grpname = self.ui.lineEditGroupName.text().rstrip('/') + '/' + dsetname_prefix  # Groupname

            try:
                pth, fname = pfname.rsplit('/', 1)
            except Exception:
                pth = None
                fname = None

        devs, not_acq, status_str = self.is_ready()
        print(status_str)
        if not (devs & not_acq):  # System is NOT ready to acquire
            return

        if yes_save:
            fid = h5py.File(pfname, 'a')
            grp = fid.create_group(grpname)
            print('Data will be saved to group: {}'.format(grpname))
        else:
            fid = None
            grp = None

        print('DO ACQUIRE')
        self.devices['running'] = True  # Need this for timing

        print(self.macroscan_fast_params.__dict__)
        print(self.macroscan_slow_params.__dict__)
        print(self.nanoscan_fixed_params.__dict__)

        fast_axis = self.macroscan_fast_params.axis
        velocity = self.macroscan_fast_params.velocity
        self.devices['MicroStage'].set_velocity({self.devices['MicroStage'].axis_to_num[fast_axis]: velocity})
        slow_axis = self.macroscan_slow_params.axis

        slow_steps = self.macroscan_slow_params.n_steps

        _midscan_plot_ref = None

        try:
            device_meta = {}
            for k in self.devices:
                if isinstance(self.devices[k], AbstractDevice):
                    print('{} is a device'.format(k))
                    device_meta.update(self.devices[k].meta)
            device_meta.update(self.devices['CCD'].meta)
            device_meta['Memo'] = self.ui.plainTextEditMemo.toPlainText()
            device_meta['Date'] = '{}'.format(datetime.datetime.now())

            for num in range(slow_steps):
                fast_pos_sample_vec = []
                slow_pos_sample_vec = []
                n_images_at_pos_samples = []

                # tmr = timer()
                print('============= {} / {} ============'.format(num + 1, slow_steps))
                self.devices['MicroStage'].set_position({self.devices['MicroStage'].axis_to_num[fast_axis]: self.macroscan_fast_params.start,
                                                         self.devices['MicroStage'].axis_to_num[slow_axis]: self.macroscan_slow_params.step_vec[num]})
                # 3. Move Slow, Fast, then Fixed
                self.devices['NanoStage'].set_position({'Y': self.ui.spinBoxYPosition.value()})
                self.devices['NanoStage'].set_position({'X': self.ui.spinBoxXPosition.value()})

                while self.devices['MicroStage'].is_moving():
                    sleep(0.1)
                curr_pos = self.devices['MicroStage'].get_position()
                fast_pos_sample_vec.append(curr_pos[self.devices['MicroStage'].axis_to_num[fast_axis]])
                slow_pos_sample_vec.append(curr_pos[self.devices['MicroStage'].axis_to_num[slow_axis]])
                n_images_at_pos_samples = [0]
                print('Ready for line scan')
                self.devices['NanoStage'].set_position({'Z': self.nanoscan_fixed_params.start})  # Put Z in last

                self.devices['CCD'].start_acquisition()
                tmr = timer()
                self.devices['MicroStage'].set_position({self.devices['MicroStage'].axis_to_num[fast_axis]: self.macroscan_fast_params.stop})

                temp_fast_pos, temp_fast_n_imgs = self.devices['MicroStage'].wait_till_near(self.devices['MicroStage'].axis_to_num[fast_axis],
                                                                                            self.macroscan_fast_params.start,
                                                                                            self.macroscan_fast_params.stop,
                                                                                            threshold=0.01, pause=0.001,
                                                                                            per_iter_fcn=lambda: self.devices['CCD'].get_num_new_images()[1])
                self.devices['CCD'].stop_acquisition()
                tmr -= timer()
                self.devices['NanoStage'].set_position({'Z': self.ui.spinBox_post_image_z_pos.value()})
                print('Time per iteration: {}'.format(-tmr))
                fast_pos_sample_vec.extend(temp_fast_pos)
                slow_pos_sample_vec.extend([slow_pos_sample_vec[-1]] * len(temp_fast_pos))
                n_images_at_pos_samples.extend(temp_fast_n_imgs)

                ret_code, n_images, first_img, last_img = self.devices['CCD'].get_num_new_images()
                print('New Images: {}'.format(n_images))
                print('Velocity: {}'.format(self.devices['MicroStage'].get_velocity()))
                print(fast_pos_sample_vec)

                # Needed the extra n_images* thus also needed the extra positional info
                # else interpolation range problems for plotting
                n_images_at_pos_samples.append(n_images)
                curr_pos = self.devices['MicroStage'].get_position()
                fast_pos_sample_vec.append(curr_pos[self.devices['MicroStage'].axis_to_num[fast_axis]])
                slow_pos_sample_vec.append(curr_pos[self.devices['MicroStage'].axis_to_num[slow_axis]])

                (ret_code, arr, validfirst, validlast) = self.devices['CCD'].get_all_images16()
                arr = arr.reshape((n_images, -1))

                if fid is not None:
                    dset_name = dsetname_prefix + '_slow_{}'.format(num)
                    dset = grp.create_dataset(dset_name, data=1 * arr, dtype=np.uint16)
                    dset.attrs.update(device_meta)
                    dset.attrs['MicroStage.raster.slow.pos'] = curr_pos[self.devices['MicroStage'].axis_to_num[slow_axis]]
                    dset.attrs['MicroStage.raster.slow.pos_sample_vec'] = slow_pos_sample_vec
                    dset.attrs['MicroStage.raster.fast.pos_sample_vec'] = fast_pos_sample_vec
                    dset.attrs['MicroStage.raster.fast.n_images_at_pos_samples'] = n_images_at_pos_samples
                    print('Writing to dataset: {}'.format(dset_name))

                # if n_fixed_steps == 1:
                #             dset_name = img_inst.name
                #         else:
                #             dset_name = img_inst.name + '_z{}'.format(num_z_stack)
                #         dset = grp.create_dataset(dset_name, shape=(img_inst.ns_list[1].n_steps, img_inst.ns_list[0].n_steps, 1600),
                #                                   dtype=np.uint16)
                #         # WRITE ATTRIBUTES
                #         dset.attrs.update(img_inst.meta)

                #         dset.attrs.update(self.devices[k].meta)
                # dset.attrs.update(self.devices['CCD'].meta)
                # dset.attrs['TimeStage.Position'] = img_inst.delay
                # dset.attrs['Memo'] = self.ui.plainTextEditMemo.toPlainText()
                # dset.attrs['Date'] = '{}'.format(datetime.datetime.now())
                # dset.attrs[img_inst.ns_list[2].prefix + 'Position'] = curr_fixed_pos

                sp_idxs = np.arange(n_images)[1:: n_images // (self._n_spectra_to_collect - 1) - 1]
                _midscan_spectra = arr[sp_idxs, :]

                if _midscan_plot_ref is None:
                    self.ui.mpl_canvas_spectra.axes.cla()
                    _midscan_plot_ref = self.ui.mpl_canvas_spectra.axes.plot(_midscan_spectra.T)
                else:
                    for entry, new_sp in zip(_midscan_plot_ref, _midscan_spectra):
                        entry.set_ydata(new_sp)
                self.ui.mpl_canvas_spectra.draw()
                self.ui.mpl_canvas_spectra.flush_events()

                interp_n_imgs_to_pos = interp1d(n_images_at_pos_samples, fast_pos_sample_vec, kind='linear')

                try:
                    self.ui.mpl_canvas_left.axes.scatter(interp_n_imgs_to_pos(np.arange(n_images)), [slow_pos_sample_vec[0]] * n_images, c=arr[:, 1000], marker='s')
                    self.ui.mpl_canvas_left.draw()
                    self.ui.mpl_canvas_left.flush_events()
                except Exception:
                    print(traceback.format_exc())
                    print('N Images: {}'.format(n_images))
                    print(len(n_images_at_pos_samples), len(fast_pos_sample_vec))

                # tmr -= timer()
                # print('Time per iteration: {}'.format(-tmr))
        except Exception:
            print(traceback.format_exc())
        finally:
            if fid is not None:
                try:
                    fid.close()
                except Exception:
                    print(traceback.format_exc())
            self.devices['running'] = False
            if yes_save:
                self.ui.spinBoxDatasetIndex.setValue(self.ui.spinBoxDatasetIndex.value() + 1)

    def stop_acquisition(self):
        self.timer_update_plots.stop()
        self.devices['CCD'].stop_acquisition()
        self.devices['CCD'].free_memory()
        self._reset_state()


if __name__ == '__main__':

    from andor_ccd import AndorNewton970
    from pi_nano_stage import NanoStage
    from pi_micro_stage import MicroStage
    from esp301 import ESP301

    just_ui = False

    try:
        # Boilerplate
        app = QApplication(sys.argv)
        app.setStyle("Fusion")
        app.setStyleSheet(stylesheet)

        devices = {}

        if not just_ui:
            devices['CCD'] = AndorNewton970(settings_kwargs={'exposure_time': 0.0035, 'readout_mode': 'FULL_VERTICAL_BINNING',
                                                             'trigger_mode': 'EXTERNAL'})

            devices['CCD'].init_all()
            devices['CCD'].set_fast_external_trigger()

            devices['NanoStage'] = NanoStage()
            devices['NanoStage'].open()

            devices['MicroStage'] = MicroStage()
            devices['MicroStage'].open()

            devices['DelayStage'] = ESP301(com_port='COM9')
            devices['DelayStage'].open()

        window = MainWindow(devices=devices)
        # print('Meta data:')
        # print(window.meta)

        # window.ui.spinBox_slow_steps.setValue(12)
        # window.ui.spinBox_slow_steps.editingFinished.emit()
        window.ui.spinBox_left_index.setValue(365)
        window.ui.spinBox_right_index.setValue(392)

        window.show()

        app.exec_()
    except Exception:
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
            window.devices['NanoStage'].close()

        if 'MicroStage' in window.devices:
            print('MicroStage...')
            window.devices['MicroStage'].close()

        if 'DelayStage' in window.devices:
            print('Delay Stage...')
            window.devices['DelayStage'].close()
