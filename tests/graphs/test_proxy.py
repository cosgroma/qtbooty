#!/usr/bin/env python

import os
import socket
import getpass
import keyring
from PyQt4 import QtCore, QtGui, QtWebKit, QtNetwork

import logging


if __name__ == '__main__':
  import random
  import logging
  import pyutils
  import getpass
  import keyring
  import sys
  app = QtGui.QApplication(sys.argv)
  # if keyring.get_password("system", getpass.getuser()) is None:
  keyring.set_password("system", getpass.getuser(), getpass.getpass())
  proxy = QtNetwork.QNetworkProxy(QtNetwork.QNetworkProxy.HttpProxy, "centralproxy.northgrum.com", 80)
  proxy.setUser(getpass.getuser())
  proxy.setPassword(keyring.get_password("system", getpass.getuser()))
  # QtNetwork.QNetworkProxy.setApplicationProxy(proxy)
  manager = QtNetwork.QNetworkAccessManager()
  manager.setProxy(proxy)  # setting the proxy on the manager

  # setting the proxy as application proxy

  QtNetwork.QNetworkProxy.setApplicationProxy(proxy)  # seems to do nothing..

  # web page

  webpage = QtWebKit.QWebView()
  # webpage.setNetworkAccessManager(manager)  # maybe.. but it doesn't work

  webpage.load(QtCore.QUrl("http://www.google.com"))
  webpage.show()
  sys.exit(app.exec_())
