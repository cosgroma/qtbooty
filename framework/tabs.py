
from PyQt4 import QtGui, QtCore, Qt

class Tabs(QtGui.QWidget):
  def __init__(self,  parent=None):
    # Initialize the QWidget object you have extended
    # QtGui.QWidget.__init__(self, parent)
    super(Tabs, self).__init__()
    # self.setSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
    self.widget = Qt.QTabWidget()
    self.layout = QtGui.QHBoxLayout()
    self.layout.addWidget(self.widget)
    self.setLayout(self.layout)

  def add_tab(self, widget, name=None):
    self.widget.addTab(widget, name)



