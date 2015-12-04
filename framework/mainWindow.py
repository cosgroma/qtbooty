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
# @Last Modified time: 2015-12-04 06:14:48
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
    # MainWindow.setObjectName(_fromUtf8("MainWindow"))
    # MainWindow.resize(641, 567)
    self.centralwidget = MainWindow
    self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
    sizePolicy.setHorizontalStretch(1)
    sizePolicy.setVerticalStretch(1)
    self.centralwidget.setSizePolicy(sizePolicy)
    # self.gridLayout = QtGui.QGridLayout(self.centralwidget)
    # self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
    self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
    self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
    self.horizontalLayout = QtGui.QHBoxLayout()
    self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
    self.portsComboBox = QtGui.QComboBox(self.centralwidget)
    # sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
    # sizePolicy.setHorizontalStretch(0)
    # sizePolicy.setVerticalStretch(0)
    # sizePolicy.setHeightForWidth(self.portsComboBox.sizePolicy().hasHeightForWidth())
    # self.portsComboBox.setSizePolicy(sizePolicy)
    # self.portsComboBox.setMinimumSize(QtCore.QSize(200, 27))
    self.portsComboBox.setObjectName(_fromUtf8("portsComboBox"))
    self.horizontalLayout.addWidget(self.portsComboBox)
    self.refreshPortsPushButton = QtGui.QPushButton(self.centralwidget)
    self.refreshPortsPushButton.setEnabled(True)
    # sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
    # sizePolicy.setHorizontalStretch(0)
    # sizePolicy.setVerticalStretch(0)
    # sizePolicy.setHeightForWidth(self.refreshPortsPushButton.sizePolicy().hasHeightForWidth())
    # self.refreshPortsPushButton.setSizePolicy(sizePolicy)
    # self.refreshPortsPushButton.setMinimumSize(QtCore.QSize(38, 27))
    self.refreshPortsPushButton.setMaximumSize(QtCore.QSize(38, 27))
    self.refreshPortsPushButton.setText(_fromUtf8(""))
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.refreshPortsPushButton.setIcon(icon)
    self.refreshPortsPushButton.setIconSize(QtCore.QSize(16, 16))
    self.refreshPortsPushButton.setObjectName(_fromUtf8("refreshPortsPushButton"))
    self.horizontalLayout.addWidget(self.refreshPortsPushButton)
    self.baudRateComboBox = QtGui.QComboBox(self.centralwidget)
    # self.baudRateComboBox.setMinimumSize(QtCore.QSize(91, 27))
    self.baudRateComboBox.setObjectName(_fromUtf8("baudRateComboBox"))
    self.horizontalLayout.addWidget(self.baudRateComboBox)
    self.connectPushButton = QtGui.QPushButton(self.centralwidget)
    # sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
    # sizePolicy.setHorizontalStretch(0)
    # sizePolicy.setVerticalStretch(0)
    # sizePolicy.setHeightForWidth(self.connectPushButton.sizePolicy().hasHeightForWidth())
    # self.connectPushButton.setSizePolicy(sizePolicy)
    # self.connectPushButton.setMinimumSize(QtCore.QSize(91, 27))
    self.connectPushButton.setObjectName(_fromUtf8("connectPushButton"))
    self.horizontalLayout.addWidget(self.connectPushButton)
    self.disconnectPushButton = QtGui.QPushButton(self.centralwidget)
    # sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
    # sizePolicy.setHorizontalStretch(0)
    # sizePolicy.setVerticalStretch(0)
    # sizePolicy.setHeightForWidth(self.disconnectPushButton.sizePolicy().hasHeightForWidth())
    # self.disconnectPushButton.setSizePolicy(sizePolicy)
    # self.disconnectPushButton.setMinimumSize(QtCore.QSize(91, 27))
    self.disconnectPushButton.setObjectName(_fromUtf8("disconnectPushButton"))
    self.horizontalLayout.addWidget(self.disconnectPushButton)
    self.verticalLayout.addLayout(self.horizontalLayout)
    self.logPlainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
    # self.logPlainTextEdit.setMinimumSize(QtCore.QSize(270, 200))
    font = QtGui.QFont()
    font.setFamily(_fromUtf8("Courier New"))
    self.logPlainTextEdit.setFont(font)
    self.logPlainTextEdit.setReadOnly(True)
    self.logPlainTextEdit.setObjectName(_fromUtf8("logPlainTextEdit"))

    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
    sizePolicy.setHorizontalStretch(1)
    self.logPlainTextEdit.setSizePolicy(sizePolicy)
    self.verticalLayout.addWidget(self.logPlainTextEdit)

    self.cmdLineEdit = QtGui.QLineEdit(self.centralwidget)
    # self.cmdLineEdit.setMinimumSize(QtCore.QSize(0, 27))
    font = QtGui.QFont()
    font.setFamily(_fromUtf8("Courier New"))
    self.cmdLineEdit.setFont(font)
    self.cmdLineEdit.setDragEnabled(True)
    self.cmdLineEdit.setObjectName(_fromUtf8("cmdLineEdit"))
    self.verticalLayout.addWidget(self.cmdLineEdit)
    self.horizontalLayout_2 = QtGui.QHBoxLayout()
    self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
    spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.horizontalLayout_2.addItem(spacerItem)
    self.exitPushButton = QtGui.QPushButton(self.centralwidget)
    # sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
    # sizePolicy.setHorizontalStretch(0)
    # sizePolicy.setVerticalStretch(0)
    # sizePolicy.setHeightForWidth(self.exitPushButton.sizePolicy().hasHeightForWidth())
    # self.exitPushButton.setSizePolicy(sizePolicy)
    # self.exitPushButton.setMinimumSize(QtCore.QSize(91, 27))
    self.exitPushButton.setObjectName(_fromUtf8("exitPushButton"))
    self.horizontalLayout_2.addWidget(self.exitPushButton)
    self.verticalLayout.addLayout(self.horizontalLayout_2)
    # self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
    # MainWindow.setCentralWidget(self.centralwidget)
    # self.menubar = QtGui.QMenuBar(MainWindow)
    # self.menubar.setGeometry(QtCore.QRect(0, 0, 641, 24))
    # self.menubar.setObjectName(_fromUtf8("menubar"))
    # self.menuFile = QtGui.QMenu(self.menubar)
    # self.menuFile.setObjectName(_fromUtf8("menuFile"))
    # MainWindow.setMenuBar(self.menubar)
    # self.statusbar = QtGui.QStatusBar(MainWindow)
    # self.statusbar.setObjectName(_fromUtf8("statusbar"))
    # MainWindow.setStatusBar(self.statusbar)
    # self.actionExit = QtGui.QAction(MainWindow)
    # self.actionExit.setObjectName(_fromUtf8("actionExit"))
    # self.menuFile.addAction(self.actionExit)
    # self.menubar.addAction(self.menuFile.menuAction())

    self.retranslateUi(MainWindow)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)

  def retranslateUi(self, MainWindow):
    MainWindow.setWindowTitle(_translate("MainWindow", "SPPyQt", None))
    self.connectPushButton.setText(_translate("MainWindow", "Connect", None))
    self.disconnectPushButton.setText(_translate("MainWindow", "Disconnect", None))
    # self.exitPushButton.setText(_translate("MainWindow", "Exit", None))
    # self.menuFile.setTitle(_translate("MainWindow", "File", None))
    # self.actionExit.setText(_translate("MainWindow", "Exit", None))

import mainWindow_rc
