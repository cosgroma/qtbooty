#!/usr/bin/env python
# -*- coding: utf-8 -*-;
"""Name of module.

Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
Examples can be given using either the ``Example`` or ``Examples``
sections. Sections support any reStructuredText formatting, including
literal blocks::

$ python undefined

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
# @Date:   2015-01-22 23:13:40
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2015-01-22 23:21:22
# REF: http://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_google.html#example-google
# REF: http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

__author__ = "Mathew Cosgrove"
__copyright__ = ""
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Mathew Cosgrove"
__email__ = "cosgroma@gmail.com"
__status__ = "Development"

from collections import deque

import numpy as np
data = deque(maxlen=10)

# t = np.linspace(0, 1, 1, endpoint=False)
t = np.array([1])
append_len = 1
only_time = False
for _ in range(append_len):
  if only_time:
    npm = np.matrix([t])
  else:
    r1 = np.random.randn(len(t))
    r2 = np.random.randn(len(t))
    npm = np.matrix([t, r1, r2])
  t += 1
  data.append(npm)

# Dump deque into matrix
dmat = np.concatenate(data, axis=1)
print dmat[:,]
print("R type (%d): %s\n", type(r1), r1.shape)
print("t type (%d): %s\n", type(t), t.shape)


