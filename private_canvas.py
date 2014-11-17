
from pdb import set_trace as _breakpoint

import numpy as np
from scipy import stats

import statsmodels.api as sm
from statsmodels.distributions.mixture_rvs import mixture_rvs

import pyqtgraph
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import PyQt4.Qwt5 as Qwt
from guiqwt.image import ImagePlot, ImageItem
from guiqwt.builder import make


class PlotType:
    timeseries  = 1
    polar       = 2
    scatter     = 3
    mesh        = 4
    grid        = 5
    bar         = 6
    surf        = 7
    image       = 8
    hist        = 9
    hist_norm   = 10
    heat        = 11
    image       = 12
    fastbar     = 13



class PrivateGuiQwtCanvas():
    def __init__(self, name=None):
        if name is not None:
            self.plot_widget = ImagePlot()

    def create(self, data=None):
        if data is not None:
            self.rows = data[0]
            self.cols = data[1]
            self.doppler_min = data[2][0]
            self.doppler_max = data[2][1]
            self.codephase_min = data[3][0]
            self.codephase_max = data[3][1]
            self.prn = data[4]
        else:
            self.rows = 1706
            self.cols = 31
            self.doppler_min = -5000
            self.doppler_max = 5000
            self.codephase_min = 0
            self.codephase_max = 1023

        self.image = make.image(data[5],
                                xdata=[self.codephase_min, self.codephase_max],
                                ydata=[self.doppler_min, self.doppler_max],
                                colormap='jet', interpolation='nearest')
        self.plot_widget.add_item(self.image)
        self.plot_widget.set_aspect_ratio(ratio=.75)
        self.plot_widget.set_axis_title(0, 'Doppler')
        self.plot_widget.set_axis_unit(0, 'Hertz')
        self.plot_widget.set_axis_title(2, 'Code Phase')
        self.plot_widget.set_axis_unit(2, 'Chips')
        self.plot_widget.set_axis_title(1, 'Correlation')
        self.plot_widget.set_axis_unit(1, 'Power I^2 + Q^2')
        self.plot_widget.set_title(("Correlation for PRN: %d") % (self.prn))
        self.plot_widget.show()

    def update_plot(self, data):
        self.plot_widget.del_item(self.image)
        self.image = make.image(data,
                                xdata=[self.codephase_min, self.codephase_max],
                                ydata=[self.doppler_min, self.doppler_max],
                                colormap='jet', interpolation='nearest')
        #self.image.set_data(data)
        self.plot_widget.add_item(self.image)
        self.plot_widget.set_plot_limits(self.codephase_min, self.codephase_max, self.doppler_min, self.doppler_max)
        self.plot_widget.show()

    def get_plot_widget(self):
        return self.plot_widget


class PrivatePyQtOpenGl():
    def __init__(self, name=None):
        self.plot_widget = gl.GLViewWidget()
        if name is not None:
            self.plot_widget.setWindowTitle(name)
        self.plot_widget.setCameraPosition(distance=300, elevation=20, azimuth=45)
        ## create three grids, add each to the view
        xgrid = gl.GLGridItem()
        ygrid = gl.GLGridItem()
        zgrid = gl.GLGridItem()
        self.scale = 100
        ## rotate x and y grids to face the correct direction
        xgrid.rotate(90, 0, 1, 0)
        ygrid.rotate(90, 1, 0, 0)
        xgrid.translate(0,          self.scale, self.scale)
        ygrid.translate(self.scale, 0,          self.scale)
        zgrid.translate(self.scale, self.scale, 0)
        xgrid.scale(self.scale/10, self.scale/10, 1)
        ygrid.scale(self.scale/10, self.scale/10, 1)
        zgrid.scale(self.scale/10, self.scale/10, 1)
        self.plot_widget.addItem(xgrid)
        self.plot_widget.addItem(ygrid)
        self.plot_widget.addItem(zgrid)

    def create(self, data=None, scale_factor=None, **kwargs):
        if data is not None:
            self.rows = data[0]
            self.cols = data[1]
        else:
            self.rows = 1
            self.cols = 1
        if scale_factor is not None:
            self.scale_factor = scale_factor
        else:
            self.scale_factor = 2
        self.surf_plot = gl.GLSurfacePlotItem(shader='normalColor', computeNormals=True, smooth=True)
        self.surf_plot.scale(self.scale/float(self.rows), self.scale/float(self.cols),  1)
        self.plot_widget.addItem(self.surf_plot)

    def update_plot(self, data):
        #self.scale_data(data)
        self.surf_plot.setData(z=data)
        self.plot_widget.show()

    def scale_data(self, data):
        data /= (np.mean(data.reshape(self.rows*self.cols,1))*2)
        #data *= 5

    def get_plot_widget(self):
        return self.plot_widget

