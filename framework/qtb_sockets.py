from PyQt4 import QtGui, QtNetwork
from PyQt4.QtCore import *


class Socket:
  socket_in = 0
  socket_out = 1


class QtBootySockets(QtNetwork.QUdpSocket):

  def __init__(self, port, ip=None, direction=Socket.socket_in, data_parser=None, parent=None):
    super(QtBootySockets, self).__init__(parent)
    self.port = port
    self.ip = ip
    self.data_parser = data_parser
    if direction == Socket.socket_in:
      self.bind(port)
      self.readyRead.connect(self.read_data)

  def read_data(self):
    while self.hasPendingDatagrams():
      data, host, port = self.readDatagram(self.pendingDatagramSize())
      self.data_parser(data)

  def write_data(self, data):
    self.writeDatagram(data, QtNetwork.QHostAddress(self.ip), self.port)

# class PrivateTcpServer(QtNetwork.QTcpServer):

#     tcpSocketReadySignal = pyqtSignal(name='tcpSocketReadySignal')
#     tcpfinishedSignal = pyqtSignal(name='tcpFinishedSignal')
#     tcpServerSamplesRequestSignal = pyqtSignal(name='tcpServerSamplesRequest')

#     def __init__(self, port):
#         super(PrivateTcpServer, self).__init__()
#         self.port = port
#         self.listen(QtNetwork.QHostAddress.Any, self.port)
#         self.newConnection.connect(self.handleIncomingConnection)

#     def start(self):
#         pass

#     @pyqtSlot()
#     def handleIncomingConnection(self):
#         self.tcpSocket = self.nextPendingConnection()
#         self.tcpSocketReadySignal.emit()

#     @pyqtSlot()
#     def sendData(self):
# samples.tofile(self.outfid)
# sampi = struct.pack("@" + "i" * len(samples), *samples)
#         while 1:
#             samples = self.getDataFunc()
# samples = struct.pack("@" + "i" * len(samples), *samples)
#             self.tcpSocket.writeData(samples)
#             self.tcpSocket.waitForBytesWritten(-1)

#     def setGetDataFunction(self, funcptr):
#         self.getDataFunc = funcptr
