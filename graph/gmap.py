#!/usr/bin/env python
# -*- coding: utf-8 -*-;
"""Name of module.

Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
  Examples can be given using either the ``Example`` or ``Examples``
  sections. Sections support any reStructuredText formatting, including
  literal blocks::

      $ python gmap.py

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
# @Date:   2015-09-04 03:23:23
# @Last Modified by:   cosgrma
# @Last Modified time: 2015-10-28 08:13:07
# REF: http://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_google.html#example-google
# REF: http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

__author__ = "Mathew Cosgrove"
__copyright__ = ""
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Mathew Cosgrove"
__email__ = "cosgroma@gmail.com"
__status__ = "Development"

import os
import socket
import getpass
import keyring
from PyQt4 import QtCore, QtGui, QtWebKit, QtNetwork

import logging


class GMap(QtGui.QWidget):

  """docstring for Map"""

  def __init__(self):

    super(GMap, self).__init__()

    self.logger = logging.getLogger(__name__)

    if 'northgrum' in socket.getfqdn().split('.'):
      if keyring.get_password("system", getpass.getuser()) is None:
        keyring.set_password("system", getpass.getuser(), getpass.getpass())

      proxy = QtNetwork.QNetworkProxy(QtNetwork.QNetworkProxy.HttpProxy, "centralproxy.northgrum.com", 80)
      proxy.setUser(getpass.getuser())
      self.logger.info('using proxy to access the internet => user: %s, proxy: %s' % (getpass.getuser(), "centralproxy.northgrum.com"))
      proxy.setPassword(keyring.get_password("system", getpass.getuser()))
      QtNetwork.QNetworkProxy.setApplicationProxy(proxy)

    self.splitter = QtGui.QSplitter(self)
    self.splitter.setOrientation(QtCore.Qt.Vertical)

    self.web = QtWebKit.QWebView(self)
    path, file = os.path.split(os.path.realpath(__file__))
    # self.web.load(QtCore.QUrl.fromLocalFile(QtCore.QFileInfo("gmaps.html").absoluteFilePath()))
    self.web.load(QtCore.QUrl.fromLocalFile(os.path.join(path, "gmaps.html")))
    self.layout = QtGui.QVBoxLayout(self)
    # self.layout.addWidget(self.web)
    # self.web.page().mainFrame().setScrollBarPolicy(QtCore.Qt.Vertical, QtCore.Qt.ScrollBarAlwaysOff)
    self.web.page().settings().setAttribute(QtWebKit.QWebSettings.DeveloperExtrasEnabled, True)
    self.webInspector = QtWebKit.QWebInspector(self)
    self.webInspector.setPage(self.web.page())

    # layout = QtGui.QVBoxLayout(self)
    # layout.setMargin(0)
    self.layout.addWidget(self.splitter)

    self.splitter.addWidget(self.web)
    self.splitter.addWidget(self.webInspector)

    shortcut = QtGui.QShortcut(self)
    shortcut.setKey(QtCore.Qt.Key_F12)
    shortcut.activated.connect(self.toggleInspector)
    self.webInspector.setVisible(False)

  def toggleInspector(self):
    self.webInspector.setVisible(not self.webInspector.isVisible())
    # self.web.page().mainFrame().addToJavaScriptWindowObject('self', self)

  def add_marker(self, lat, lon):
    self.web.page().currentFrame().evaluateJavaScript(
        QtCore.QString(
            "addMarker(" + ','.join(str(e) for e in [lat, lon]) + ")"
        )
    )

  def add_path(self, lat, lon):
    self.web.page().currentFrame().evaluateJavaScript(
        QtCore.QString(
            "addPath(" + ','.join(str(e) for e in [lat, lon]) + ")"
        )
    )

  def add_circle(self, lat, lon, radius):
    self.web.page().currentFrame().evaluateJavaScript(
        QtCore.QString(
            "addErrorCircle(" + ','.join(str(e) for e in [lat, lon, radius]) + ")"
        )
    )


if __name__ == '__main__':
  import random
  import logging
  import pyutils
  import getpass
  import keyring

  def update():
    map.add_circle(34.17192, -118.59521, random.random() * 100)

  if keyring.get_password("system", getpass.getuser()) is None:
    keyring.set_password("system", getpass.getuser(), getpass.getpass())
  proxy = QtNetwork.QNetworkProxy(QtNetwork.QNetworkProxy.HttpProxy, "centralproxy.northgrum.com", 80)
  proxy.setUser(getpass.getuser())
  proxy.setPassword(keyring.get_password("system", getpass.getuser()))
  QtNetwork.QNetworkProxy.setApplicationProxy(proxy)

  pyutils.setup_logging()
  logger = logging.getLogger()

  from QtBooty import App
  app = App('config/bad_app_config.json')
  # app.main.menus["File"].actions["New"].triggered.connect(test_trigger)
  map = GMap()
  app.add_widget(map)
  app.add_timer(1000, update)
  app.run()

# class Map(QtGui.QWidget):

#   def __init__(self):

#     self.web = QWebView(self.window)
#     self.web.setMinimumSize(800, 800)
# self.web.page().mainFrame().addToJavaScriptWindowObject('self', self)

# self.web.setHtml(maphtml)
# self.web.loadQUrl.fromLocalFile("C:/cygwin/home/cosgrma/workspace/libs/python/modules/sandbox/gmaps.html")
#     self.web.load(QUrl.fromLocalFile(QFileInfo("gmaps.html").absoluteFilePath()))
#     self.button = QPushButton(self.window)
#     self.button.clicked.connect(self.add_marker)
#     self.text = QTextEdit(self.window)
#     self.layout = QVBoxLayout(self.window)
#     self.layout.addWidget(self.web)
#     self.layout.addWidget(self.text)

#     self.window.show()
#     self.exec_()

#   def add_marker(self):
# self.web.page().currentFrame().evaluateJavaScript(QString("addMarker(37.5, -122.2)"))
#     self.web.page().currentFrame().evaluateJavaScript(QString("addErrorCircle(37.5, -122.2, 1000)"))

#   @pyqtSlot(float, float, int)
#   def polygoncomplete(self, lat, lng, i):
#     if i == 0:
#       self.text.clear()
# self.text.append("Point #{} ({}, {})".format(i, lat, lng))
