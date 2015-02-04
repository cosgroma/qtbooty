
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-12-05 22:26:11
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2015-02-03 15:15:16

import PyQt4.QtGui
from PyQt4 import QtGui, QtCore, Qt
from PyQt4.QtCore import pyqtSignal, pyqtSlot

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui

import pyqtgraph.parametertree.parameterTypes as pTypes
from pyqtgraph.parametertree import Parameter, ParameterTree, ParameterItem, registerParameterType

from copy import deepcopy
import numpy as np

from functools import partial

import logging

from components import make_funcs

import simplejson as json
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


group_instance = {
  "name":        None,
  "box_enabled": False,
  "group_name":    None,
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


# class ComplexParameter(pTypes.GroupParameter):
#     def __init__(self, **opts):
#         opts['type'] = 'bool'
#         opts['value'] = True
#         pTypes.GroupParameter.__init__(self, **opts)

#         self.addChild({'name': 'A = 1/B', 'type': 'float', 'value': 7, 'suffix': 'Hz', 'siPrefix': True})
#         self.addChild({'name': 'B = 1/A', 'type': 'float', 'value': 1/7., 'suffix': 's', 'siPrefix': True})
#         self.a = self.param('A = 1/B')
#         self.b = self.param('B = 1/A')
#         self.a.sigValueChanged.connect(self.aChanged)
#         self.b.sigValueChanged.connect(self.bChanged)

#     def aChanged(self):
#         self.b.setValue(1.0 / self.a.value(), blockSignal=self.bChanged)

#     def bChanged(self):
#         self.a.setValue(1.0 / self.b.value(), blockSignal=self.aChanged)

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

    config["groups"] = [deepcopy(group_instance) for i in range(ngroups)]

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
    self.groups = []

    self.p = Parameter.create(name='params', type='group')

    for group in config["groups"]:
      c = deepcopy(group_instance)
      c.update(group)

      if c["box_enabled"]:
        widget = QtGui.QGroupBox(c["group_name"])
        widget.setCheckable(c["checkable"])
      else:
        widget = QtGui.QWidget()

      layout = get_layout(c["layout"])
      widget.setLayout(layout)
      self.groups.append(layout)

      for io in c["items"]:
        iow = make_funcs[io["class"]](io, callback=self.generic_callback)
        self.io_widgets[io["name"]] = iow
        layout.addWidget(iow)
        io["added"] = True
        self.p.addChild(io)

      if c["scrollable"]:
        widget2 = QtGui.QGroupBox(c["box_name"])
        layout2 = get_layout(c["layout"])
        widget.setTitle("")
        scroll = QtGui.QScrollArea()
        scroll.setWidget(widget)
        scroll.setWidgetResizable(True)
        scroll.setAlignment(QtCore.Qt.AlignTop)
        scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        layout2.addWidget(scroll)
        widget2.setLayout(layout2)
        widget = widget2

      self.layout.addWidget(widget)
      # self.p.sigTreeStateChanged.connect(change)
    return self.p

  def config_update(self, config):
    for idx, c in enumerate(config["groups"]):
      layout = self.groups[idx]
      for io in c["items"]:
        if io["added"]:
          continue
        layout.addWidget(make_funcs[io["class"]](io, callback=self.generic_callback))

        io["added"] = True

  def update_widget(self, name, data):
    instance = self.io_widgets[name]
    table_items = []
    for d in data:
      if d not in icon_lookup.keys():
        table_items.append(QtGui.QTableWidgetItem(d))
      else:
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsUserCheckable |
                          QtCore.Qt.ItemIsEnabled)
        item.setIcon(QtGui.QIcon(icon_lookup[d]))
        table_items.append(item)

    row = instance.rowCount()
    instance.insertRow(row)
    for idx, item in enumerate(table_items):
      item.setTextAlignment(QtCore.Qt.AlignCenter)
      instance.setItem(row, idx, item)

    # tableitem = instance.(1,1)

    # imageName = QtCore.QFileInfo(fileName).baseName()
    # item0 = QtGui.QTableWidgetItem(imageName)
    # item0.setData(QtCore.Qt.UserRole, fileName)
    # item0.setFlags(item0.flags() & ~QtCore.Qt.ItemIsEditable)
    # tableitem.setBackgroundColor(QtGui.QColor("gray"))



    # instance.setRowCount(row + 1)

  def get_icon(self, description):
    if description == "delete":
      return




def get_layout(args):
  layout = layout_lookup[args[0]]()
  layout.setAlignment(align_lookup[args[1]])
  return layout