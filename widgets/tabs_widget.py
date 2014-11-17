
import sys
from QtBooty.graphs import TimeSeriesWidget

from PyQt4 import QtGui, QtCore, Qt

class TabsWidget(QtGui.QWidget):
    def __init__(self,  parent=None):
        # Initialize the QWidget object you have extended
        QtGui.QWidget.__init__(self, parent)
        self.setSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.layout = QtGui.QVBoxLayout()
        self.tab_widget = Qt.QTabWidget()

    def add_tab(self, widget, name=None):
        self.tab_widget.addTab(widget, name)

    def commit_layout(self):
        self.layout.addWidget(self.tab_widget)
        self.setLayout(self.layout)

