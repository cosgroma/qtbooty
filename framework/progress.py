
from PyQt4 import QtGui
from PyQt4 import QtCore


class ProgressBar(QtGui.QWidget):

  def __init__(self, name="Progress", parent=None, total=20):
    super(ProgressBar, self).__init__(parent)
    self.pbar = QtGui.QProgressBar()
    self.pbar.setMinimum(1)
    self.pbar.setMaximum(total)
    main_layout = QtGui.QGridLayout()
    main_layout.addWidget(self.pbar, 0, 0)
    self.setLayout(main_layout)

  def update(self, value):
    self.pbar.setValue(value)


# app = QtGui.QApplication(sys.argv)
# bar = ProgressBar(total=101)
# bar.show()
# sys.exit(app.exec_())
