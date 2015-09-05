
from PyQt4 import QtGui, QtCore, Qt


class Tabs(QtGui.QWidget):

  def __init__(self, parent=None):
    # Initialize the QWidget object you have extended
    # QtGui.QWidget.__init__(self, parent)
    super(Tabs, self).__init__()
    # self.setSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
    self.widget = Qt.QTabWidget()
    self.layout = QtGui.QHBoxLayout()
    self.layout.addWidget(self.widget)
    self.setLayout(self.layout)

    # self.setSizePolicy(
    #   QtGui.QSizePolicy(
    #     QtGui.QSizePolicy.MinimumExpanding,
    #     QtGui.QSizePolicy.Maximum
    #   )
    # )
    # self.widget.setMaximumWidth(900)
    # self.widget.setMinimumWidth(300)

    # self.widget.setMaximumWidth(900)?
    # self.widget.setMinimumHeight(300)
    # self.widget.setSizePolicy(
    #   QtGui.QSizePolicy(
    #     QtGui.QSizePolicy.MinimumExpanding,
    #     QtGui.QSizePolicy.Maximum
    #   )
    # )
    # self.setMaximumWidth(1200)
  def add_tab(self, widget, name=None):
    self.widget.addTab(widget, name)
