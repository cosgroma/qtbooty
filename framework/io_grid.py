
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-12-05 22:26:11
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2014-12-10 01:34:55

from PyQt4 import QtGui, QtCore, Qt
from PyQt4.QtCore import pyqtSignal, pyqtSlot
from copy import deepcopy
import numpy as numpy

from functools import partial

import logging

group_instance = {"box_enabled": False,
                  "box_name":    None,
                  "layout":      None,
                  "items":       []}

io_instance = {"class": "", "config": ""}

label_defaults = {"label": ""}
button_defaults = {"type": "default", "label": "", "callback": None, "args": None}
edit_defaults = {"type": "default", "label": None, "default": None, "callback": None, "args": None}

slider_defaults = {"type": "default", "label": "", "range": [0, 100], "orientation": "h", "display": False, "callback": None, "args": None}
dial_defaults = {"label": "", "value": 0, "callback": None, "args": None}

o_map = {"h": QtCore.Qt.Horizontal, "v": QtCore.Qt.Vertical}

def get_layout(name):
  """
  @summary:
  @param name:
  @result:
  """
  if name == "h":
    return QtGui.QHBoxLayout()
  elif name == "v":
    return QtGui.QVBoxLayout()
  elif name == "g":
    return QtGui.QGridLayout()


def make_label(config):
  instance = deepcopy(label_defaults)
  instance.update(config)
  label = QtGui.QLabel(instance["label"])
  return label


def make_button(config):
  instance = deepcopy(button_defaults)
  instance.update(config)
  if instance["type"] == "radio":
    button = QtGui.QRadioButton(instance["label"])
  else:
    button = QtGui.QPushButton(instance["label"])
  if instance["callback"] is not None:
    button.clicked.connect(partial(instance["callback"], instance["args"]))
  return button

def add_label(widget, label, position="left"):
  container = QtGui.QWidget()

  if position == "above":
    layout = QtGui.QVBoxLayout()
    layout.addWidget(QtGui.QLabel(label))
    layout.addWidget(widget)
  elif position == "below":
    layout = QtGui.QVBoxLayout()
    layout.addWidget(widget)
    layout.addWidget(QtGui.QLabel(label))
  else:
    layout = QtGui.QHBoxLayout()
    layout.addWidget(QtGui.QLabel(label))
    layout.addWidget(widget)

  container.setLayout(layout)
  return container


def make_edit(config):
  instance = deepcopy(edit_defaults)
  instance.update(config)

  if instance["type"] == "datetime":
    edit = QtGui.QDateTimeEdit()
    # edit.setDateTime()
  elif instance["type"] == "spin":
    edit = QtGui.QSpinBox()
    # edit.setValue(instance["default"])
  else:
    edit = QtGui.QLineEdit(instance["default"])

  if instance["label"] is not None:
    edit = add_label(edit, instance["label"])

  return edit

def slider_value_callback(slider, display):
  print("slider value:", slider.value())
  display.setText(str(slider.value()))

def make_slider(config):
  instance = deepcopy(slider_defaults)
  instance.update(config)

  if instance["type"] == "scroll":
    slider = QtGui.QScrollBar(o_map[instance["orientation"]])
  else:
    slider = QtGui.QSlider(o_map[instance["orientation"]])

  slider.setRange(instance["range"][0], instance["range"][1])

  if instance["display"]:
    display = QtGui.QLabel("")
    container = QtGui.QWidget()
    layout = QtGui.QHBoxLayout()
    layout.addWidget(slider)
    layout.addWidget(display)
    container.setLayout(layout)
    slider.valueChanged.connect(partial(slider_value_callback, slider, display))
    if instance["label"] is not None:
      slider = add_label(container, instance["label"], position="above")
  else:
    slider = add_label(slider, instance["label"], position="above")

  return slider


def make_dial(config):
  instance = deepcopy(dial_defaults)
  instance.update(config)
  dial = QtGui.QDial()

  dial.setValue(instance["value"])
  dial.setNotchesVisible(True)

  if instance["label"] is not None:
    label = QtGui.QLabel(instance["label"])
    label.setBuddy(dial)
  return dial


