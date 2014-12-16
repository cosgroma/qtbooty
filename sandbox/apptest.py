import sys
sys.path.append('/Users/cosgroma/workspace/sergeant/guis')

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import *

from QtBooty import App
from QtBooty import graphs
from QtBooty import framework

class PieChart (QDeclarativeItem):

    def __init__(self, parent = None):
        QDeclarativeItem.__init__(self, parent)
        # need to disable this flag to draw inside a QDeclarativeItem
        self.setFlag(QGraphicsItem.ItemHasNoContents, False)
        self._name = u''
        self.time_series = graphs.TimeSeries(interval=50, maxlen=100)
        self.time_series.run_test( interval=50, dynamic=True, freqs=[.1, .2, .3])

    def paint(self, painter, options, widget):
        pen = QPen(self.color, 2)
        painter.setPen(pen);
        painter.setRenderHints(QPainter.Antialiasing, True);
        painter.drawPie(self.boundingRect(), 90 * 16, 290 * 16);

    def getColor(self):
        return self._color

    def setColor(self, value):
        self._color = value

    def getName(self):
        return self._name

    def setName(self, value):
        self._name = value

    color = Property(QColor, getColor, setColor)
    name = Property(unicode, getName, setName)

    chartCleared = Signal()

    @Slot() # This should be something like @Invokable
    def clearChart(self):
        self.setColor(Qt.transparent)
        self.update()
        self.chartCleared.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    qmlRegisterType(PieChart, 'Charts', 1, 0, 'PieChart');

    view = QDeclarativeView()
    view.setSource(QUrl.fromLocalFile('app.qml'))
    view.show()
    sys.exit(app.exec_())
