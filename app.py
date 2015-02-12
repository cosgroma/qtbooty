#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-12-05 20:56:57
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2015-02-12 05:34:46

import logging
logger = logging.getLogger(__name__)

import sys
import os

from os import path
import json

from PyQt4 import QtCore, QtGui


color_gradients = {
  "orange": [("gradienta", "#b56c17"), ("gradientb", "#d7801a"), ("gradientc", "#ffa02f"), ("gradientd", "#ffaa00")],
  "blue": [("gradienta", "#353DE7"), ("gradientb", "#484FE5"), ("gradientc", "#5B61E4"), ("gradientd", "#6E74E2")],
  "blue2": [("gradienta", "#484FE5"), ("gradientb", "#353DE7"), ("gradientc", "#222BE9"), ("gradientd", "#0F19EB")],
  "green": [("gradienta", "#2CF293"), ("gradientb", "#38F296"), ("gradientc", "#45F29A"), ("gradientd", "#52F39E")]
}


default_settings = {
  "name": "Default Settings File",
  "size": {
    "layout": "g",
    "policy": "unbounded",
    "min": [100, 100],
    "max": [480, 320]
  },
  "menu": {
    "enabled": True,
    "items": [{
      "name": "File",
      "actions": [{
        "name": "New",
        "shortcut": "Ctrl+N",
        "tip": "make a new file"
        }, {
        "name": "Open",
        "shortcut" : "Ctrl+O",
        "tip": "open an existing file"
        }]
      }, {
      "name": "Edit",
      "actions": []
      }, {
      "name": "View",
      "actions": [{
          "name": "CPU Statistics",
          "shortcut": "Ctrl+N",
          "tip": "view run-time CPU stats"
          }]
    }]
  },
  "status": {
    "enabled": True
  }
}

layout_lookup = {
  "h": QtGui.QHBoxLayout,
  "v": QtGui.QVBoxLayout,
  "g": QtGui.QGridLayout,
  "f": QtGui.QFormLayout
}

#
class App(QtGui.QApplication):
  """
  @summary:
  """
  def __init__(self, json_file=None):
    """
    @summary:
    @param json_file:
    @result:
    """
    super(App, self).__init__(sys.argv)
    self.resources = path.join(path.dirname(__file__), 'resources')
    # Setup high level logging for this system
    # logging.basicConfig(format='%(asctime)s %(message)s',
    #                     datefmt='%m/%d/%Y %I:%M:%S %p')
    self.timers = []
    self.widgets = dict()
    self.app_settings = None

    # Process the app configuration file
    if json_file is not None and os.path.isfile(json_file):
      self.json_file = json_file
      self.app_settings = json.load(open(json_file))
    else:
      logger.critical('config file fucked up : %s' % (json_file))
      self.app_settings = default_settings

    self.main = MainWindow(self.app_settings)
    self.apply_style("default")

  def add_widget(self, widget, *args):
    logger.debug('widget args : %s' % (args, ))
    if args is not None:
      if self.main.settings["size"]["layout"] == "g":
        logger.debug('main is grid layout')
        self.main.layout.addWidget(widget, *args)
    else:
      self.main.layout.addWidget(widget)

  def add_timer(self, interval, callback):
    timer = QtCore.QTimer()
    timer.setInterval(interval)
    timer.timeout.connect(callback)
    self.timers.append(timer)

  def add_close_callback(self, callback):
    self.main.set_close_callback(callback)

  def apply_style(self, name):
    with open(path.join(self.resources, 'styles', 'style.css'), "r") as style:
      styleSheet = style.read()
      import numpy as np
      rand_key = color_gradients.keys()[np.random.randint(len(color_gradients.keys()))]

      for item, value in color_gradients[rand_key]:
        styleSheet = styleSheet.replace((item), value)
      self.setStyleSheet(styleSheet)

  def update_status(self, message):
    self.main.update_status(message)

  def run(self):
    for timer in self.timers:
      timer.start()
    self.main.show()
    sys.exit(self.exec_())


class MainWindow(QtGui.QMainWindow):
  def __init__(self, settings=None):
    super(MainWindow, self).__init__()
    self.settings = settings
    self.menus = None
    self.layout = None
    self.close_callback = None

    # Setup the minimum structure before you process settings
    self.central = QtGui.QWidget()
    self.setCentralWidget(self.central)



    # Process user settings
    if self.settings is not None:
      self.apply_settings()

  def apply_settings(self):
    self.central_setup()
    self.menu_setup()
    self.statusBar().showMessage("")

  def central_setup(self):
    self.setWindowTitle(self.settings["name"])


    if self.settings["size"]["policy"] == "bounded":
      self.setMinimumSize(self.settings["size"]["min"][0],
                          self.settings["size"]["min"][1])
      self.resize(self.settings["size"]["max"][0],
                  self.settings["size"]["max"][1])

    self.layout = layout_lookup[self.settings["size"]["layout"]]()
    self.central.setLayout(self.layout)
  def menu_setup(self):
    if self.settings["menu"]["enabled"]:
      self.menus = dict()
      for item in self.settings["menu"]["items"]:
        self.menus[item["name"]] = self.menuBar().addMenu(item["name"])
        self.menus[item["name"]].actions = dict()
        for action in item["actions"]:
          act = QtGui.QAction(action["name"], self,
                              shortcut=action["shortcut"],
                              statusTip=action["tip"])
          self.menus[item["name"]].actions[action["name"]] = act
          self.menus[item["name"]].addAction(self.menus[item["name"]].actions[action["name"]])

  def closeEvent(self, event):
    if self.close_callback is not None:
      self.close_callback()

  def update_status(self):
    if self.settings["status"]["enabled"]:
      self.statusBar().showMessage("test")
    # also by default added the CPU percentage and memory usage

  def set_close_callback(self, callback):
    self.close_callback = callback


def close_test():
  print("Closed")

if __name__ == '__main__':
  app = App('tests/config/app_config.json')
  # app.add_close_callback(close_test)
  # app.main.menus["File"].actions["New"].triggered.connect(test_trigger)
  app.run()
  print("test", )

