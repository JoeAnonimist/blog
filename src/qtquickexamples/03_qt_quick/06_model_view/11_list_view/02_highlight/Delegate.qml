import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


Rectangle {
    
    id: root

    width: ListView.view.width
    height: 40
    color: "transparent"
    border.color: "lightgrey"
    border.width: 1
    
    required property int value
    required property int index
    property int barCount: value

    Label {
        text: value
        anchors.centerIn: parent
    }
    
    MouseArea {
        anchors.fill: parent
        onClicked: {
            root.ListView.view.currentIndex = index
            console.log("Clicked: " +
                "Current index: " + root.ListView.view.currentIndex +
                " Value: " + value)
        }
    }
}