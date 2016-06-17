#!/usr/bin/env python
# -*- coding: utf-8 -*-;
"""Name of module.

Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
  Examples can be given using either the ``Example`` or ``Examples``
  sections. Sections support any reStructuredText formatting, including
  literal blocks::

      $ python components.py

Section breaks are created by simply resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
  module_level_variable (int): Module level variables may be documented in
    either the ``Attributes`` section of the module docstring, or in an
    inline docstring immediately following the variable.

    Either form is acceptable, but the two should not be mixed. Choose
    one convention to document module level variables and be consistent
    with it.

.. _Google Python Style Guide:
   http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

"""
# @Author: Mathew Cosgrove
# @Date:   2015-01-21 15:05:05
# @Last Modified by:   cosgrma
# @Last Modified time: 2016-02-03 03:02:50
# REF: http://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_google.html#example-google
# REF: http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

__author__ = "Mathew Cosgrove"
__copyright__ = ""
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Mathew Cosgrove"
__email__ = "cosgroma@gmail.com"
__status__ = "Development"

import logging

from copy import deepcopy
import numpy as np
from functools import partial

from PyQt4 import QtGui
from PyQt4 import QtCore
# from PyQt4 import Qt

# import pyqtgraph as pg
# from pyqtgraph.Qt import QtCore, QtGui

# import pyqtgraph.parametertree.parameterTypes as pTypes
# from pyqtgraph.parametertree import Parameter, ParameterTree, ParameterItem, registerParameterType

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


def set_common_policy(widget, policy=None):

  if policy == "V-Expand":
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
  else:
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)

  widget.setSizePolicy(sizePolicy)

  # widget.setSizePolicy(
  #     QtGui.QSizePolicy(
  #         QtGui.QSizePolicy.MinimumExpanding,
  #         QtGui.QSizePolicy.Preferred
  #     )
  # )
  # sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
  # sizePolicy.setHeightForWidth(widget.sizePolicy().hasHeightForWidth())
  # print type(widget)
  # bound = widget.sizeHint().boundedTo(QtCore.QSize(1000,1000))
  # size = widget.size()
  # expand = widget.sizeHint().expandedTo(widget.minimumSizeHint())
  # print "bound", bound, "size:", size, "expand", expand
  # print bound, widget.minimumSize()
  # widget.resize(widget.minimumSize())
  # if isinstance(widget, PyQt4.QtGui.QPushButton):
  # if bound.isValid() and
  # QtCore.QSize.boundedTo(widget.sizeHint()).height()
  # qsize = QtCore.QSize()
  # if qsize.boundedTo(widget.sizeHint()).height() < 50:
  #   widget.setMaximumHeight(50)


def make_label(config, callback=None):
  instance = deepcopy(label_defaults)
  instance.update(config)
  label = QtGui.QLabel(instance["label"])

  return label


def add_label(widget, label, position="left", policy=None):
  container = QtGui.QWidget()
  set_common_policy(container)

  label = QtGui.QLabel(label)
  set_common_policy(label)

  label.setAlignment(QtCore.Qt.AlignCenter)

  if position == "above":
    layout = QtGui.QVBoxLayout()
    layout.addWidget(label)
    layout.addWidget(widget)
  elif position == "below":
    layout = QtGui.QVBoxLayout()
    layout.addWidget(widget)
    layout.addWidget(label)
  else:
    layout = QtGui.QHBoxLayout()
    layout.addWidget(label)
    layout.addWidget(widget)

  container.setLayout(layout)
  return container

############################################

############################################
# Buttons

button_defaults = {
    "name": None,
    "qtype": "button",
    'type': 'bool',
    "label": "",
    "clicked": None,
    "enabled": False,
    "args": None,
    "tool-tip": None
}


def make_button(config, callback=None):
  instance = deepcopy(button_defaults)
  instance.update(config)

  if instance["qtype"] == "radio":
    button = QtGui.QRadioButton(instance["label"])
  elif instance["qtype"] == "check":
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
  else:
    button.clicked.connect(partial(callback, button, instance))
  set_common_policy(button)
  return button

############################################

############################################
# Buttons
edit_defaults = {
    "name": None,
    "qtype": "edit",
    "type": "text",
    "label": None,
    "position": "left",
    "default": "",
    "min": 0,
    "max": 100,
    "editingFinished": None,
    "args": None,
    "tool-tip": None,
    "read-only": False,
    "use-callback": True
}


