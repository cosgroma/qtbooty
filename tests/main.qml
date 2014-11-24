import QtQuick 1.1
import myPyQtGraph 1.0

Rectangle {
    id : page
    width: 900
    height: 400
    color:  "#343434"

    PyQtGraph {
        id: angleGraphID
        anchors{
            top: parent.top
            left: parent.left
            topMargin: 50
            leftMargin: 50
        }
        width: 800
        height: 300
        //color: "#f5deb3"
    }
    MouseArea {
        anchors.fill: parent
        onClicked: aPieChart.clearChart()
    }

    Text {
        id: text_Heading
        anchors{
            top: parent.top
            left: parent.left
            topMargin: 20
            leftMargin: 50
        }
        text: qsTr("PyqtGraph QML Test")
        font.pixelSize: 12
    }
}
