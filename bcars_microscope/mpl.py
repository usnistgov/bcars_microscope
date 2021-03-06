from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

class MplCanvas(FigureCanvasQTAgg):
    """ Matplotlib Canvas """
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        self.cbar = None
        super(MplCanvas, self).__init__(self.fig)