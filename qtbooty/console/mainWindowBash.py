#!/usr/bin/env python
"""Name of module.

Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
  Examples can be given using either the ``Example`` or ``Examples``
  sections. Sections support any reStructuredText formatting, including
  literal blocks::

      $ python mainWindowBash.py

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

__author__ = "Mathew Cosgrove"
__copyright__ = ""
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Mathew Cosgrove"
__email__ = "cosgroma@gmail.com"
__status__ = "Development"


#
#

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
    self.centralwidget = MainWindow
    self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
    sizePolicy.setHorizontalStretch(1)
    sizePolicy.setVerticalStretch(1)
    self.centralwidget.setSizePolicy(sizePolicy)
    self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
    self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
    self.logPlainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
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
    font = QtGui.QFont()
    font.setFamily(_fromUtf8("Courier New"))
    self.cmdLineEdit.setFont(font)
    self.cmdLineEdit.setDragEnabled(True)
    self.cmdLineEdit.setObjectName(_fromUtf8("cmdLineEdit"))
    self.verticalLayout.addWidget(self.cmdLineEdit)

    self.retranslateUi(MainWindow)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)

  def retranslateUi(self, MainWindow):
    MainWindow.setWindowTitle(_translate("MainWindow", "PyBash", None))

import mainWindow_rc
