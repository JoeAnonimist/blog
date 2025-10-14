import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {

    visible: true
    width: listView.implicitWidth
    height: listView.implicitHeight
    title: "DelegateChooser Demo"
    
    ListModel {
    
        id: listModel
    
        ListElement { type: "info"; message: "Build completed successfully" }
        ListElement { type: "warning"; message: "Unused variable 'temp'"; lineno: 143 }
        ListElement { type: "error"; message: "Null pointer dereference"; severity: 4 }
        ListElement { type: "info"; message: "Connected to server" }
        ListElement { type: "warning"; message: "Deprecated API call"; lineno: 58 }
        ListElement { type: "error"; message: "File not found"; severity: 2 }
        ListElement { type: "info"; message: "Cache updated" }
        ListElement { type: "warning"; message: "Unreachable code detected"; lineno: 179 }
        ListElement { type: "error"; message: "Division by zero"; severity: 5 }
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
        highlight: Rectangle { color: "orange"; opacity: 0.2 }
        
        delegate: chooser
        
        DelegateChooser {
            id: chooser
            role: "type"
            DelegateChoice {roleValue: "info"; InfoDelegate { }}
            DelegateChoice {roleValue: "warning"; WarningDelegate { }}
            DelegateChoice {roleValue: "error"; ErrorDelegate { }}
        }
        
        ScrollBar.vertical: ScrollBar {}
        
        onCurrentIndexChanged: () => {
            console.log("Current index changed: " + currentIndex)
        }
    }
    
    component MyCodeDelegate: ItemDelegate {
        
        id: root
        
        required property int index
        required property string type
        required property string message
    
        width: 300
        height: 40
        
        text: message

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
                    " Type: " + type + " Message: " + message)
            }
        }
    }
    
    component InfoDelegate: MyCodeDelegate {
        icon.source: "info.png"
    }
    
    component ErrorDelegate: MyCodeDelegate {

        icon.source: "error.png"
        required property int severity
        
        Row {
            anchors.right: contentItem.right
            anchors.rightMargin: 6
            anchors.verticalCenter: parent.verticalCenter
            Repeater {
                model: severity
                Rectangle {
                    height: 14; width: 6; color: "orange";
                    border.width: 1; border.color: "#FFDBBB"
                }
            }
        }
    }
    
    component WarningDelegate: MyCodeDelegate {

        icon.source: "warning.png"
        required property int lineno
        
        Text {
            anchors.right: parent.right
            anchors.rightMargin: 6
            anchors.verticalCenter: parent.verticalCenter
            text: "<a href='someline'>Go to line: " + lineno + " </a>"
            MouseArea {
                anchors.fill: parent
                cursorShape: Qt.PointingHandCursor
                propagateComposedEvents: true
                onClicked: (mouse) => {
                    console.log("Go to line " + lineno)
                    mouse.accepted = false
                    }
            }
        }
    }
}