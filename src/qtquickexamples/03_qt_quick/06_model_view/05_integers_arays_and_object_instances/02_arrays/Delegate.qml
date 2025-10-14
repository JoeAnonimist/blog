import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


Rectangle {
    
    id: root

    width: ListView.view.width
    height: 40
    color: ListView.isCurrentItem ? "#e3f2fd" : "transparent"
    border.color: ListView.isCurrentItem ? "#1976d2" : "lightgrey"
    border.width: 1
    
    required property string modelData
    required property int index
    
    RowLayout {
    
        anchors.fill: parent
        anchors.margins: 8

        Label {
            text: modelData
            Layout.fillWidth: true
            horizontalAlignment: Text.AlignHCenter
        }
    }
    
    MouseArea {
        anchors.fill: parent
        onClicked: {
            root.ListView.view.currentIndex = index
            console.log("modelData: " + modelData)
            root.ListView.view.model[index] = "new value"
            // root.ListView.view.model.length = 3
        }
    }
}