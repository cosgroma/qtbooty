'''
Created on Dec 11, 2013

@author: cosgrma
'''

import sys
from private_canvas import PlotType, PrivatePlotCanvas
from PyQt4 import QtGui, QtCore, Qt

# class PlotType:
#     timeseries  = 1
#     polar       = 2
#     scatter     = 3
#     mesh        = 4
#     grid        = 5
#     bar         = 6
#     surf        = 7
#     image       = 8
#     hist        = 9
#     hist_norm   = 10
#     heat        = 11
#     image       = 12
#     fastbar     = 13

class PlotTimeSeries(QtGui.QWidget):
    pass

class PlotWidget(QtGui.QWidget):
    def __init__(self, plot_type, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.plot_layout = QtGui.QHBoxLayout()

        size_policy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        size_policy.setVerticalStretch(1)
        size_policy.setHorizontalStretch(0)
        self.setSizePolicy(size_policy)

        self.plot_canvas = PrivatePlotCanvas(plot_type, str(plot_type), parent=parent)
        self.plot_layout.addWidget(self.plot_canvas.get_widget())

        self.setLayout(self.plot_layout)

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


# def main():
#     # Create the App
#     app = QtGui.QApplication(sys.argv)
#     tabs_widget = TabsWidget()
#     with open('pyspy_styles.css',"r") as fh:
#         app.setStyleSheet(fh.read())

#     tabs_widget.setSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
#     mainLayout = QtGui.QVBoxLayout()
#     mainLayout.addWidget(tabs_widget.box)
#     tabs_widget.setLayout(mainLayout)
#     # Show the Window
#     tabs_widget.show()
#     # Execute the app and perform sys cleanup on exit
#     sys.exit(app.exec_())

# if __name__ == "__main__":
#     main()



#         plot_types = [attr for attr in dir(PlotType) if not callable(attr) and not attr.startswith("__")]
#         self.plots = dict()
#         self.plots["timeseries"] = PlotWidget(PlotType.timeseries)
#         # self.plots["polar"] = PlotWidget(PlotType.polar, parent=self.box)
#         # self.plots["scatter"] = PlotWidget(PlotType.scatter, parent=self.box)
#         self.plots["mesh"] = PlotWidget(PlotType.mesh)
#         # self.plots["grid"] = PlotWidget(PlotType.grid)

#         for k in self.plots.keys():
#             self.tab_widget.addTab(self.plots[k], k)
#         # for plot in plot_types:
#         #     print(plot)
#         #     self.plots[plot] = PlotWidget(getattr(PlotType, plot))
#         #     self.tab_widget.addTab(self.plots[plot].plot_widget, plot)
#         self.status_layout.addWidget(self.tab_widget)
#         self.box.setLayout(self.status_layout)
