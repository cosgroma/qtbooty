#!/usr/bin/env python
# -*- coding: utf-8 -*-;
"""Name of module.

Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
  Examples can be given using either the ``Example`` or ``Examples``
  sections. Sections support any reStructuredText formatting, including
  literal blocks::

      $ python docs_widget.py

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
# @Date:   2015-09-04 03:23:23
# @Last Modified by:   cosgrma
# @Last Modified time: 2016-02-17 05:01:23


__author__ = "Mathew Cosgrove"
__copyright__ = ""
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Mathew Cosgrove"
__email__ = "cosgroma@gmail.com"
__status__ = "Development"

from PyQt4 import QtCore, QtGui, QtWebKit, QtNetwork


class DocsWidget(QtGui.QWidget):

  """docstring for DocsWidget"""

  def __init__(self):
    super(DocsWidget, self).__init__()

    self.web = QtWebKit.QWebView(self)
    self.layout = QtGui.QVBoxLayout(self)
    self.layout.addWidget(self.web)
    self.web.page().mainFrame().setScrollBarPolicy(QtCore.Qt.Vertical, QtCore.Qt.ScrollBarAsNeeded)

  def load_page(self, page=None):
    if page is None:
      page = 'C:\\cygwin64\\home\\cosgrma\\workspace\\sandbox\\sphix-test\\_build\\html\\index.html'

    self.web.load(QtCore.QUrl.fromLocalFile(QtCore.QFileInfo(page).absoluteFilePath()))

if __name__ == '__main__':
  import random
  import logging
  import pyutils
  pyutils.setup_logging()
  logger = logging.getLogger()
  from QtBooty import App
  app = App('config/bad_app_config.json')
  docswidget = DocsWidget()
  app.add_widget(docswidget)
  docswidget.load_page('C:\\cygwin64\\home\\cosgrma\\workspace\\sandbox\\sphix-test\\_build\\html\\index.html')
  app.run()
