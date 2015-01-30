
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-12-05 22:26:11
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2015-01-29 16:41:12

from PyQt4 import QtGui, QtCore, Qt
from PyQt4.QtCore import pyqtSignal, pyqtSlot
from copy import deepcopy
import numpy as np

from functools import partial

import logging

o_map = {"h": QtCore.Qt.Horizontal, "v": QtCore.Qt.Vertical}


#    ______  _____  _____  _____  _____     ______   ________  _______     ______
#   |_   _ \|_   _||_   _||_   _||_   _|   |_   _ `.|_   __  ||_   __ \  .' ____ \
#     | |_) | | |    | |    | |    | |       | | `. \ | |_ \_|  | |__) | | (___ \_|
#     |  __'. | '    ' |    | |    | |   _   | |  | | |  _| _   |  __ /   _.____`.
#    _| |__) | \ \__/ /    _| |_  _| |__/ | _| |_.' /_| |__/ | _| |  \ \_| \____) |
#   |_______/   `.__.'    |_____||________||______.'|________||____| |___|\______.'
#


############################################
# Labels

label_defaults = {"label": ""}

def make_label(config):
  instance = deepcopy(label_defaults)
  instance.update(config)
  label = QtGui.QLabel(instance["label"])
  return label

############################################

############################################
# Buttons

button_defaults = {
  "type":    "default",
  "label":   "",
  "clicked": None,
  "enabled": False,
  "args":    None
}

def make_button(config):
  instance = deepcopy(button_defaults)
  instance.update(config)

  if instance["type"] == "radio":
    button = QtGui.QRadioButton(instance["label"])
  elif instance["type"] == "check":
    button = QtGui.QCheckBox(instance["label"])
  else:
    button = QtGui.QPushButton(instance["label"])

  button.setChecked(instance["enabled"])

  if instance["clicked"] is not None:
    button.clicked.connect(
      partial(
        instance["clicked"],
        [button] + instance["args"]
      )
    )
  return button

############################################

############################################
# Buttons
edit_defaults = {
  "type":            "default",
  "label":           None,
  "position":        "left",
  "default":         None,
  "editingFinished": None,
  "args":            None
}

def make_edit(config):
  instance = deepcopy(edit_defaults)
  instance.update(config)

  if instance["type"] == "datetime":
    edit = QtGui.QDateTimeEdit()
  elif instance["type"] == "spin":
    edit = QtGui.QSpinBox()
  else:
    edit = QtGui.QLineEdit(instance["default"])

  if instance["editingFinished"] is not None:
    edit.textEdited.connect(
      partial(
        instance["editingFinished"],
        [edit] + instance["args"]
      )
    )

  if instance["label"] is not None:
    return add_label(edit, instance["label"], position=instance["position"])

  return edit

############################################
# Sliders

slider_defaults = {
  "type":         "default",
  "label":        "",
  "position":     "above",
  "range":        [0, 100],
  "orientation":  "h",
  "policy":       None,
  "display":      False,
  "valueChanged": None,
  "args":         [None]
}


def make_slider(config):
  def display_slider_value(slider, display, user_callback, args):
    units = ""
    if user_callback is not None:
      user_callback([slider] + args)
      units = args[0]
    display.setText("%s" % (str(slider.value()) + " " + units))

  instance = deepcopy(slider_defaults)
  instance.update(config)

  if instance["type"] == "scroll":
    slider = QtGui.QScrollBar(o_map[instance["orientation"]])
  elif instance["type"] == "dial":
    slider = QtGui.QDial()
    slider.setNotchesVisible(True)
  else:
    slider = QtGui.QSlider(o_map[instance["orientation"]])

  slider.setRange(instance["range"][0], instance["range"][1])
  slider.setValue(0)

  if instance["display"]:
    display = QtGui.QLineEdit("%3s" % "0")
    display.setAlignment(QtCore.Qt.AlignCenter)
    slider.valueChanged.connect(
      partial(
        display_slider_value,
        slider,
        display,
        instance["valueChanged"],
        instance["args"]
      )
    )

    container = QtGui.QWidget()

    # container.setSizePolicy(
    #   QtGui.QSizePolicy(
    #     QtGui.QSizePolicy.Maximum,
    #     QtGui.QSizePolicy.Maximum
    #   )
    # )

    if instance["orientation"] == "h":
      layout = QtGui.QHBoxLayout()

      display.setMinimumSize(40, 30)

      display.setSizePolicy(
        QtGui.QSizePolicy(
          QtGui.QSizePolicy.Maximum,
          QtGui.QSizePolicy.Minimum
        )
      )
      # layout = QtGui.QGridLayout()
      layout.addWidget(display)
      layout.addWidget(slider)



      # layout.addWidget(slider)
      # layout.addWidget(display)
    elif instance["orientation"] == "v":

      display.setMinimumSize(70, 30)
      slider.setSizePolicy(
        QtGui.QSizePolicy(
          QtGui.QSizePolicy.Expanding,
          QtGui.QSizePolicy.Expanding
        )
      )
      # layout = QtGui.QVBoxLayout()
      layout = QtGui.QGridLayout()
      layout.addWidget(display, 0, 0, 1, 1)
      layout.addWidget(slider, 1, 0, 8, 1)

    # layout.setAlignment(QtCore.Qt.AlignCenter)

    container.setLayout(layout)
  else:
    container = slider

  if instance["label"] is not None:
    return add_label(container,
                     instance["label"],
                     position=instance["position"],
                     policy=instance["policy"])

  return container

