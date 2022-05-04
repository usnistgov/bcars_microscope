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
from PySide2.QtCore import QTimer, Qt, QThreadPool, QRunnable, QObject, Signal, Slot

from PySide2 import QtCore

from PySide2.QtGui import QPalette, QColor

QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

from ui_learn_multithread import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure

from bcars_microscope import dark_style_sheet
stylesheet = dark_style_sheet

from pipython import pitools

class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    progress
        int indicating % progress

    '''
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)

class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress

    @Slot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done

class MplCanvas(FigureCanvasQTAgg):
    """ Matplotlib Canvas """
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
        
        # MPL Stuff
        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar2QT(self.ui.mpl_canvas, self)
        
        # Create a layout to house our MPL widget
        layout = QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(self.ui.mpl_canvas)
        
        # Using the placeholder widget (mpl_widget) to hold our toolbar and canvas.
        self.ui.mpl_widget.setLayout(layout)
        
        self.ui.mpl_canvas.axes.axis('square')
        self.ui.mpl_canvas.fig.set_tight_layout(True)
        self.ui.mpl_canvas.axes.autoscale(True)
        self.ui.mpl_canvas.axes.axis([0,200,0,200])

        self.ui.mpl_canvas.draw()

        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())
           
        # Setup QTimers here
        self.data = None
        self.timer_update_plot = QTimer()
        self.timer_update_plot.setInterval(1000)
        self.timer_update_plot.timeout.connect(self.update_plot)
        

        # Signals and Slots
        self.ui.pushButtonStartAcq.pressed.connect(self.start_acquisition)
        self.ui.pushButtonStopAcq.pressed.connect(self.stop_acquisition)
        
        
    def start_acquisition(self):
        self.ui.pushButtonStartAcq.setEnabled(False)
        print('START acquisition')
        self.plot_ref = None
        self.data = None
        self.data_is_new = False
        
        
        self.plot_count = 0

        self.timer_update_plot.start()
        worker = Worker(self.get_data)
        # worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        # worker.signals.progress.connect(self.progress_fn)

        # Execute
        self.threadpool.start(worker)

        # self.timer_update_plot.stop()
        print('Number of plots: {}'.format(self.plot_count))
        self.plot_ref = None
        print('STOP acquisition')
        self.ui.pushButtonStartAcq.setEnabled(True)

    def thread_complete(self):
        self.timer_update_plot.stop()

    def get_data(self, progress_callback):
        tmr_loop_list = []
        for num in range(50):
            print(num)
            self.data = np.random.randn(2,100)
            self.data_is_new = True
            
            tmr_loop = timer()
            sleep(0.1)
            if self.ui.pushButtonStopAcq.isChecked():
                print('Stopping')
                self.ui.pushButtonStopAcq.setChecked(False)
                break
            # if num == 0:
            #     self.update_plot()
            # Without this, only 1 plot is shown
            # QApplication.processEvents()
            tmr_loop -= timer()
            tmr_loop_list.append(-tmr_loop)
            # print(tmr_loop_list)
        print('{} Iterations Total Time: {:.3f} sec.\nMean {:.3f} +/- {:.3f} sec'.format(len(tmr_loop_list), np.sum(tmr_loop_list), np.mean(tmr_loop_list), np.std(tmr_loop_list)))
        
    def update_plot(self):
        if self.data_is_new:
            if self.data is not None:
                self.plot_count += 1
                if self.plot_ref is None:
                    self.ui.mpl_canvas.axes.cla()
                    plot_ref = self.ui.mpl_canvas.axes.plot(self.data.T)
                else:
                    for entry, new_sp in zip(self.plot_ref, self.data):
                        entry.set_ydata(new_sp)
                self.data_is_new = False
                # print(num)
                self.ui.mpl_canvas.draw()
        

    def stop_acquisition(self):
        print('Stop Button Pressed')

if __name__ == '__main__':
    
    try:
        # Boilerplate
        app = QApplication(sys.argv)
        app.setStyle("Fusion")
        app.setStyleSheet(stylesheet)

        window = MainWindow()
        
        window.show()

        app.exec_()
    except Exception as e:
        print(traceback.format_exc())
    else:
        pass
    finally:
        pass
    