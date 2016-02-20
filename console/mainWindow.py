#!/usr/bin/env python
# -*- coding: utf-8 -*-;
"""Name of module.

Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
  Examples can be given using either the ``Example`` or ``Examples``
  sections. Sections support any reStructuredText formatting, including
  literal blocks::

      $ python mainWindow.py

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
# @Date:   2015-12-04 05:39:48
# @Last Modified by:   cosgrma
# @Last Modified time: 2016-02-17 07:35:18
# REF: http://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_google.html#example-google
# REF: http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

__author__ = "Mathew Cosgrove"
__copyright__ = ""
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Mathew Cosgrove"
__email__ = "cosgroma@gmail.com"
__status__ = "Development"

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
  _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
  def _fromUtf8(s):
    return s

try:
  _encoding = QtGui.QApplication.UnicodeUTF8

  def _translate(context, text, disambig):
    return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
  def _translate(context, text, disambig):
    return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):

  def setupUi(self, MainWindow):
    font = QtGui.QFont()
    font.setFamily(_fromUtf8("Courier New"))

    self.centralwidget = MainWindow
    self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
    #
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
    sizePolicy.setHorizontalStretch(1)
    sizePolicy.setVerticalStretch(1)
    #
    self.centralwidget.setSizePolicy(sizePolicy)

    #
    self.portsComboBox = QtGui.QComboBox(self.centralwidget)
    self.portsComboBox.setObjectName(_fromUtf8("portsComboBox"))
    #
    self.refreshPortsPushButton = QtGui.QPushButton(self.centralwidget)
    self.refreshPortsPushButton.setEnabled(True)
    self.refreshPortsPushButton.setMaximumSize(QtCore.QSize(38, 27))
    self.refreshPortsPushButton.setText(_fromUtf8(""))
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.refreshPortsPushButton.setIcon(icon)
    self.refreshPortsPushButton.setIconSize(QtCore.QSize(16, 16))
    self.refreshPortsPushButton.setObjectName(_fromUtf8("refreshPortsPushButton"))
    #
    self.baudRateComboBox = QtGui.QComboBox(self.centralwidget)
    self.baudRateComboBox.setObjectName(_fromUtf8("baudRateComboBox"))
    #
    self.connectPushButton = QtGui.QPushButton(self.centralwidget)
    self.connectPushButton.setObjectName(_fromUtf8("connectPushButton"))

    self.logPushButton = QtGui.QPushButton(self.centralwidget)
    self.logPushButton.setObjectName(_fromUtf8("logPushButton"))
    self.filterButton = QtGui.QPushButton(self.centralwidget)
    self.filterButton.setObjectName(_fromUtf8("filterButton"))

    # self.logFieldEdit = QtGui.QLineEdit(self.centralwidget)
    # self.logFieldEdit.setFont(font)
    # self.logFieldEdit.setDragEnabled(True)
    # self.logFieldEdit.setObjectName(_fromUtf8("logFieldEdit"))

    self.horizontalLayout = QtGui.QHBoxLayout()
    self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
    self.horizontalLayout.addWidget(self.portsComboBox)
    self.horizontalLayout.addWidget(self.refreshPortsPushButton)
    self.horizontalLayout.addWidget(self.baudRateComboBox)
    self.horizontalLayout.addWidget(self.connectPushButton)
    self.horizontalLayout.addWidget(self.logPushButton)
    self.horizontalLayout.addWidget(self.filterButton)

    # splitter_serial = QtGui.QSplitter(QtCore.Qt.Vertical)
    #
    self.logPlainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
    self.logPlainTextEdit.setFont(font)
    self.logPlainTextEdit.setReadOnly(True)
    self.logPlainTextEdit.setObjectName(_fromUtf8("logPlainTextEdit"))
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
    sizePolicy.setHorizontalStretch(1)
    self.logPlainTextEdit.setSizePolicy(sizePolicy)
    #
    self.cmdLineEdit = QtGui.QLineEdit(self.centralwidget)
    self.cmdLineEdit.setFont(font)
    self.cmdLineEdit.setDragEnabled(True)
    self.cmdLineEdit.setObjectName(_fromUtf8("cmdLineEdit"))

    # self.horizontalLayout_2 = QtGui.QHBoxLayout()
    # self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
    # spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    # self.horizontalLayout_2.addItem(spacerItem)
    # self.horizontalLayout_2.addWidget(self.exitPushButton)

    self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
    self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
    self.verticalLayout.addLayout(self.horizontalLayout)
    self.verticalLayout.addWidget(self.logPlainTextEdit)
    self.verticalLayout.addWidget(self.cmdLineEdit)
    # self.verticalLayout.addLayout(self.horizontalLayout_2)

    self.retranslateUi(MainWindow)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)

  def retranslateUi(self, MainWindow):
    MainWindow.setWindowTitle(_translate("MainWindow", "PyQt Serial Port", None))
    self.connectPushButton.setText(_translate("MainWindow", "connect", None))
    self.logPushButton.setText(_translate("MainWindow", "log", None))
    self.filterButton.setText(_translate("MainWindow", "filter", None))
    # self.logFilter.setText(_translate("MainWindow", "start", None))

import mainWindow_rc
