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

from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication
from PyQt5.QtCore import QTimer, Qt, QThreadPool, QRunnable, QObject, Signal, Slot

from PyQt5 import QtCore

from PyQt5.QtGui import QPalette, QColor

QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

from bcars_microscope.ui.ui_learn_multithread import Ui_MainWindow
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

        
        # Setup QTimers here

        # Signals and Slots
        self.ui.pushButtonStartAcq.pressed.connect(self.start_acquisition)
        self.ui.pushButtonStopAcq.pressed.connect(self.stop_acquisition)
        
           
    def start_acquisition(self):
        plot_ref = None

        tmr_loop_list = []
        for num in range(50):
            data = np.random.randn(2,100)
            tmr_loop = timer()
            # sleep(0.005)
            pass
            tmr_loop -= timer()
            tmr_loop_list.append(-tmr_loop)

            if self.ui.pushButtonStopAcq.isChecked():
                print('Stopping')
                break

            # Without this, only 1 plot is shown
            # QApplication.processEvents()

        print('{} Iterations Total Time: {:.6f} sec.\nMean {:.6f} +/- {:.6f} sec'.format(len(tmr_loop_list), np.sum(tmr_loop_list), np.mean(tmr_loop_list), np.std(tmr_loop_list)))
            
            


    def stop_acquisition(self):
        pass

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
    