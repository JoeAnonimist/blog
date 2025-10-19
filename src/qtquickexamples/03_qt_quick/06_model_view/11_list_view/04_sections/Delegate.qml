import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


Rectangle {
    
    id: root
    
    required property int index
    required property var model

    required property string value

    width: ListView.view.width
    height: 40
    color: ListView.isCurrentItem ? "#e3f2fd" : "transparent"
    border.color: ListView.isCurrentItem ? "#1976d2" : "lightgrey"
    border.width: 1
    
    RowLayout {
    
        anchors.fill: parent
        anchors.margins: 8

        Label { text: value }
    }
    
    MouseArea {
        anchors.fill: parent
        onClicked: {
            root.ListView.view.currentIndex = index
            console.log("Clicked: " +
                "Current index: " + root.ListView.view.currentIndex +
                " Value: " + model.value)
        }
    }
}