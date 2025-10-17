import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


Rectangle {
    
    id: root

    width: 40
    height: ListView.view.height
    color: ListView.isCurrentItem ? "#e3f2fd" : "transparent"
    border.color: ListView.isCurrentItem ? "#1976d2" : "lightgrey"
    border.width: 1
    
    Label {
        anchors.centerIn: parent
        text: modelData
        rotation: 270
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