############################################

############################################
# Combo

combo_defaults = {
  "label":           "combobox",
  "items":           [],
  "maxVisible":      10,
  "activated":       None,
  "indexChanged":    None,
  "args":            None
}

# activated (int)
# activated (const QString&)
# currentIndexChanged (int)
# currentIndexChanged (const QString&)
# editTextChanged (const QString&)
# highlighted (int)
# highlighted (const QString&)

def make_combo(config):
  instance = deepcopy(combo_defaults)
  instance.update(config)
  combo = QtGui.QComboBox()
  combo.setSizePolicy(
    QtGui.QSizePolicy(
      QtGui.QSizePolicy.Expanding,
      QtGui.QSizePolicy.Maximum
    )
  )
  # combo.maxVisibleItems(instance["maxVisible"])
  combo.addItems(instance["items"])
  label = QtGui.QLabel(instance["label"])
  label.setBuddy(combo)
  return combo
  # styleComboBox.activated[str].connect(self.changeStyle)

table_defaults = {
  "label": "table",
  "headers": [],
  "items": [],
  "args": None
}

def make_table(config):
  instance = deepcopy(table_defaults)
  instance.update(config)
  table = QtGui.QTableWidget()
  #table.insertRow(1)
  table.setHorizontalHeaderLabels(instance["headers"])
  for idx, item in enumerate(instance["items"]):
    print idx, item

  # self.resizeColumnsToContents()
  # self.resizeRowsToContents()
  # combo.setSizePolicy(
  #   QtGui.QSizePolicy(
  #     QtGui.QSizePolicy.Expanding,
  #     QtGui.QSizePolicy.Maximum
  #   )
  # )
  # combo.maxVisibleItems(instance["maxVisible"])
  # combo.addItems(instance["items"])
  # label = QtGui.QLabel(instance["label"])
  # label.setBuddy(combo)
  return table
  # styleComboBox.activated[str].connect(self.changeStyle)
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

def add_label(widget, label, position="left", policy=None):
  container = QtGui.QWidget()

  if policy is not None:
    container.setSizePolicy(
      QtGui.QSizePolicy(
        QtGui.QSizePolicy.Maximum,
        QtGui.QSizePolicy.Expanding
      )
    )

  label = QtGui.QLabel(label)
  label.setSizePolicy(
    QtGui.QSizePolicy(
      QtGui.QSizePolicy.Expanding,
      QtGui.QSizePolicy.Maximum
    )
  )

  label.setAlignment(QtCore.Qt.AlignCenter)

  if position == "above":
    layout = QtGui.QVBoxLayout()
    layout.addWidget(label)
    layout.addWidget(widget)
    # layout.setAlignment(QtCore.Qt.AlignJustify)
  elif position == "below":
    layout = QtGui.QVBoxLayout()
    layout.addWidget(widget)
    layout.addWidget(label)
    # layout.setAlignment(QtCore.Qt.AlignVCenter)
  else:
    layout = QtGui.QHBoxLayout()
    layout.addWidget(label)
    layout.addWidget(widget)

  container.setLayout(layout)
  return container

make_funcs = {
  "label": make_label,
  "button": make_button,
  "edit": make_edit,
  "slider": make_slider,
  "combo": make_combo
 }

group_instance = {
  "box_enabled": False,
  "box_name":    None,
  "layout":      None,
  "scrollable":  False,
  "checkable":   False,
  "added":       False,
  "items":       []
}

io_instance = {
  "class": "",
  "added": False,
  "config": ""
}

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

  def config_widget(self, config):
    self.layout = get_layout(config["layout"])
    self.setLayout(self.layout)
    self.groups = []

    for c in config["groups"]:
      if c["box_enabled"]:
        widget = QtGui.QGroupBox(c["box_name"])
        widget.setCheckable(c["checkable"])
      else:
        widget = QtGui.QWidget()

      layout = get_layout(c["layout"])
      widget.setLayout(layout)
      self.groups.append(layout)

      for io in c["items"]:
        make_funcs[io["class"]](io["config"]))
        # if io["class"] == "label":
        #   layout.addWidget(make_label(io["config"]))
        # elif io["class"] == "button":
        #   layout.addWidget(make_button(io["config"]))
        # elif io["class"] == "edit":
        #   layout.addWidget(make_edit(io["config"]))
        # elif io["class"] == "slider":
        #   layout.addWidget(make_slider(io["config"]))
        # elif io["class"] == "combo":
        #   layout.addWidget(make_combo(io["config"]))

        io["added"] = True

      if c["scrollable"]:
        scroll = QtGui.QScrollArea()
        scroll.setWidget(widget)
        scroll.setWidgetResizable(True)
        scroll.setAlignment(QtCore.Qt.AlignTop)
        scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        widget = scroll

      self.layout.addWidget(widget)

  def config_update(self, config):
    for idx, c in enumerate(config["groups"]):
      layout = self.groups[idx]
      for io in c["items"]:
        if io["added"]:
          continue
        if io["class"] == "label":
          layout.addWidget(make_label(io["config"]))
        elif io["class"] == "button":
          layout.addWidget(make_button(io["config"]))
        elif io["class"] == "edit":
          layout.addWidget(make_edit(io["config"]))
        elif io["class"] == "slider":
          layout.addWidget(make_slider(io["config"]))
        elif io["class"] == "combo":
          layout.addWidget(make_combo(io["config"]))
        elif io["class"] == "table":
          layout.addWidget(make_combo(io["config"]))

        io["added"] = True