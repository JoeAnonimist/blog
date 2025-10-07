import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    visible: true
    width: listView.implicitWidth
    height: listView.implicitWidth
    title: "Editable ListModel"

    ListModel {
        id: listModel
        objectName: "listModel"

        ListElement { name: "Item 0"; value: 0 }
        ListElement { name: "Item 1"; value: 1 }
        ListElement { name: "Item 2"; value: 2 }
        ListElement { name: "Item 3"; value: 3 }
        ListElement { name: "Item 4"; value: 4 }
        ListElement { name: "Item 5"; value: 5 }
        ListElement { name: "Item 6"; value: 6 }
        ListElement { name: "Item 7"; value: 7 }
        ListElement { name: "Item 8"; value: 8 }
        ListElement { name: "Item 9"; value: 9 }
    }

    ListView {
        id: listView

        anchors.fill: parent
        model: listModel

        implicitWidth: 200
        implicitHeight: count * 40

        focus: true
        highlightFollowsCurrentItem: true
        highlight: Rectangle {
            color: "orange"
            opacity: 0.2
        }

        delegate: MyDelegate {}

        ScrollBar.vertical: ScrollBar {}

        onCurrentIndexChanged: console.log("Current index changed: " + currentIndex)
    }

    component MyDelegate: Rectangle {
        id: root

        required property int index
        required property var model

        width: 200
        height: 40
        color: index === ListView.view.currentIndex ?
                   "transparent" :
                   index % 2 === 0 ? "#f0f0f0" : "#dcdcdc"

        RowLayout {
            anchors.fill: parent
            anchors.margins: 8

            TextField {
                id: nameField
                text: model.name
                readOnly: true
                Layout.fillWidth: true
                onAccepted: {
                    model.name = text
                    readOnly = true
                }
            }

            TextField {
                id: valueField
                text: model.value
                readOnly: true
                horizontalAlignment: Text.AlignRight
                validator: IntValidator {}  // Ensures only integers
                Layout.preferredWidth: 50
                onAccepted: {
                    model.value = parseInt(text, 10)
                    readOnly = true
                }
            }
        }

        MouseArea {
            anchors.fill: parent
            acceptedButtons: Qt.LeftButton | Qt.RightButton  // For double-click detection
            onClicked: {
                root.ListView.view.currentIndex = index
                console.log("Clicked: " +
                            "Current index: " + root.ListView.view.currentIndex +
                            " Name: " + model.name + " Value: " + model.value)
            }
            onDoubleClicked: {
                nameField.readOnly = false
                nameField.forceActiveFocus()
                valueField.readOnly = false  // Optionally edit both; could target specific field
                console.log("Entered edit mode for index: " + index)
            }
        }
    }
}