import QtQuick
import QtQuick.Controls
import QtQuick.Layouts    

Rectangle {

    id: root
    required property string value
    required property int index
    
    property bool editing: false
    
    width: ListView.view.width
    height: 40
    
    color: "transparent"
    border.color: "lightgrey"
    border.width: 1

    Label {
        anchors.fill: parent
        anchors.margins: 8
        verticalAlignment: Text.AlignVCenter
        text: root.value
        visible: !root.editing
    }

    TextField {
        anchors.fill: parent
        anchors.margins: 8
        text: root.value
        focus: root.editing
        visible: root.editing

        onActiveFocusChanged: () => {
            if (!activeFocus) root.editing = false
        }
        
        Keys.onReturnPressed: () => {
            root.ListView.view.model.setProperty(index, "value", text)
            root.editing = false
            mouse.forceActiveFocus()
        }
        
        Keys.onEnterPressed: () => {
            root.ListView.view.model.setProperty(index, "value", text)
            root.editing = false
            mouse.forceActiveFocus()
        }
        
        Keys.onEscapePressed: () => {
            root.editing = false
            text = root.value
            mouse.forceActiveFocus()
        }
    }
    
    MouseArea {
        id: mouse
        anchors.fill: parent
        enabled: !root.editing
        onClicked: (mouse) => {
            root.ListView.view.currentIndex = root.index
        }
        onDoubleClicked: () => {
            root.editing = true
        }
    }

    Keys.onEnterPressed: () => { root.editing = true }
    Keys.onReturnPressed: () => { root.editing = true }
}