def make_edit(config, callback=None):
  instance = deepcopy(edit_defaults)
  instance.update(config)
  signal = None
  size_policy = None
  if instance["qtype"] == "datetime":
    edit = QtGui.QDateTimeEdit()
    signal = edit.dateTimeChanged
  elif instance["qtype"] == "spin":
    edit = QtGui.QSpinBox()
    edit.setMinimum(instance['min'])
    edit.setMaximum(instance['max'])
    signal = edit.valueChanged
  elif instance["qtype"] == "window":
    edit = QtGui.QPlainTextEdit()
    edit.setMinimumSize(QtCore.QSize(270, 200))
    edit.setReadOnly(True)
    signal = None
    size_policy = "V-Expand"
  else:
    edit = QtGui.QLineEdit(str(instance["default"]))
    signal = edit.textEdited
    if instance["type"] == "int":
      edit.setValidator(QtGui.QIntValidator(edit))
    elif instance["type"] == "float":
      edit.setValidator(QtGui.QDoubleValidator(edit))

  if instance["editingFinished"] is not None:
    edit.textEdited.connect(
        partial(
            instance["editingFinished"],
            [edit] + instance["args"]
        )
    )
  elif signal is not None:
    signal.connect(partial(callback, edit, instance))

  if instance["use-callback"]:
    callback(edit, instance)
  # edit.cursorPositionChanged.connect(partial(callback, edit, instance))

  if instance["label"] is not None:
    edit = add_label(edit, instance["label"], position=instance["position"])

  if instance["tool-tip"] is not None:
    edit.setToolTip(instance["tool-tip"])
    edit.setStatusTip(instance["tool-tip"])

  set_common_policy(edit, policy=size_policy)

  return edit

############################################
# Sliders

slider_defaults = {
    "name": None,
    "type": "int",
    "qtype": "slider",
    "label": "",
    "position": "above",
    "range": [0, 100],
    "orientation": "h",
    "policy": None,
    "display": False,
    "valueChanged": None,
    "args": [None]
}


def make_slider(config, callback=None):
  def display_slider_value(slider, display, user_callback, instance):
    units = ""
    if user_callback is not None:
      user_callback(slider, instance)
    display.setText("%s" % (str(slider.value()) + " " + units))

  instance = deepcopy(slider_defaults)
  instance.update(config)

  if instance["qtype"] == "scroll":
    slider = QtGui.QScrollBar(o_map[instance["orientation"]])
  elif instance["qtype"] == "dial":
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
            callback,
            instance
        )
    )

    container = QtGui.QWidget()

    if instance["orientation"] == "h":
      layout = QtGui.QHBoxLayout()

      # display.setMaximumSize(40, 30)

      display.setSizePolicy(
          QtGui.QSizePolicy(
              QtGui.QSizePolicy.MinimumExpanding,
              QtGui.QSizePolicy.Minimum
          )
      )

      layout.addWidget(display)
      layout.addWidget(slider)

    elif instance["orientation"] == "v":

      # display.setMinimumSize(70, 30)
      slider.setSizePolicy(
          QtGui.QSizePolicy(
              QtGui.QSizePolicy.MinimumExpanding,
              QtGui.QSizePolicy.Minimum
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
    container = add_label(
        container,
        instance["label"],
        position=instance["position"],
        policy=instance["policy"])

  set_common_policy(container)
  return container

############################################

############################################
# Combo

combo_defaults = {
    "name": None,
    "type": "text",
    "label": "combobox",
    "items": [],
    "maxVisible": 10,
    "activated": None,
    "position": "above",
    "policy": None,
    "indexChanged": None,
    "args": None
}


def make_combo(config, callback=None):
  instance = deepcopy(combo_defaults)
  instance.update(config)
  combo = QtGui.QComboBox()
  # combo.maxVisibleItems(instance["maxVisible"])
  combo.addItems(instance["items"])

  if callback is not None:
    combo.currentIndexChanged.connect(partial(callback, combo, instance))

  label = QtGui.QLabel(instance["label"])
  if instance["label"] is not None:
    combo = add_label(combo,
                      instance["label"],
                      position=instance["position"],
                      policy=instance["policy"])
  else:
    label.setBuddy(combo)

  set_common_policy(combo)

  return combo
  # styleComboBox.activated[str].connect(self.changeStyle)

table_defaults = {
    "name": None,
    "label": "table",
    "headers": [],
    "items": [],
    "args": None
}


def make_table(config, callback=None):
  instance = deepcopy(table_defaults)
  instance.update(config)
  table = QtGui.QTableWidget(0, len(instance["headers"]))
  # table.insertRow(1)
  # table.setAlignment(QtCore.Qt.AlignCenter)
  table.setHorizontalHeaderLabels(instance["headers"])

  header = table.horizontalHeader()
  vertical = table.verticalHeader()
  # header.setStretchLastSection(True)
  # header.setResizeMode(QtGui.QHeaderView.ResizeToContents)
  header.setResizeMode(QtGui.QHeaderView.Stretch)
  # vertical.setResizeMode(QtGui.QHeaderView.Fixed)
  header.setCascadingSectionResizes(True)
  # vertical.setCascadingSectionResizes(True)
# QHeaderView.resizeSections (self, ResizeMode mode)
  return table

widget_defaults = {
    "name": None,
    "label": "table"
}


def make_widget(config, callback=None):
  instance = deepcopy(widget_defaults)
  instance.update(config)

  widget = QtGui.QWidget()
  set_common_policy(widget)
  return widget


make_funcs = {
    "label": make_label,
    "button": make_button,
    "edit": make_edit,
    "slider": make_slider,
    "combo": make_combo,
    "table": make_table,
    "widget": make_widget
}
