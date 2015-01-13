#!/usr/bin/env python
# -*- coding: utf-8 -*-;
"""Name of module.

Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
  Examples can be given using either the ``Example`` or ``Examples``
  sections. Sections support any reStructuredText formatting, including
  literal blocks::

      $ python polar.py

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
# @Date:   2014-12-30 13:47:49
# @Last Modified by:   mac
# @Last Modified time: 2014-12-30 19:23:36
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
from QtBooty.graphs import MplCanvas, VisPolar, GraphUpdater

front_end = 'visvis'
# front_end = 'matplotlib'

class Polar(GraphUpdater):
  def __init__(self, name=None, controller=False, interval=1000, maxlen=100):
    super(Polar, self).__init__(interval=interval, maxlen=maxlen)
    if front_end == "visvis":
      self.graph = VisPolar(self)
    else:
      self.graph = MplCanvas(self)
    self.layout.addWidget(self.graph)

  def add_line(self, name, color):
    self.graph.add_line(name, color)

  def add_point(self, name, point):
    self.graph.add_point(name, point)

  def set_lims(self, theta, range):
    self.graph.set_lims(theta, range)

  def _update(self):
    self.graph.update_plot()

# if __name__ == '__main__':
#   # Create the App
#   import sys
#   app = QtGui.QApplication(sys.argv)

#   polar = Polar()
#   polar.set_lims(0,)
#   svs = [1, 2, 3, 4]
#   az = np.radians([10, 45, 90, 135])
#   el = 90 - np.array([45/4, 45/3, 45/2, 45])

#   vpolar.set_xlabel('degrees')
#   vpolar.set_ylabel('dB')

#   sys.exit(app.exec_())

#   vpolar = VisPolar(None)
#   vpolar.set_lims(0, vv.Range(-40, 5))
#   vpolar.set_xlabel('degrees')
#   vpolar.set_ylabel('dB')

#   svset = range(0, 1)
#   angs = 0.1 + np.linspace(-90, 90, 181)  # 0.1+ get rid of singularity

#   for sv in svset:
#     vpolar.add_line(sv, colorset[sv])
#     vpolar.add_pointset(sv, zip(angs + sv*20, get_mags(sv, angs)))
#   vpolar.update_plot()




# class Polar(QtGui.QWidget):
#   def __init__(self, name=None, controller=False, interval=1000, maxlen=10):
#     super(Polar, self).__init__()

#     self.maxlen = maxlen
#     self.interval = interval
#     self.layout = QtGui.QHBoxLayout()

#     self.lines = dict()

#     if front_end == "visvis":
#       self.graph = VisCanvas(self)
#     else:
#       self.graph = MplCanvas(self)

#     self.layout.addWidget(self.graph)

#     size_policy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
#     self.setSizePolicy(size_policy)

#     self.setLayout(self.layout)
#     self.update_timer = QtCore.QTimer()
#     self.update_timer.timeout.connect(self._update)
#     self.update_timer.setInterval(interval)

#     self.data_set = deque(maxlen=self.maxlen)

#   def add_line(self, name, color=None):


#   def add_data(self, name, data):
#     self.data_set.append(data)

#   def start(self):
#     self.update_timer.start()

#   def set_interval(self, interval):
#     self.update_timer.setInterval(interval)

#   def _update(self):
#     self.graph.update_plot()

# class MplCanvas(FigureCanvas):
#   """
#   Initializes the object. The init function takes in a QtWidget as
#   a parent. This is required to add the widget to a Qt application.
#   """
#   def __init__(self, parent=None, name=None, width=10, height=10, dpi=10, rows=None, cols=None):
#     # Initialize the Figure Canvas
#     self.fig = Figure()
#     FigureCanvas.__init__(self, self.fig)
#     self.setParent(QtGui.QWidget(parent))
#     if name is not None:
#       self.fig.suptitle(name)

#     self.configure_polar_axes()

#   def configure_polar_axes(self):
#     self.axes = self.fig.add_subplot(111, projection='polar')
#     self.axes.hold(False)
#     self.axes.grid(True)
#     xtick_delta = 30
#     self.axes.set_xticks(np.radians(np.arange(0, 360, xtick_delta)))
#     ytick_delta = (np.pi/2)/2
#     yticks = np.degrees(np.arange(0, np.pi/2 + ytick_delta, ytick_delta)).astype(int)
#     self.axes.set_yticks(yticks)
#     self.axes.set_yticklabels(np.core.defchararray.add(yticks[::-1].astype(str), np.array(['$^\circ$']*len(yticks))))
#     self.axes.set_rmax(90.0)

#   def update_plot(self):
#     self.axes.plot(az, el, marker='D', fillstyle='full', color='r', ls='', markersize=20)
#     for i, txt in enumerate(svs):
#       self.axes.annotate(txt, (az[i], el[i]), size=12, ha='center', va='center')
#     self.fig.canvas.draw()


# class VisCanvas(QtGui.QWidget):
#   """docstring for VisCanvas"""
#   def __init__(self, parent):
#     super(VisCanvas, self).__init__()

#   def update_plot(self):
#     vv.cla()