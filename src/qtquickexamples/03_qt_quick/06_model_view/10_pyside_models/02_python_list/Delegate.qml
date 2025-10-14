import QtQuick
import QtQuick.Controls
import QtQuick.Layouts    

Rectangle {

    id: root
    required property var modelData
    required property int index
    
    width: ListView.view.width
    height: 40
    
    color: "transparent"
    border.color: "lightgrey"
    border.width: 1

    Label {
        anchors.fill: parent
        anchors.margins: 8
        verticalAlignment: Text.AlignVCenter
        text: root.modelData
    }

    MouseArea {
        id: mouse
        anchors.fill: parent
        onClicked: (mouse) => {
            root.ListView.view.currentIndex = root.index
        }
    }
}