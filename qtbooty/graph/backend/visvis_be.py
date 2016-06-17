#!/usr/bin/env python
# -*- coding: utf-8 -*-;
"""Name of module.

Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
  Examples can be given using either the ``Example`` or ``Examples``
  sections. Sections support any reStructuredText formatting, including
  literal blocks::

      $ python visvis_be.py

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
# @Date:   2014-12-30 14:18:27
# @Last Modified by:   cosgrma
# @Last Modified time: 2015-09-02 06:01:02
# REF: http://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_google.html#example-google
# REF: http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

__author__ = "Mathew Cosgrove"
__copyright__ = ""
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Mathew Cosgrove"
__email__ = "mathew.cosgrove@ngc.com"
__status__ = "Development"

from collections import deque

import numpy as np
from PyQt4 import QtGui

import visvis as vv
backend = 'pyqt4'
vv_app = vv.use(backend)


class VisBaseCanvas(QtGui.QWidget):

  """docstring for VisCanvas"""

  def __init__(self, parent):
    if parent is not None:
      super(VisBaseCanvas, self).__init__()
      # Setup figure to attach to the QtApp
      Figure = vv_app.GetFigureClass()

      self.fig = Figure(parent)
      self.fig.bgcolor = 0.1953, 0.1953, 0.1953

      self.layout = QtGui.QHBoxLayout(parent)
      self.layout.addWidget(self.fig._widget)
      # print self.fig._widget.colorCount(), self.fig._widget.colormap()
      self.setLayout(self.layout)

      # self.setSizePolicy(QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding,
      #                                      QtGui.QSizePolicy.MinimumExpanding))

      self.updateGeometry()

    self.axes = vv.gca()

    self.xlabel = None
    self.ylabel = None
    self.zlabel = None

  def set_xlabel(self, label):
    self.axes.axis.xLabel = label

  def set_ylabel(self, label):
    self.axes.axis.yLabel = label

  def set_yticks(self, ticks):
    self.axes.axis.yTicks = ticks

  def set_zlabel(self, label):
    self.axes.axis.zLabel = label

  def set_lims(self, xlims, ylims, zlims):
    pass

  def set_data(self, data):
    pass

  def update_plot(self):
    pass


class VisSurface(VisBaseCanvas):

  """docstring for VisSurface"""

  def __init__(self, parent):
    super(VisSurface, self).__init__(parent)

    self.x = None
    self.y = None
    self.z = None

    self.xlim = None
    self.ylim = None
    self.zlim = None

    self.surf = None

    self.axes.bgcolor = 0.1953, 0.1953, 0.1953
    self.axes.axis.axisColor = 'w'  # 0.1953, 0.1953, 0.1953  # 'w'
    self.axes.axis.showBox = False
    self.axes.axis.showGrid = True
    self.axes.axis.showGridZ = True
    # print(self.axes.bgcolors)
    # print dir(self.axes), dir(self.axes.axis)
    # print type(self.axes)

  def set_lims(self, xlim, ylim, zlim):
    self.axes.SetLimits(rangeX=xlim,
                        rangeY=ylim,
                        rangeZ=zlim)
    self.clim = zlim
    xptp = xlim[1] - xlim[0]
    yptp = ylim[1] - ylim[0]
    zptp = zlim[1] - zlim[0]

    a_vec = np.array((1.0 / xptp, 1.0 / yptp, 1.0 / zptp))
    max_a_vec = a_vec.max()
    camera_dict = {'zoom': max_a_vec / 2, 'daspect': a_vec / max_a_vec}
    self.axes.camera.SetViewParams(**camera_dict)

  def set_data(self, data):
    self.z = data

  def set_xymesh(self, x, y):
    self.x, self.y = np.meshgrid(x, y)

  def set_boundary(self, x_r, y_r, z_r):
    self.x, self.y = np.meshgrid(x_r, y_r)
    self.axes.SetLimits(rangeX=(np.min(x_r), np.max(x_r)),
                        rangeY=(np.min(y_r), np.max(y_r)),
                        rangeZ=(np.min(z_r), np.max(z_r)))

    self.clim = (np.min(z_r), np.max(z_r))

    a_vec = np.array((1.0 / x_r.ptp(), 1.0 / y_r.ptp(), 1.0 / z_r.ptp()))
    max_a_vec = a_vec.max()
    daspect = a_vec / max_a_vec

    zoom = max_a_vec / 2  # zoom = 1.0/np.sqrt(x_r.ptp()**2 + y_r.ptp()**2 + z_r.ptp()**2)
    camera_dict = {'zoom': zoom, 'daspect': daspect}
    self.axes.camera.SetViewParams(**camera_dict)

  def update_plot(self):
    vv.cla()
    self.surf = vv.surf(self.x, self.y, self.z, axesAdjust=False, axes=self.axes)
    self.surf.clim = self.clim
    self.surf.colormap = vv.CM_JET

from visvis.utils.pypoints import Pointset


class VisPolar(VisBaseCanvas):

  """docstring for VisPolar"""

  def __init__(self, parent):
    super(VisPolar, self).__init__(parent)
    self.lines = dict()
    self.polar = None
    vv.polarplot([0], [0], lc='w', axesAdjust=True)
    self.axes = vv.gca()
    self.params = self.axes.camera.GetViewParams()

    self.axes.axisType = 'polar'
    self.axes.axis.angularRefPos = 0  # 0 deg points up
    self.axes.axis.isCW = True  # changes angular sense (azimuth instead of phi)
    self.axes.axis.showGrid = True
    fig = self.axes.GetFigure()
    # fig.enableUserInteraction = False

  def set_lims(self, rangeTheta, rangeR):
    self.axes.axis.SetLimits(rangeTheta=vv.Range(rangeTheta),
                             rangeR=vv.Range(rangeR))
    # npa = range(rangeR[0], rangeR[1])
    # print npa
    # ticks = [str(e) for e in npa[::-10]]
    # ticks = {k:str(90-k) + "-" for k in range(0, 90, 10)}
    # print ticks
    # self.set_yticks(ticks)

  def add_line(self, name, color):
    self.lines[name] = (deque(maxlen=1000), color)

  def add_point(self, name, point):
    self.lines[name][0].append(point)

  def add_pointset(self, name, pointset):
    self.lines[name][0].extend(pointset)

  def update_plot(self):
    # vv.cla()
    for k in self.lines.keys():
      data = np.array(self.lines[k][0])
      vv.polarplot(data[:, 0], data[:, 1], lc=self.lines[k][1], axesAdjust=False, axes=self.axes)
    # print self.axes.camera.GetViewParams()
    # print self.axes.camera.GetViewParams()
      # 'elevation': 90.0,
      # 'azimuth': 0.0,
    # params = {'loc': (-0.81907558441162, 0.7204818725585938, 0.10000000149011613),
    #           'daspect': (1.0, 1.0, 1.0),
    #           'zoom': 0.010112156249263062}
    # self.axes.camera.SetViewParams(**params)
    # self.axes.axisType = 'polar'
    # print self.axes.camera.GetViewParams()


def get_mags(sv, angs):
  # Define magnitude
  angsRads = np.pi * angs / 180.0
  mags = 10 * np.log10(np.abs(np.sin(10 * angsRads) / angsRads)) + angsRads
  mags = mags - np.max(mags)
  return mags


colorset = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']


def polar_test2():
  vpolar = VisPolar(None)
  vpolar.set_lims(0, (90, 0))
  vpolar.set_xlabel('degrees')
  vpolar.set_ylabel('dB')

  svset = range(0, 8)
  angs = 0.1 + np.linspace(-90, 90, 181)  # 0.1+ get rid of singularity

  for sv in svset:
    vpolar.add_line(sv, colorset[sv])
    vpolar.add_pointset(sv, zip(angs + sv * 20, get_mags(sv, angs)))
  vpolar.update_plot()


if __name__ == '__main__':
  polar_test2()

  app = vv.use()

  app.Run()
