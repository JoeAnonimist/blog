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
    
    required property int index
    required property var model
    required property string value

    TextField {

        id: editor

        anchors.fill: parent
        anchors.margins: 8
        text: value
        
        onAccepted: () => {
            
            root.ListView.view.model.setProperty(index, "value", text)
            
            var model = root.ListView.view.model
            console.log(model)
            console.log(index)
            for (var i = 0; i < model.count; i++) {
                console.log(model.get(i).value)
            }
        }
        
        Keys.onEscapePressed: () => {
            text = value
        }
    }

    Connections {
        target: root.ListView.view
        function onCurrentIndexChanged() {
            if (root.ListView.isCurrentItem) {
                editor.forceActiveFocus()
            }
        }
    }
}