import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


Rectangle {
    
    id: root
    
    required property int index
    required property var model
    
    required property string name
    required property int value

    width: 200
    height: 40
    color: index === ListView.view.currentIndex ?
        "transparent" :
            index % 2 === 0 ? "#f0f0f0" : "#dcdcdc" 
    
    RowLayout {
    
        anchors.fill: parent
        anchors.margins: 8
        
        Label { text: name }
        Label { text: value }
    }
    
    MouseArea {
        anchors.fill: parent
        onClicked: {
            root.ListView.view.currentIndex = index
            console.log("Clicked: " +
                "Current index: " + root.ListView.view.currentIndex +
                " Name: " + model.name + " Value: " + model.value)
        }
    }
}