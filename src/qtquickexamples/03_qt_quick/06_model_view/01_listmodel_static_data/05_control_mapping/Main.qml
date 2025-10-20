import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {

    visible: true
    width: 200
    height: 300
    title: "Editable ListModel with Mapped Controls"

    ColumnLayout {

        anchors.fill: parent
        anchors.margins: 4

        ListView {

            id: listView

            Layout.fillWidth: true
            implicitHeight: 250
            spacing: 4
            focus: true
            clip: true

            highlightFollowsCurrentItem: true
            highlight: Rectangle {
                height: 40; width: parent.width
                color: "#0078d7"; opacity: 0.2
            }

            ScrollBar.vertical: ScrollBar { }

            model: Model { id: listModel }

            delegate: Delegate {}

            Keys.onEnterPressed: () => {
                valueField.forceActiveFocus()
                console.log("focus")
            }
            Keys.onReturnPressed: () => {
                valueField.forceActiveFocus()
                console.log("focus")
            }
        }

        RowLayout {

            Layout.fillWidth: true
            spacing: 6

            property int currentIndex: listView.currentIndex
            property bool hasSelection: {
                currentIndex >= 0 && currentIndex < listModel.count
            }

            TextField {
                id: valueField
                Layout.fillWidth: true
                placeholderText: "Value"
                text: {
                    parent.hasSelection ?
                        listModel.get(parent.currentIndex).value : ""
                }
                onAccepted: {
                    if (parent.hasSelection) {
                        listModel.setProperty(
                            listView.currentIndex, "value", text)
                        listView.forceActiveFocus()
                    }
                }
            }

            Button {
                text: "➕"
                Layout.preferredWidth: implicitHeight
                onClicked: () => {
                    listModel.append({"value": "<new>"})
                    listView.currentIndex = listModel.count - 1
                    listView.positionViewAtIndex(listView.currentIndex, ListView.Center)
                    listView.forceActiveFocus()
                }
            }

            Button {
                text: "➖"
                enabled: listModel.count > 0
                Layout.preferredWidth: implicitHeight
                onClicked: () => {
                    if (listModel.count > 0) {
                        listModel.remove(listView.currentIndex)
                        if (listView.currentIndex == listModel.count) {
                            listView.currentIndex = listView.currentIndex - 1
                        }
                        listView.forceActiveFocus()
                    }
                }
            }
        }

    }
}
