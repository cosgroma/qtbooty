#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-12-05 22:26:11
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2016-06-16 23:58:12

import logging
try:
  import pyutils
  pyutils.setup_logging()
  # from pyutils import is_number
except:
  pass
logger = logging.getLogger(__name__)

import os
from copy import deepcopy
from functools import partial
import simplejson as json
import numpy as np
from PyQt4 import QtGui, QtCore, Qt
from pyqtgraph.Qt import QtCore, QtGui
from PyQt4.QtCore import pyqtSignal, pyqtSlot
import PyQt4.QtGui
import pyqtgraph as pg
from pyqtgraph.parametertree import Parameter, ParameterTree, ParameterItem, registerParameterType
import pyqtgraph.parametertree.parameterTypes as pTypes
from components import make_funcs
from tabs import Tabs


def is_number(s):
  try:
    float(s)
    return True
  except ValueError:
    pass

  try:
    import unicodedata
    unicodedata.numeric(s)
    return True
  except (TypeError, ValueError):
    pass
  return False

############################################

#    ____  ____  ________  _____     _______  ________  _______     ______
#   |_   ||   _||_   __  ||_   _|   |_   __ \|_   __  ||_   __ \  .' ____ \
#     | |__| |    | |_ \_|  | |       | |__) | | |_ \_|  | |__) | | (___ \_|
#     |  __  |    |  _| _   | |   _   |  ___/  |  _| _   |  __ /   _.____`.
#    _| |  | |_  _| |__/ | _| |__/ | _| |_    _| |__/ | _| |  \ \_| \____) |
#   |____||____||________||________||_____|  |________||____| |___|\______.'
#

layout_lookup = {
    "h": QtGui.QHBoxLayout,
    "v": QtGui.QVBoxLayout,
    "g": QtGui.QGridLayout,
    "f": QtGui.QFormLayout
}

align_lookup = {
    "t": QtCore.Qt.AlignTop,
    "b": QtCore.Qt.AlignBottom,
    "l": QtCore.Qt.AlignLeft,
    "r": QtCore.Qt.AlignRight,
    "c": QtCore.Qt.AlignCenter,
    "j": QtCore.Qt.AlignJustify,
    "b": QtCore.Qt.AlignBottom,
    "na": QtCore.Qt.AlignTop,
}

icon_lookup = {
    "enable": os.path.join(os.path.dirname(__file__), 'icons', 'enable2.png'),
    "edit": '../resources/edit.png',
    "delete": '../resources/delete.png',
}


config_defaults = {
    "layout": ["h", "na"],
    "tabs_enabled": False,
    "groups": []
}

group_default = {
    "name": None,
    "enabled": True,
    "box_enabled": False,
    "tabs_enabled": False,
    "splitter_enabled": False,
    "group_name": None,
    "layout": None,
    "scrollable": False,
    "checkable": False,
    "added": False,
    "items": []
}

io_instance = {
    "name": None,
    "class": "",
    "added": False,
    "label": None,
    "tool-tip": None,
    "default": None,
    "type": None
}


# If anything changes in the tree, print a message
def change(param, changes):
  print("tree changes:")
  for param, change, data in changes:
    # path = p.childPath(param)
    # if path is not None:
    #   childName = '.'.join(path)
    # else:
    childName = param.name()
    print('  parameter: %s' % childName)
    print('  change:    %s' % change)
    print('  data:      %s' % str(data))
    print('  ----------')


