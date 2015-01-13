#!/usr/bin/env python
# -*- coding: utf-8 -*-;
"""Name of module.

Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
  Examples can be given using either the ``Example`` or ``Examples``
  sections. Sections support any reStructuredText formatting, including
  literal blocks::

      $ python mpl_canvas.py

Section breaks are created by simply resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
  module_level_variable (int): Module level variables may be documented in
    either the ``Attributes`` section of the module docstring, or in an
    inline docstring immediately following the variable.

    Either form is acceptable, but the two should not be mixed. Choose
    one convention to document module level variables and be consistent
    with it.

.. _Google Python Style Guide:
   http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

"""
# @Author: Mathew Cosgrove
# @Date:   2014-12-30 14:14:36
# @Last Modified by:   mac
# @Last Modified time: 2014-12-30 21:30:18
# REF: http://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_google.html#example-google
# REF: http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

__author__ = "Mathew Cosgrove"
__copyright__ = ""
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Mathew Cosgrove"
__email__ = "mathew.cosgrove@ngc.com"
__status__ = "Development"

import numpy as np

from PyQt4 import QtGui, QtCore

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


class MplCanvas(FigureCanvas):
  """
  Initializes the object. The init function takes in a QtWidget as
  a parent. This is required to add the widget to a Qt application.
  """
  def __init__(self, parent, plot_type, name=None, width=10, height=10, dpi=10, rows=None, cols=None):
    # Initialize the Figure Canvas
    self.fig = Figure()
    FigureCanvas.__init__(self, self.fig)
    self.setParent(QtGui.QWidget(parent))

    self.plot_type = plot_type

    if name is not None:
      self.fig.suptitle(name)

    if plot_type == "polar":
      self.polar = None
      self.configure_polar_axes()

    elif plot_type == "surface":
      self.surf = None
      self.configure_surf_axes()

  def configure_surf_axes(self):
    self.axes = self.fig.add_subplot(111, projection='3d')
    self.axes.hold(False)
    self.axes.grid(True)

  def configure_polar_axes(self):
    self.axes = self.fig.add_subplot(111, projection='polar')
    self.axes.hold(False)
    self.axes.grid(True)
    xtick_delta = 30
    self.axes.set_xticks(np.radians(np.arange(0, 360, xtick_delta)))
    ytick_delta = (np.pi/2)/2
    yticks = np.degrees(np.arange(0, np.pi/2 + ytick_delta, ytick_delta)).astype(int)
    self.axes.set_yticks(yticks)
    self.axes.set_yticklabels(np.core.defchararray.add(yticks[::-1].astype(str), np.array(['$^\circ$']*len(yticks))))
    self.axes.set_rmax(90.0)

  def update_plot(self):
    if self.plot_type == "polar":
      self.update_polar_plot()
    elif self.plot_type == "surface":
      self.update_surface_plot()
    self.fig.canvas.draw()

  def update_polar_plot(self):
    self.axes.plot(az, el, marker='D', fillstyle='full', color='r', ls='', markersize=20)
    for i, txt in enumerate(svs):
      self.axes.annotate(txt, (az[i], el[i]), size=12, ha='center', va='center')

  def update_surface_plot(self):
    # self.axes.clear()
    if self.surf is not None:
      self.surf.remove()
    # self.axes.plot_wireframe(self.x, self.y, self.z, rstride=1, cstride=1)
    self.surf = self.axes.plot_surface(self.x, self.y, self.z,
                                       rstride=1, cstride=1,
                                       cmap=cm.coolwarm,
                                       linewidth=0,
                                       antialiased=False)

  def set_xymesh(self, x, y):
    self.x, self.y = np.meshgrid(x, y)

  def set_zdata(self, data):
    self.z = data

  def set_lims(self, xlim, ylim, zlim):
    pass

  def set_xticks(self, xticks):
    pass

  def set_xrange(self, xrange):
    pass

  def set_xlim(self, xlim):
    pass

  def set_xlabel(self, xlabel):
    pass

  def set_yticks(self, yticks):
    pass

  def set_yrange(self, yrange):
    pass

  def set_ylim(self, ylim):
    pass

  def set_ylabel(self, ylabel):
    pass

  def set_zticks(self, zticks):
    pass

  def set_zrange(self, zrange):
    pass

  def set_zlim(self, zlim):
    pass

  def set_zlabel(self, zlabel):
    pass

# class MplCanvas(FigureCanvas):
#   """
#   Initializes the object. The init function takes in a QtWidget as
#   a parent. This is required to add the widget to a Qt application.
#   """
#   def __init__(self, parent=None, name=None, width=10, height=10, dpi=10, rows=None, cols=None):
#     # Initialize the Figure Canvas
#     self.fig = Figure()
#     FigureCanvas.__init__(self, self.fig)

#     # Create a Figure
#     self.x_label = None
#     self.x_r = None
#     self.x = None

#     self.y = None
#     self.ylabel = None
#     self.y_r = None
#     self.ylim = None

#     self.z = None
#     self.z_r = None

#     self.surf = None

#     self.setParent(QtGui.QWidget(parent))
#     if name is not None:
#       self.fig.suptitle(name)

    # # Sets the Horizontal and Vertical size policy to enable expanding
    # size_policy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
    # FigureCanvas.setSizePolicy(self, size_policy)
    # # Updates the geometry to reflect the changes
    # FigureCanvas.updateGeometry(self)


    # self.axes = self.fig.gca(projection='3d')

    # self.fig.patch.set_visible(True)

  # def set_x_r(self, x_r):
  #   self.x_r = x_r

  # def set_y_r(self, y_r):
  #   self.y_r = y_r

  # def set_boundary(self, x_r, y_r):
  #   self.x, self.y = np.meshgrid(x_r, y_r)
