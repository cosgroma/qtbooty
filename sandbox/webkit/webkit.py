#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-12-10 01:59:58
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2014-12-10 03:00:54

import os
import sys

# from PyQt4 import QtWebKit
from PySide import QtCore, QtGui, QtWebKit

#Should be swapped with a read of a template
html = '''
<!DOCTYPE html>
<html>
<head>
<script type="text/javascript" src="js/d3.min.js"></script>
<script type="text/javascript" src="js/corr_w_scatter.js"></script>
</head>
<body>
    <div id="viz"></div>
    <script type="text/javascript">
    var sampleSVG = d3.select("#viz")
        .append("svg")
        .attr("width", 100)
        .attr("height", 100);
    sampleSVG.append("circle")
        .style("stroke", "gray")
        .style("fill", "white")
        .attr("r", 40)
        .attr("cx", 50)
        .attr("cy", 50)
        .on("mouseover", function(){d3.select(this).style("fill", "aliceblue");})
        .on("mouseout", function(){d3.select(this).style("fill", "white");});
    </script>
</body>
</html>
   '''

html2 = '''
<!DOCTYPE html>
<html>

<head>
  <script type="text/javascript" src="d3/d3.min.js"></script>
</head>

<body>

<div id="viz"></div>
  <script type="text/javascript">

  var data = [1, 1, 2, 3, 5, 8, 13, 21];

  var width = 960,
      height = 500,
      radius = height / 2 - 10;

  var arc = d3.svg.arc()
      .innerRadius(radius - 40)
      .outerRadius(radius)
      .cornerRadius(20);

  var pie = d3.layout.pie()
      .padAngle(.02);

  var color = d3.scale.category10();

  var svg = d3.select("body").append("svg")
      .attr("width", width)
      .attr("height", height)
    .append("g")
      .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

  svg.selectAll("path")
      .data(pie(data))
    .enter().append("path")
      .style("fill", function(d, i) { return color(i); })
      .attr("d", arc);

  </script>

</body>

</html>
'''
class WebView(QtGui.QWidget):
  def __init__(self, name=None, controller=False, interval=1000, maxlen=1000,  ylim=[-1 , 1]):
    super(WebView, self).__init__()

    self.view = QtWebKit.QWebView(self)

    self.view.settings().setAttribute(QtWebKit.QWebSettings.LocalContentCanAccessRemoteUrls, True)
    self.view.settings().setAttribute(QtWebKit.QWebSettings.PluginsEnabled, True)
    # self.view.settings().setAttribute(QtWebKit.QWebSettings.WebAttribute.DeveloperExtrasEnabled, True)
    self.view.settings().setAttribute(QtWebKit.QWebSettings.PrivateBrowsingEnabled, True)
    self.view.setHtml(html2, baseUrl=QtCore.QUrl().fromLocalFile('/Users/cosgroma/workspace/libs/python/modules/QtBooty/webkit/'))

    # self.view.load(QtCore.QUrl('http://www.google.com/ncr'))


if __name__ == "__main__":
  # Create the App
  import sys
  app = QtGui.QApplication(sys.argv)
  web_view = WebView()
  web_view.show()
  sys.exit(app.exec_())