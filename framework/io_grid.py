
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-12-05 22:26:11
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2015-01-30 02:03:06

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
############################################

#    ____  ____  ________  _____     _______  ________  _______     ______
#   |_   ||   _||_   __  ||_   _|   |_   __ \|_   __  ||_   __ \  .' ____ \
#     | |__| |    | |_ \_|  | |       | |__) | | |_ \_|  | |__) | | (___ \_|
#     |  __  |    |  _| _   | |   _   |  ___/  |  _| _   |  __ /   _.____`.
#    _| |  | |_  _| |__/ | _| |__/ | _| |_    _| |__/ | _| |  \ \_| \____) |
#   |____||____||________||________||_____|  |________||____| |___|\______.'
#

def get_layout(args):
  """
  @summary:
  @param name:
  @result:
  """
  name = args[0]
  align = args[1]

  if name == "h":
    layout = QtGui.QHBoxLayout()
  elif name == "v":
    layout = QtGui.QVBoxLayout()
  elif name == "g":
    layout = QtGui.QGridLayout()
  elif name == "f":
    layout = QtGui.QFormLayout()

  if align == "t":
    layout.setAlignment(QtCore.Qt.AlignTop)
  elif align == "b":
    layout.setAlignment(QtCore.Qt.AlignBottom)
  elif align == "l":
    layout.setAlignment(QtCore.Qt.AlignLeft)
  elif align == "r":
    layout.setAlignment(QtCore.Qt.AlignRight)
  elif align == "c":
    layout.setAlignment(QtCore.Qt.AlignCenter)
  elif align == "j":
    layout.setAlignment(QtCore.Qt.AlignJustify)

  return layout


group_instance = {
  "name":        None,
  "box_enabled": False,
  "box_name":    None,
  "layout":      None,
  "scrollable":  False,
  "checkable":   False,
  "added":       False,
  "items":       []
}

io_instance = {
  "name":  None,
  "class": "",
  "added": False,
  "config": ""
}


class ComplexParameter(pTypes.GroupParameter):
    def __init__(self, **opts):
        opts['type'] = 'bool'
        opts['value'] = True
        pTypes.GroupParameter.__init__(self, **opts)

        self.addChild({'name': 'A = 1/B', 'type': 'float', 'value': 7, 'suffix': 'Hz', 'siPrefix': True})
        self.addChild({'name': 'B = 1/A', 'type': 'float', 'value': 1/7., 'suffix': 's', 'siPrefix': True})
        self.a = self.param('A = 1/B')
        self.b = self.param('B = 1/A')
        self.a.sigValueChanged.connect(self.aChanged)
        self.b.sigValueChanged.connect(self.bChanged)

    def aChanged(self):
        self.b.setValue(1.0 / self.a.value(), blockSignal=self.bChanged)

    def bChanged(self):
        self.a.setValue(1.0 / self.b.value(), blockSignal=self.aChanged)



class IOGrid(QtGui.QWidget):
  """
  @summary:
  """
  def __init__(self):
    super(IOGrid, self).__init__()
    # logging.basicConfig()
    self.logger = logging.getLogger("iogrid")
    self.io_widgets = []

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
    print type(obj)
    if isinstance(obj, PyQt4.QtGui.QSlider):
      self.p.param(instance["name"]).setValue(obj.value())
    else:
      self.p.param(instance["name"]).setValue(obj.text())


  def config_widget(self, config):
    self.layout = get_layout(config["layout"])
    self.setLayout(self.layout)
    self.groups = []

    self.p = Parameter.create(name='params', type='group')

    for c in config["groups"]:
      # gp = pTypes.GroupParameter(**c)
      # self.p.addChild(gp)
      if c["box_enabled"]:
        widget = QtGui.QGroupBox(c["box_name"])
        widget.setCheckable(c["checkable"])
      else:
        widget = QtGui.QWidget()

      layout = get_layout(c["layout"])
      widget.setLayout(layout)
      self.groups.append(layout)

      for io in c["items"]:
        layout.addWidget(
          make_funcs[io["class"]](
            io["config"],
            callback=self.generic_callback
          )
        )
        io["added"] = True
        # gp.addChild(io)
        self.p.addChild(io)

      if c["scrollable"]:
        scroll = QtGui.QScrollArea()
        scroll.setWidget(widget)
        scroll.setWidgetResizable(True)
        scroll.setAlignment(QtCore.Qt.AlignTop)
        scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        widget = scroll

      self.layout.addWidget(widget)
    return self.p

  def config_update(self, config):
    for idx, c in enumerate(config["groups"]):
      layout = self.groups[idx]
      for io in c["items"]:
        if io["added"]:
          continue
        layout.addWidget(
          make_funcs[io["class"]](
            io["config"]
          )
        )

        io["added"] = True