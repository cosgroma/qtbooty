#!/usr/bin/env python
# -*- coding: utf-8 -*-;
"""Name of module.

Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
  Examples can be given using either the ``Example`` or ``Examples``
  sections. Sections support any reStructuredText formatting, including
  literal blocks::

      $ python freq_series.py

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
# @Date:   2015-01-10 16:22:17
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2015-02-07 07:19:04
# REF: http://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_google.html#example-google
# REF: http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

__author__ = "Mathew Cosgrove"
__copyright__ = ""
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Mathew Cosgrove"
__email__ = "cosgroma@gmail.com"
__status__ = "Development"


from QtBooty.graph import PointSeries

import numpy as np
import matplotlib
matplotlib.use('QT4Agg')
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import struct
import scipy
import scipy.fftpack
import pylab
import time
import pyfftw
from scipy import pi

import collections

spectrum_backend = "np"

class Spectrum(PointSeries):
  """docstring for Spectrum"""
  def __init__(self, sample_frequency, signal_length, numpoints, **kwargs):
    super(Spectrum, self).__init__(**kwargs)
    self.sample_frequency = sample_frequency
    self.numpoints = numpoints
    self.signal_length = signal_length
    if spectrum_backend == "pyfftw":
      self.get_fft = self._pyfftw
      self.signal = pyfftw.n_byte_align_empty((self.signal_length), 16, dtype=np.complex128)
      self.signal_ft = pyfftw.n_byte_align_empty((self.signal_length), 16, dtype=np.complex128)
      # Create an FFTW transforms which will execute the code FFT.
      self.signal_fft = pyfftw.FFTW(self.signal, self.signal_ft)
      self.freqs = np.linspace(0, self.sample_frequency/2, len(self.signal_ft))
    elif spectrum_backend == "np":
      self.get_fft = self._npfft
      self.freqs = np.linspace(0, self.sample_frequency/2, self.numpoints/2+1)

  def get_freqs(self):
    return self.freqs

  def _pyfftw(self, signal):
    self.signal[:] = signal
    self.signal_fft.execute()
    return self.freqs, 20*np.log10(np.abs(self.signal_ft))

  def _npfft(self, signal):
    return self.freqs, 20*np.log10(np.abs(np.fft.rfft(signal, n=self.numpoints)))

