from multiprocessing.sharedctypes import Value
import sys
import traceback

import matplotlib as mpl
mpl.use('Qt5Agg')
mpl.rcParams['font.size'] = 20
mpl.rcParams['axes.labelsize'] = 20

import numpy as np

from PySide2.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication
from PySide2.QtCore import QTimer, Qt
from PySide2 import QtCore
from PySide2.QtGui import QPalette, QColor

QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

from ui.ui_demo_2_threads import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure

from andor_ccd import AndorNewton970, andor_err_code_str
from pyAndorSDK2 import atmcd_errors, atmcd_codes
err_codes = atmcd_errors.Error_Codes

from pipython import GCS2Commands, GCSDevice, pitools

dark_palette = QPalette()
dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
dark_palette.setColor(QPalette.WindowText, Qt.white)
dark_palette.setColor(QPalette.Base, QColor(35, 35, 35))
dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
dark_palette.setColor(QPalette.ToolTipBase, QColor(25, 25, 25))
dark_palette.setColor(QPalette.ToolTipText, Qt.white)
dark_palette.setColor(QPalette.Text, Qt.white)
dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
dark_palette.setColor(QPalette.ButtonText, Qt.white)
dark_palette.setColor(QPalette.BrightText, Qt.red)
dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
dark_palette.setColor(QPalette.HighlightedText, QColor(35, 35, 35))
dark_palette.setColor(QPalette.Active, QPalette.Button, QColor(53, 53, 53))
dark_palette.setColor(QPalette.Disabled, QPalette.ButtonText, Qt.darkGray)
dark_palette.setColor(QPalette.Disabled, QPalette.WindowText, Qt.darkGray)
dark_palette.setColor(QPalette.Disabled, QPalette.Text, Qt.darkGray)
dark_palette.setColor(QPalette.Disabled, QPalette.Light, QColor(53, 53, 53))

# Stylesheet overwrites palette for button
stylesheet = "QPushButton {background-color: (53,53,53), border-style: inset; border-width: 2px; border-radius: 3px;}"

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
        toolbar.setStyleSheet('font: 20pt "Arial";')  # Work around to setting the nav toolbar coordinate font size

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
        self.ui.pushButton_setPos_getCurrent.pressed.connect(self.update_position)
        self.ui.pushButton_moveX.pressed.connect(self.inner_move_stage)
        self.ui.pushButton_moveY.pressed.connect(self.inner_move_stage)
        self.ui.pushButton_moveZ.pressed.connect(self.inner_move_stage)
        self.ui.pushButton_moveAll.pressed.connect(self.inner_move_stage)
        self.ui.pushButton_moveCenter.pressed.connect(self.inner_move_stage)
        self.ui.pushButton_moveCenter_Offset.pressed.connect(self.inner_move_stage)

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
        if self.sender() == self.ui.pushButton_setPos_getCurrent:
            self.ui.spinBox_x_setpos.setValue(locs_dict['X'])
            self.ui.spinBox_y_setpos.setValue(locs_dict['Y'])
            self.ui.spinBox_z_setpos.setValue(locs_dict['Z'])
        else: # Not from the set from current-position load button
            self.ui.spinBox_x_pos.setValue(locs_dict['X'])
            self.ui.spinBox_y_pos.setValue(locs_dict['Y'])
            self.ui.spinBox_z_pos.setValue(locs_dict['Z'])


    def update_plot(self):
        xdata, ydata = get_spectrum()
        if ydata is not None:
            if self.ui.plot_ref is None:
                self.ui.plot_ref = self.ui.mpl_canvas.axes.plot(xdata, ydata, lw=1)[0]
                
            else:
                self.ui.plot_ref.set_ydata(xdata)
                self.ui.plot_ref.set_ydata(ydata)
            # self.ui.mpl_canvas.axes.set_ylim(bottom=ydata.min()-np.std(ydata), top=ydata.max()+np.std(ydata))
            self.ui.mpl_canvas.draw()
        
        # print('Here')
        # print(ydata)

    def inner_move_stage(self):
        self.timer2.stop()
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
        self.timer2.start()

# def get_position():
#     vals = 2*100*np.random.rand(3)
#     return {'X':vals[0], 'Y':vals[1], 'Z':vals[2]}

if __name__ == '__main__':
    test_mode = True

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
        app.setStyleSheet(stylesheet)
        app.setStyle("Fusion")
        app.setPalette(dark_palette)
        window = MainWindow()
        window.show()
        app.exec_()
        
    if not test_mode:
        try:
            ccd = AndorNewton970(settings_kwargs=AndorNewton970.default_fvb)
            ccd.initialize_default()
            ccd.sdk.PrepareAcquisition()
            if ccd.is_fvb_or_sgl_track == True:
                    sgl_image_size = ccd.n_cols
            else:
                sgl_image_size = ccd.n_rows * ccd.n_cols

            def get_spectrum(n=1600):
                ret_code, first_img, last_img = ccd.sdk.GetNumberNewImages()
                # print('New Images: {}:{}'.format(first_img, last_img))
                
                n_images = last_img-first_img + 1
                allImageSize = sgl_image_size * n_images

                if n_images > 0:
                    (ret_code, arr, validfirst, validlast) = ccd.sdk.GetImages16(last_img, last_img, sgl_image_size)
                    # print(arr[0])
                    return np.arange(n), arr
                else:
                    return None

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

        except Exception as e:
            print('ERROR: {}'.format(traceback.format_exc()))
            ret_code = ccd.sdk.ShutDown()
            print("Function Shutdown returned {}: {}".format(ret_code, err_codes(ret_code).name))
        else:
            ret_code = ccd.sdk.StartAcquisition()
            print('Starting Acquisition: {} -- {}'.format(ret_code, andor_err_code_str(ret_code)))
            

            app = QApplication(sys.argv)
            app.setStyleSheet(stylesheet)
            app.setStyle("Fusion")
            app.setPalette(dark_palette)
            window = MainWindow()
            window.show()
            app.exec_()
            ccd.sdk.AbortAcquisition()
            ret_code = ccd.sdk.ShutDown()
            print("Function Shutdown returned {}: {}".format(ret_code, err_codes(ret_code).name))
            pidevice.CloseConnection()