class IOGrid(QtGui.QWidget):

  """
  @summary:
  """

  def __init__(self):
    super(IOGrid, self).__init__()
    # logging.basicConfig()
    self.logger = logging.getLogger(__name__)
    self.io_widgets = dict()

  def load_config_file(self, filename):
    return self.config_widget(json.load(open(filename, 'r')))

  def load_config(self, config):
    if config is None:
      return self.config_widget(config_defaults)
    else:
      return self.config_widget(config)

  # def config_init(self, ngroups, nitems_arr):
  #   """
  #   @summary:
  #   @param ngroups:
  #   @param nitems_arr:
  #   @result:
  #   """
  # Set default config layout for self widget
  #   config = {"layout"}

  # populated the default groups, check if well formed
  #   if not ngroups == len(nitems_arr):
  #     self.logger.error(
  #       "nitems_arr length (%d) doest not match ngroups (%d)" %
  #       (ngroups, nitems_arr)
  #     )

  #   config["groups"] = [deepcopy(group_default) for i in range(ngroups)]

  # populated a set of default item configurations for each group
  #   for c, nitems in zip(config["groups"], nitems_arr):
  #     c["items"] = [deepcopy(io_instance) for n in range(0, nitems)]
  #   return config

  def generic_callback(self, obj, instance):
    if isinstance(obj, PyQt4.QtGui.QAbstractSlider):
      self.p.param(instance["name"]).setValue(obj.value())
    elif isinstance(obj, PyQt4.QtGui.QAbstractButton):
      curval = self.p.param(instance["name"]).value()
      curval = 0 if curval is None else curval
      self.p.param(instance["name"]).setValue(1 ^ curval)
      # self.p.param(instance["name"]).setCheckable(True)
      # print(type(curval))
      # if curval == 1:
      #   setchecked = True
      # else:
      #   setchecked = False
      # obj.setChecked(setchecked)
      # sef.p.
      # self.p.param(instance["name"]).setValue(0, blockSignal=self.callback)
    elif isinstance(obj, PyQt4.QtGui.QComboBox):
      self.p.param(instance["name"]).setValue(obj.itemText(obj.currentIndex()))
    else:
      if instance["type"] in ["int", "float"] and is_number(obj.text()):
        value = eval("%s(%s)" % (instance["type"], obj.text()))
      else:
        value = obj.text()

      self.p.param(instance["name"]).setValue(value)

  def connect_changed_callback(self, callback):
    self.callback = callback
    self.p.sigTreeStateChanged.connect(callback)
    # self.p.sigValueChanged.connect(callback)

  def config_widget(self, user_config):
    config = deepcopy(config_defaults)
    config.update(user_config)

    self.layout = get_layout(config["layout"])
    self.setLayout(self.layout)
    self.groups = []
    self.group_names = dict()
    self.p = Parameter.create(name='params', type='group')

    if config["tabs_enabled"]:
      tabs = Tabs()
      self.layout.addWidget(tabs)

    for gconf in config["groups"]:
      if not gconf["enabled"]:
        continue
      group = deepcopy(group_default)
      group.update(gconf)

      if group["box_enabled"]:
        widget = QtGui.QGroupBox(group["group_name"])
        # widget.setSizePolicy(
        #     QtGui.QSizePolicy(
        #         QtGui.QSizePolicy.Maximum,
        #         QtGui.QSizePolicy.Maximum
        #     )
        # )
        self.group_names[group["group_name"]] = widget
        widget.setCheckable(group["checkable"])
      else:
        widget = QtGui.QWidget()

      if group["splitter_enabled"]:
        splitter = QtGui.QSplitter()
        splitter.setStretchFactor(0, 0)
        splitter.setStretchFactor(1, 1)

      layout = get_layout(group["layout"])
      widget.setLayout(layout)
      self.groups.append(layout)

      for io in group["items"]:
        self.p.addChild(io)
        iow = make_funcs[io["class"]](io, callback=self.generic_callback)
        self.io_widgets[io["name"]] = iow
        if group["splitter_enabled"]:
          splitter.addWidget(iow)
        else:
          layout.addWidget(iow)

        io["added"] = True
        # if instance["type"] is not None:
        #   self.p.[io["name"]]

      if group["scrollable"]:
        widget2 = QtGui.QGroupBox(group["group_name"])
        layout2 = get_layout(group["layout"])
        widget.setTitle("")
        scroll = QtGui.QScrollArea()
        scroll.setWidget(widget)
        scroll.setWidgetResizable(True)
        scroll.setAlignment(QtCore.Qt.AlignTop)
        scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        layout2.addWidget(scroll)
        widget2.setLayout(layout2)
        widget = widget2

      if config['tabs_enabled']:
        tabs.add_tab(widget, group["group_name"])
      elif "group_layout_params" in config.keys():
        self.layout.addWidget(widget, *config["group_layout_params"][group["group_name"]])
      elif group["splitter_enabled"]:
        self.layout.addWidget(splitter)
      else:
        self.layout.addWidget(widget)

      # self.p.sigTreeStateChanged.connect(change)
    return self.p, config

  def config_update(self, config):
    for idx, c in enumerate(config["groups"]):
      layout = self.groups[idx]
      for io in c["items"]:
        if "added" in io.keys() and io["added"]:
          continue
        self.p.addChild(io)
        iow = make_funcs[io["class"]](io, callback=self.generic_callback)
        self.io_widgets[io["name"]] = iow
        layout.addWidget(iow)
        io["added"] = True

  # def config_remove_io(self, name):
  #   self.p.removeChild(io)
  #     self.io_widgets[io["name"]]
  #   pass
  # def get_widget(self):

  def set_groups_enabled(self, names, enable):
    for name in names:
      self.group_names[name].setEnabled(enable)

  def update_widget(self, name, data, changed, controls=["enable", "edit", "delete"]):
    # If we aren't tracking a handle to this then bail
    if name not in self.io_widgets.keys():
      return

    # Otherwise we redirect the update toward particular object types
    if isinstance(self.io_widgets[name], PyQt4.QtGui.QTableWidget):
      self.update_table_widget(name, data, controls=controls)

    # Everything is at some point a QWidget, here we look at the type of change
    elif isinstance(self.io_widgets[name], PyQt4.QtGui.QWidget):
      for c in self.io_widgets[name].children():
        if isinstance(c, PyQt4.QtGui.QLineEdit):
          c.setText(str(data))

  def update_table_widget(self, name, data, controls=["enable", "edit", "delete"]):
    def new_table_item(label=""):
      item = QtGui.QTableWidgetItem(label)
      item.setTextAlignment(QtCore.Qt.AlignCenter)
      item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
      return item

    def new_button(name, height):
      button = QtGui.QPushButton()
      icon = icon_lookup[name]
      if os.path.isfile(icon):
        button.setIcon(QtGui.QIcon(icon))
      else:
        logger.info("icon file does not exist: %s" % (icon))
      button.setMinimumHeight(height)
      return button

    def control_buttons(item, height):
      controlLayout = QtGui.QHBoxLayout()
      controlLayout.setAlignment(QtCore.Qt.AlignVCenter)

      controlWidget = QtGui.QWidget()
      controlWidget.setMinimumHeight(height)
      controlWidget.setContentsMargins(0, -5, 0, 5)

      for cb in controls:
        instance = {"name": "%s.%d" % (cb, row)}
        button = new_button(cb, height)
        button.clicked.connect(partial(self.generic_callback, button, instance))
        controlLayout.addWidget(button)
        self.p.addChild(instance)

      controlWidget.setLayout(controlLayout)
      return controlWidget

    table = self.io_widgets[name]
    row = table.rowCount()
    table.insertRow(row)
    height = table.rowHeight(row) * .8

    item = new_table_item()
    table.setItem(row, 0, item)

    idx = 0
    if controls:
      table.setCellWidget(row, 0, control_buttons(item, height))
      idx = 1

    for idx, d in enumerate(data, start=idx):
      item = new_table_item(d)
      table.setItem(row, idx, item)

    table.sortItems(1, order=QtCore.Qt.AscendingOrder)


def get_layout(args):
  layout = layout_lookup[args[0]]()
  layout.setAlignment(align_lookup[args[1]])
  return layout
