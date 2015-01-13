
import pyqtgraph
from pyqtgraph.Qt import QtCore, QtGui

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import cm

class SuftPlotWidget(QtGui.QWidget):

              rows = data[0]
            cols = data[1]

        elif self.plot_type == PlotType.surf:
            self.axes = self.fig.add_subplot(111, projection='3d')
        if self.plot_type == PlotType.surf:
            self.axes.set_xlabel(self.xlabel)
            self.axes.set_ylabel(self.ylabel)
            x = np.linspace(kwargs['header'][3], kwargs['header'][3] + kwargs['header'][4]*kwargs['header'][5],kwargs['header'][5])
            y = np.linspace(kwargs['header'][6], kwargs['header'][6] + kwargs['header'][7]*kwargs['header'][8],kwargs['header'][8])
            self.x, self.y = np.meshgrid(x, y)
class PolarPlotWidget(QtGui.QWidget):
          if self.plot_type == PlotType.polar:
            self.axes = self.fig.add_subplot(111, projection='polar')

class ScatterPlotWidget(QtGui.QWidget):

        elif self.plot_type == PlotType.scatter:
            self.axes = self.fig.add_subplot(111, projection='3d')

            self.axes.set_xlabel(self.xlabel)
            self.axes.set_ylabel(self.ylabel)
            myx = np.linspace(kwargs['header'][3], kwargs['header'][3] + kwargs['header'][4]*kwargs['header'][5],kwargs['header'][5])
            myy = np.linspace(kwargs['header'][6], kwargs['header'][6] + kwargs['header'][7]*kwargs['header'][8],kwargs['header'][8])
            self.x, self.y = np.meshgrid(myx, myy)

class HistogramtWidget(QtGui.QWidget):

        elif self.plot_type == PlotType.hist:
            count, bins, ignored = self.axes.hist(data.astype('float'), 64, normed=True)
            self.axes.hold(True)
            kde = sm.nonparametric.KDEUnivariate(data.astype('float'))
            kde.fit()
            self.axes.plot(kde.support, kde.density, lw=2, color='red')
            self.axes.hold(False)
        elif self.plot_type == PlotType.hist_norm:
            count, bins, ignored = self.axes.hist(data.astype('float'), 200, normed=True)
            self.axes.plot(bins[:-1], count/sum(count))
            self.axes.hold(True)
            kde = sm.nonparametric.KDEUnivariate(data.astype('float'))
            kde.fit()
            self.axes.plot(kde.support, kde.density, lw=2, color='black')
            self.axes.hold(False)


if self.plot_type == PlotType.bar:
            width = 0.35
            self.axes.bar(range(len(data[0])), data[1], width, color='#1C41D8')
            if self.ylim is not None:
                self.axes.set_ylim(self.ylim[0],self.ylim[1])

            if self.ylabel is not None:
                self.axes.set_ylabel(self.ylabel)

            if self.xlabel is not None:
                self.axes.set_xlabel(self.xlabel)

            self.axes.set_xticks(np.arange(len(data[0])) + width/2)
            self.axes.set_xticklabels(data[0])#, rotation=90)
            self.axes.grid('on')

            self.axes.margins(.1)

class PrivateMplCanvas(FigureCanvas):
    def __init__(self, parent=None, name=None, width=10, height=10, dpi=10, rows=None, cols=None):
        """Initializes the object. The init function takes in a QtWidget as
        a parent. This is required to add the widget to a Qt application.
        """
        # Create a Figure
        #self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.fig = Figure()
        if name is not None:
            self.fig.suptitle(name)

        self.xlabel = None
        self.ylabel = None
        self.ylim = None

        # Initialize the Figure Canvas
        FigureCanvas.__init__(self, self.fig)
        # Sets the Horizontal and Vertical size policy to enable expanding
        size_policy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        FigureCanvas.setSizePolicy(self, size_policy)
        # Updates the geometry to reflect the changes
        FigureCanvas.updateGeometry(self)
        self.setParent(QtGui.QWidget(parent))

        self.axes = self.fig.add_subplot(111)
        self.axes.hold(False)

        self.fig.patch.set_visible(True)

    def set_ylim(self, ylim):
        self.ylim = ylim

    def set_xlim(self, xlim):
        self.xlim = xlim

    def set_xlabel(self, label):
        self.xlabel = label

    def set_ylabel(self, label):
        self.ylabel = label

    def create(self, data=None, **kwargs):
        if data is None:
            return
        else:

    def update_plot(self, data, **kwargs):


        elif self.plot_type == PlotType.polar:
            svs = [1, 2, 3, 4]
            az = np.radians([10, 45, 90, 135])
            el = 90 - np.array([45/4, 45/3, 45/2, 45])
            self.axes.plot(az, el, marker='D', fillstyle='full', color='r', ls='', markersize=20)
            xtick_delta = 30
            self.axes.set_xticks(np.radians(np.arange(0, 360, xtick_delta)))
            ytick_delta = (np.pi/2)/2
            yticks = np.degrees(np.arange(0, np.pi/2 + ytick_delta, ytick_delta)).astype(int)
            self.axes.set_yticks(yticks)
            self.axes.set_yticklabels(np.core.defchararray.add(yticks[::-1].astype(str),\
                                      np.array(['$^\circ$']*len(yticks))))
            self.axes.set_rmax(90.0)
            self.axes.grid(True)

            for i, txt in enumerate(svs):
                self.axes.annotate(txt, (az[i],el[i]), size=12, ha='center', va='center',)

            #self.set_title("A line plot on a polar axis", va='top')
        elif self.plot_type == PlotType.surf:
            self.surf = self.axes.plot_surface(self.x, self.y, data, rstride=1, cstride=1, cmap=cm.coolwarm,\
                                               linewidth=0, antialiased=False)

        elif self.plot_type == PlotType.scatter:
            self.axes.scatter(self.x, self.y, data)
        self.fig.canvas.draw()
