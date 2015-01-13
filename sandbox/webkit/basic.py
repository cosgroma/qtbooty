import os
import sys

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *
from PySide import QtWebKit

#Should be swapped with a read of a template
html = '''
<!DOCTYPE html>
<html>
<head>
<script type="text/javascript" src="js/d3.min.js"></script>
<link rel=stylesheet type="text/css" href="corr_w_scatter.css">
</head>
<body>
    <div id="plot"></div>
    <script type="text/javascript" src="js/corr_w_scatter.js"></script>

</body>
</html>
   '''

def main():
    basepath = os.path.dirname(os.path.abspath(__file__))
    print basepath
    app = QApplication(sys.argv)
    win = QWebView()

    win.setWindowTitle('D3 in Qt Test')
    layout = QVBoxLayout()
    win.setLayout(layout)

    view = QWebView()
    view.settings().setAttribute(QWebSettings.LocalContentCanAccessRemoteUrls, True)
    view.settings().setAttribute(QtWebKit.QWebSettings.PluginsEnabled, True)
    view.settings().setAttribute(QtWebKit.QWebSettings.WebAttribute.DeveloperExtrasEnabled, True)
    view.settings().setAttribute(QtWebKit.QWebSettings.PrivateBrowsingEnabled, True)
    view.setHtml(html, baseUrl=QUrl().fromLocalFile('/Users/jay/github/qwebviewtesting/'))

    # A button to call our JavaScript
    #button = QPushButton('Set Full Name')

    # Interact with the HTML page by calling the completeAndReturnName
    # function; print its return value to the console
    #def complete_name():
        #frame = view.page().mainFrame()
        #print frame.evaluateJavaScript('completeAndReturnName();')

    # Connect 'complete_name' to the button's 'clicked' signal
    #button.clicked.connect(complete_name)

    # Add the QWebView and button to the layout
    layout.addWidget(view)
    #layout.addWidget(button)

    # Show the window and run the app
    win.show()
    app.exec_()

if __name__ == '__main__':
    main()
