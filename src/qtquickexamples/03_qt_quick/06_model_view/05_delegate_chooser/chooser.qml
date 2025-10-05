import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {

    visible: true
    width: listView.implicitWidth
    height: listView.implicitHeight
    title: "DelegateChooser"
    
    ListModel {

        id: listModel

        ListElement { type: "info"; message: "Build completed successfully" }
        ListElement { type: "warning"; message: "Unused variable 'temp'" }
        ListElement { type: "error"; message: "Null pointer dereference" }
        ListElement { type: "info"; message: "Connected to server" }
        ListElement { type: "warning"; message: "Deprecated API call" }
        ListElement { type: "error"; message: "File not found" }
        ListElement { type: "info"; message: "Cache updated" }
        ListElement { type: "warning"; message: "Unreachable code detected" }
        ListElement { type: "error"; message: "Division by zero" }
        ListElement { type: "info"; message: "Test suite passed" }
    }

    ListView {
    
        id: listView        
        anchors.fill: parent
        model: listModel
        
        implicitWidth: 300
        implicitHeight: count * 40
        
        focus: true
        highlightFollowsCurrentItem: true
        highlight: Rectangle {
            z: 100; color: "orange"; opacity: 0.2 }
        
        delegate: chooser
        
        DelegateChooser {
            id: chooser
            role: "type"
            DelegateChoice {roleValue: "info"; MyDelegate {
                text: model.message
                icon.source: "info.png"}}
            DelegateChoice {roleValue: "warning"; MyDelegate {
                text: model.message
                icon.source: "warning.png"}}
            DelegateChoice {roleValue: "error"; MyDelegate {
                text: model.message
                icon.source: "error.png"}}
        }
        
        ScrollBar.vertical: ScrollBar {}
        
        onCurrentIndexChanged: () => {
            console.log("Current index changed: " + currentIndex)
        }
    }
    
    component MyDelegate: ItemDelegate {
        
        id: root
        
        required property int index
        required property var model
        required property string type
        required property string message
    
        width: 300
        height: 40

        background: Rectangle {
            opacity: 0.2
            color: index % 2 === 0 ?
                "#f0f0f0" : "#dcdcdc"
        }

        MouseArea {
            anchors.fill: parent
            onClicked: {
                root.ListView.view.currentIndex = index
                console.log("Clicked: " +
                    "Current index: " + root.ListView.view.currentIndex +
                    " Type: " + model.type + " Message: " + model.message)
            }
        }
    }
}