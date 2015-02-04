
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-12-05 22:26:11
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2015-02-03 21:32:48

from copy import deepcopy
from functools import partial
import logging

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
  "delete": '../resources/deleteIcon.png'
}


group_default = {
  "name":        None,
  "enabled":     True,
  "box_enabled": False,
  "group_name":  None,
  "layout":      None,
  "scrollable":  False,
  "checkable":   False,
  "added":       False,
  "items":       []
}

io_instance = {
  "name":     None,
  "class":    "",
  "added":    False,
  "label":    None,
  "tool-tip": None,
  "default":  None,
  "dtype":    None
}


## If anything changes in the tree, print a message
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
    self.logger = logging.getLogger("iogrid")
    self.io_widgets = dict()

  def load_config_file(self, filename):
    return self.config_widget(json.load(open(filename, 'r')))

  def load_config(self, config):
    return self.config_widget(config)

  def config_init(self, ngroups, nitems_arr):
    """
    @summary:
    @param ngroups:
    @param nitems_arr:
    @result:
    """
    # Set default config layout for self widget
    config = {"layout": ["h", "na"]}

    # populated the default groups, check if well formed
    if not ngroups == len(nitems_arr):
      self.logger.error(
        "nitems_arr length (%d) doest not match ngroups (%d)" %
        (ngroups, nitems_arr)
      )

    config["groups"] = [deepcopy(group_default) for i in range(ngroups)]

    # populated a set of default item configurations for each group
    for c, nitems in zip(config["groups"], nitems_arr):
      c["items"] = [deepcopy(io_instance) for n in range(0, nitems)]
    return config

  def generic_callback(self, obj, instance):
    if isinstance(obj, PyQt4.QtGui.QAbstractSlider):
      self.p.param(instance["name"]).setValue(obj.value())
    elif isinstance(obj, PyQt4.QtGui.QAbstractButton):
      self.p.param(instance["name"]).setValue(1)
      try:
        self.p.param(instance["name"]).setValue(0, blockSignal=self.callback)
      except Exception, e:
        pass

    else:
      self.p.param(instance["name"]).setValue(obj.text())

  def connect_changed_callback(self, callback):
    self.callback = callback
    self.p.sigTreeStateChanged.connect(callback)

  def config_widget(self, config):
    self.layout = get_layout(config["layout"])
    self.setLayout(self.layout)
    # self.groups = []

    self.p = Parameter.create(name='params', type='group')

    for gconf in config["groups"]:
      if not gconf["enabled"]: continue
      group = deepcopy(group_default)
      group.update(gconf)

      if group["box_enabled"]:
        widget = QtGui.QGroupBox(group["group_name"])
        widget.setCheckable(group["checkable"])
      else:
        widget = QtGui.QWidget()

      layout = get_layout(group["layout"])
      widget.setLayout(layout)
      # self.groups.append(layout)

      for io in group["items"]:
        iow = make_funcs[io["class"]](io, callback=self.generic_callback)
        self.io_widgets[io["name"]] = iow
        layout.addWidget(iow)
        io["added"] = True
        self.p.addChild(io)

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

      if "group_layout_params" in config.keys():
        self.layout.addWidget(widget, *config["group_layout_params"][group["group_name"]])
      else:
        self.layout.addWidget(widget)

    #
      # self.p.sigTreeStateChanged.connect(change)
    return self.p

  def config_update(self, config):
    for idx, c in enumerate(config["groups"]):
      layout = self.groups[idx]
      for io in c["items"]:
        if io["added"]: continue
        layout.addWidget(make_funcs[io["class"]](io, callback=self.generic_callback))
        io["added"] = True

  def update_widget(self, name, data):
    self.update_table_widget(name, data)

  def update_table_widget(self, name, data):
    def new_table_item(label=""):
      item = QtGui.QTableWidgetItem(label)
      item.setTextAlignment(QtCore.Qt.AlignCenter)
      item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
      return item

    table = self.io_widgets[name]
    row = table.rowCount()
    table.insertRow(row)

    item = new_table_item()
    table.setItem(row, 0, item)

    cellLayout = QtGui.QHBoxLayout()

    enWidget = QtGui.QComboBox()
    enWidget.addItems(["a", "b", "c"])
    edWidget = QtGui.QPushButton("EDIT")
    edWidget.setSizePolicy(
      QtGui.QSizePolicy(
        QtGui.QSizePolicy.Preferred,
        QtGui.QSizePolicy.Preferred
      )
    )

    cellLayout.addWidget(enWidget)
    # cellLayout.addWidget(edWidget)
    cellWidget = enWidget
    # cellWidget = QtGui.QWidget()
    # cellWidget.setLayout(cellLayout)
    table.setCellWidget(row, 0, cellWidget)

    for idx, d in enumerate(data, start=1):
      item = new_table_item(d)
      table.setItem(row, idx, item)

    item.setIcon(QtGui.QIcon(icon_lookup["delete"]))
    table.setItem(row, len(d) + 1, item)

  def get_icon(self, description):
    if description == "delete":
      return



def get_layout(args):
  layout = layout_lookup[args[0]]()
  layout.setAlignment(align_lookup[args[1]])
  return layout