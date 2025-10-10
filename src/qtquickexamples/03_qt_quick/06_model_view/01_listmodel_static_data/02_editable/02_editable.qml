import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {

    visible: true
    width: listView.implicitWidth
    height: listView.implicitHeight
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
        implicitWidth: 220
        implicitHeight: count * 40
        focus: true
        highlightFollowsCurrentItem: true

        highlight: Rectangle {
            color: "orange"
            opacity: 0.2
        }

        delegate: MyDelegate {}

        ScrollBar.vertical: ScrollBar {}
    }

    component MyDelegate: Rectangle {

        id: root

        required property int index
        required property string name
        required property int value
        
        property int originalValue

        width: 200
        height: 40
        color: index === ListView.view.currentIndex
            ? "transparent"
            : index % 2 === 0 ? "#f0f0f0" : "#dcdcdc"

        RowLayout {
            anchors.fill: parent
            anchors.margins: 8

            Label {
                text: name
                Layout.fillWidth: true
            }

            StackLayout {
                id: valueStack
                Layout.preferredWidth: 20
                Layout.fillHeight: true
                currentIndex: root.state === "edit" ? 1 : 0

                Label {
                    id: displayControl
                    text: value
                    horizontalAlignment: Text.AlignRight
                }

                SpinBox {
                    id: editControl
                    focus: root.state === "edit"
                    from: 0; to: 100; editable: true
                    value: root.value
                    
                    onValueModified: () => {
                        listModel.setProperty(index, "value", value)
                    }

                    onActiveFocusChanged: {
                        if (!activeFocus && root.state === "edit") {
                            root.state = ""
                        }
                    }

                    Keys.onReturnPressed: { root.state = "" }
                    Keys.onEnterPressed: { root.state = "" }
                    Keys.onEscapePressed: {
                        console.log(root.originalValue)
                        listModel.setProperty(index, "value", root.originalValue)
                        editControl.value = root.originalValue
                        root.state = ""
                    }
                }
            }
        }

        MouseArea {

            anchors.fill: parent
            enabled: root.state !== "edit"

            onClicked: (mouse) => {
                root.ListView.view.currentIndex = index
            }

            onDoubleClicked: (mouse) => {
                originalValue = value
                root.state = "edit"
                editControl.forceActiveFocus()
            }
        }
    }
}
