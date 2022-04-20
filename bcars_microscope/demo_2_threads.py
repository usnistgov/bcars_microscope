import sys
import matplotlib
matplotlib.use('Qt5Agg')

import numpy as np

from PySide2.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication
from PySide2.QtCore import QTimer

from ui.ui_demo_2_threads import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure


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

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar2QT(self.ui.mpl_canvas, self)

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

        self.ui.pushButton_updatePosition.pressed.connect(self.update_position)

        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

        self.timer2 = QTimer()
        self.timer2.setInterval(1000)
        self.timer2.timeout.connect(self.update_position)
        self.timer2.start()

    def update_position(self):
        locs_dict = get_position()
        self.ui.spinBox_x_pos.setValue(locs_dict['X'])
        self.ui.spinBox_y_pos.setValue(locs_dict['Y'])
        self.ui.spinBox_z_pos.setValue(locs_dict['Z'])

    def update_plot(self):
        ydata = get_spectrum()
        if self.ui.plot_ref is None:
            xdata = np.arange(ydata.size)
            # self.ui.mpl_canvas.axes.cla()
            self.ui.plot_ref = self.ui.mpl_canvas.axes.plot(xdata, ydata, lw=1)[0]
            
        else:
            self.ui.plot_ref.set_ydata(ydata)
        # self.ui.mpl_canvas.axes.set_ylim(bottom=ydata.min()-np.std(ydata), top=ydata.max()+np.std(ydata))
        self.ui.mpl_canvas.draw()
        
        # print('Here')
        # print(ydata)

def get_spectrum(n=1600):
    return np.random.randint(0,2**16,size=1600)

def get_position():
    vals = 2*100*np.random.rand(3)
    return {'X':vals[0], 'Y':vals[1], 'Z':vals[2]}

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()