class PrivatePyQtGraph():
    def __init__(self, name=None, legend=None):
        pyqtgraph.setConfigOption('background', 'w')
        pyqtgraph.setConfigOption('foreground', 'k')
        self.plot_widget = pyqtgraph.PlotWidget(name=name)
        self.plot_widget.showGrid(x=True, y=True)
        if legend:
            self.plot_widget.addLegend()
        self.plot_widget.setLabel("bottom", text="Time (s)")

    def get_plot_widget(self):
        return self.plot_widget

    def destroy(self):
        pass

    def create_artist(self, color, downsample=None):
        return self.plot_widget.plot(pen=color, downsample=downsample, antialias=True)

    def update_artist(self, artist, data):
        artist.setData(data[0], data[1])

    def remove_artist(self, artist):
        artist.clear()

    def init_legend(self):
        self.plot_widget.getPlotItem().legend.items = []

    def update_legend(self, artist, label):
        self.plot_widget.getPlotItem().legend.addItem(artist, label)

    def add_item(self, item):
        self.plot_widget.addItem(item)

    def remove_item(self, item):
        self.plot_widget.removeItem(item)

class PrivatePyQtImage():

    def __init__(self, name=None, legend=None):
        self.win = pyqtgraph.GraphicsLayoutWidget()
        self.img = pyqtgraph.ImageItem(border='w')
        self.view = self.win.addViewBox()

    def get_plot_widget(self):
        return self.win

    def create(self, data, **kwargs):
        self.view.addItem(self.img)

    def update_plot(self, data):
        self.img.setImage(data)

    def init_legend(self):
        pass

    def update_legend(self, artist, label):
        pass

    def add_item(self, item):
        pass

    def remove_item(self, item):
        self.img.removeItem(item)

class PrivatePlotCanvas(object):
    def __init__(self, plot_type, name=None, legend=None, parent=None, rows=None, cols=None):
        if plot_type == PlotType.timeseries:
            self.figure = PrivatePyQtGraph(name=name, legend=legend)
        elif plot_type == PlotType.bar:
            self.figure = PrivateMplCanvas(parent=parent, name=name, plot_type=plot_type)
        elif plot_type == PlotType.hist:
            self.figure = PrivateMplCanvas(parent=parent, name=name, plot_type=plot_type)
        elif plot_type == PlotType.hist_norm:
            self.figure = PrivateMplCanvas(parent=parent, name=name, plot_type=plot_type)
        elif plot_type == PlotType.polar:
            self.figure = PrivateMplCanvas(parent=parent, name=name, plot_type=plot_type)
        elif plot_type == PlotType.mesh:
            self.figure = PrivatePyQtOpenGl(name=name)
        elif plot_type == PlotType.surf:
            self.figure = PrivateMplCanvas(parent=parent, name=name, plot_type=plot_type, rows=rows, cols=cols)
        elif plot_type == PlotType.image:
            self.figure = PrivateGuiQwtCanvas(name=name)
        elif plot_type == PlotType.heat:
            self.figure = PrivatePyQtImage(name=name, legend=legend)
        elif plot_type == PlotType.scatter:
            self.figure = PrivateMplCanvas(parent=parent, name=name, plot_type=plot_type, rows=rows, cols=cols)
        elif plot_type == PlotType.fastbar:
            self.figure = PrivatePyQtGraph(name=name, legend=legend)

    def get_widget(self):
        return self.figure.get_plot_widget()

    def destroy(self):
        pass

    def create(self, data=None, scale_factor=None, **kwargs):
        return self.figure.create(data=data, scale_factor=scale_factor, **kwargs)

    def create_artist(self, color, downsample=None):
        return self.figure.create_artist(color, downsample=downsample)
#         if downsample is not None:
#             return self.figure.create_artist(color, data=data, downsample=downsample)
#         else:
#             return self.figure.create_artist(color)

#         if data is not None:
#             return self.figure.create_artist(color, data)
#         else:
#             return self.figure.create_artist(color)

    def update_artist(self, artist, data):
        self.figure.update_artist(artist, data)

    def remove_artist(self, artist):
        self.figure.remove_artist(artist)

    def init_legend(self):
        self.figure.init_legend()

    def update_legend(self, artist, label):
        self.figure.update_legend(artist, label)

    def add_item(self, item):
        self.figure.add_item(item)

    def remove_item(self, item):
        self.figure.remove_item(item)

    def update(self, data, **kwargs):
        self.figure.update_plot(data)

    def set_ylim(self, ylim):
        self.figure.set_ylim(ylim)

    def set_xlim(self, xlim):
        self.figure.set_xlim(xlim)

    def set_xlabel(self, label):
        self.figure.set_xlabel(label)

    def set_ylabel(self, label):
        self.figure.set_ylabel(label)