def make_dropdown(config):
  pass


def make_combo(config):
  pass


class IOGrid(QtGui.QWidget):

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
    config = {"layout": "h"}
    # populated the default groups, check if well formed
    if not ngroups == len(nitems_arr):
      self.logger.error("nitems_arr length (%d) doest not match ngroups (%d)" % (ngroups, nitems_arr))
    config["groups"] = [deepcopy(group_instance) for i in range(ngroups)]
    # populated a set of default item configurations for each group
    for c, nitems in zip(config["groups"], nitems_arr):
      c["items"] = [deepcopy(io_instance) for n in range(0, nitems)]
    return config

  def config_widget(self, config):
    self.layout = get_layout(config["layout"])
    self.setLayout(self.layout)

    for c in config["groups"]:
      if c["box_enabled"]:
        widget = QtGui.QGroupBox(c["box_name"])
      else:
        widget = QtGui.QWidget()

      layout = get_layout(c["layout"])
      widget.setLayout(layout)

      for io in c["items"]:
        if io["class"] == "label":
          layout.addWidget(make_label(io["config"]))

        if io["class"] == "button":
          layout.addWidget(make_button(io["config"]))

        if io["class"] == "edit":
          layout.addWidget(make_edit(io["config"]))

        if io["class"] == "slider":
          layout.addWidget(make_slider(io["config"]))

      self.layout.addWidget(widget)

    # Check Box
    # Drop Down
    # Combo wheel
    pass


# self.app_load_button.clicked.connect(self.load_unload_app)
# Select Group bool and Layout type H, V, G
#
def test_callback(name):
  print("Button pressed: %s" % name)


if __name__ == '__main__':
  from QtBooty import App
  app = App()


  io_grid = IOGrid()
  config = io_grid.config_init(4, [1, 3, 2, 2])
  config["layout"] = "v"
  groups = config["groups"]

  groups[0]["box_enabled"] = False
  groups[0]["box_name"] = "class::label"
  groups[0]["layout"] = "h"

  # label_defaults = {"label": ""}
  groups[0]["items"] = [{
      "class": "label",
      "config": {
        "label": "regular label"
        }
    }
  ]

  groups[1]["box_enabled"] = True
  groups[1]["box_name"] = "class::edit"
  groups[1]["layout"] = "h"

  # edit_defaults = {"type": "default", "label": None, "default": "", "callback": None, "args": None}
  groups[1]["items"] = [{
      "class": "edit",
      "config": {
        "label": "normal"
        }
    },{
      "class": "edit",
      "config": {
        "type": "datetime",
        "label": "date time"
        }
    },{
      "class": "edit",
      "config": {
        "type": "spin",
        "label": "spin"
        }
      }
  ]

  # button_defaults = {"type": "default", "label": "", "callback": None, "args": None}
  groups[2]["box_enabled"] = True
  groups[2]["box_name"] = "class::button"
  groups[2]["layout"] = "h"

  groups[2]["items"] = [{
      "class": "button",
      "config": {
        "label": "button1",
        "callback": test_callback,
        "args":"normal_button"
        }
    },{
      "class": "button",
      "config": {
        "type": "radio",
        "label": "radio button",
        "callback": test_callback,
        "args":"radio_button"
        }
    }
  ]

  # slider_defaults = {"type": "default", "label": "", "range": 100, "orientation": "h", "display": False, "callback": None, "args": None}

  groups[3]["box_enabled"] = True
  groups[3]["box_name"] = "class::slider"
  groups[3]["layout"] = "v"

  groups[3]["items"] = [{
      "class": "slider",
      "config": {
        "label": "slider",
        "display": True
        }
    },{
      "class": "slider",
      "config": {
        "type": "scroll",
        "label": "scroll"
        }
    }
  ]

  # scroll_defaults = {"label": "", "value": 0, "orientation": "h", "callback": None, "args": None}


  # dial_defaults = {"label": "", "value": 0, "callback": None, "args": None}


  io_grid.config_widget(config)

  app.add_widget(io_grid)

  app.run()