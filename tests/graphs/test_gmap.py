#!/usr/bin/env python
# -*- coding: utf-8 -*-;
"""Name of module.

Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
  Examples can be given using either the ``Example`` or ``Examples``
  sections. Sections support any reStructuredText formatting, including
  literal blocks::

      $ python test_gmap.py

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
# @Date:   2015-10-28 03:07:56
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2016-06-16 23:52:10
# REF: http://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_google.html#example-google
# REF: http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

__author__ = "Mathew Cosgrove"
__copyright__ = ""
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Mathew Cosgrove"
__email__ = "cosgroma@gmail.com"
__status__ = "Development"

import sys
import os
sys.path.append(os.path.dirname(os.path.join(os.path.dirname(__file__), "../../qtbooty")))

import random
import logging
from qtbooty import App
from qtbooty import graph

try:
  import pyutils
  pyutils.setup_logging()
except:
  pass

logger = logging.getLogger()


def update():
  gmap.add_circle(34.17192, -118.59521, random.random() * 100)

app = App('config/app_config.json')
gmap = graph.GMap()
app.add_widget(gmap)
app.add_timer(1000, update)
app.run()
