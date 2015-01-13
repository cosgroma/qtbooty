#!/usr/bin/env python
# -*- coding: utf-8 -*-;
"""Name of module.

Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
  Examples can be given using either the ``Example`` or ``Examples``
  sections. Sections support any reStructuredText formatting, including
  literal blocks::

      $ python polar_test.py

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
# @Date:   2014-12-30 06:57:46
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2015-01-10 01:16:07
# REF: http://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_google.html#example-google
# REF: http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

__author__ = "Mathew Cosgrove"
__copyright__ = ""
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Mathew Cosgrove"
__email__ = "mathew.cosgrove@ngc.com"
__status__ = "Development"

import sys
from QtBooty import App
from QtBooty.graphs import Polar
import numpy as np

app = App('../config/app_config.json')

polar = Polar()
polar.set_lims(0, (0, 90))
# polar.set_xlabel('degrees')
# polar.set_ylabel('dB')

polar.add_line('1', 'r')
polar.add_line('2', 'b')

def get_mag(ang):
  # Define magnitude
  angRad = np.pi * ang / 180.0
  mag = 10 * np.log10(np.abs(np.sin(10 * angRad) / angRad)) + angRad
  return mag

ang = 0
ang_delta = 5

def update_polar():
  global ang
  ang += ang_delta
  mag = get_mag(ang)
  polar.add_point('1', (ang, mag))
  polar.add_point('2', (ang + 10, mag))

update_polar_interval = 5

app.add_widget(polar)
app.add_timer(update_polar_interval, update_polar)
polar.set_interval(update_polar_interval*2)
polar.start()
app.run()
