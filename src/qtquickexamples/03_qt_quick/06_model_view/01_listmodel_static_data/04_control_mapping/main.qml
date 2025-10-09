import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import "."
import "ListOperations.js" as ListOps

ApplicationWindow {
    visible: true
    width: 250
    height: 400
    title: "Resizable ListModel"

    ItemModel {
        id: listModel
    }

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 6

        ListView {
            id: listView
            Layout.fillWidth: true
            Layout.fillHeight: true
            model: listModel
            focus: true
            highlightFollowsCurrentItem: true

            highlight: Rectangle {
                color: "orange"
                opacity: 0.2
            }

            delegate: ItemDelegate {
                isSelected: index === listView.currentIndex
                onClicked: listView.currentIndex = index
            }

            ScrollBar.vertical: ScrollBar {}
        }

        RowLayout {
            Layout.fillWidth: true
            spacing: 6

            property int currentIndex: listView.currentIndex
            property bool hasSelection: {
                currentIndex >= 0 && currentIndex < listModel.count
            }

            TextField {
                id: nameField
                Layout.fillWidth: true
                placeholderText: "Name"
                text: {
                    parent.hasSelection ?
                        listModel.get(parent.currentIndex).name : ""
                }
                onAccepted: {
                    if (parent.hasSelection) {
                        let currentValue = listModel.get(parent.currentIndex).value
                        ListOps.updateItem(listModel, listView, parent.currentIndex, text, currentValue)
                    }
                }
            }

            SpinBox {
                id: valueSpinbox
                Layout.preferredWidth: 70
                from: 0
                to: 100
                editable: true
                value: parent.hasSelection ? listModel.get(parent.currentIndex).value : 0
                onValueModified: {
                    if (parent.hasSelection) {
			            let currentName = listModel.get(parent.currentIndex).name
			            ListOps.updateItem(listModel, listView, parent.currentIndex, currentName, value)
                    }
                }
            }

            Button {
                text: "➕"
                Layout.preferredWidth: implicitHeight
                onClicked: ListOps.addItem(listModel, listView)
            }

            Button {
                text: "➖"
                enabled: listModel.count > 0
                Layout.preferredWidth: implicitHeight
                onClicked: ListOps.removeCurrentItem(listModel, listView)
            }
        }
    }

    function addItem() {
        listModel.append({ name: "New Item", value: 0 })
        listView.currentIndex = listModel.count - 1
        listView.positionViewAtIndex(listView.currentIndex, ListView.End)
    }

    function removeCurrentItem() {
        if (listView.currentIndex >= 0 && listView.currentIndex < listModel.count) {
            listModel.remove(listView.currentIndex, 1)
            listView.currentIndex = Math.min(listView.currentIndex, listModel.count - 1)
        }
    }

    function updateItem(idx, newName, newValue) {
        if (idx >= 0 && idx < listModel.count) {
            listModel.setProperty(idx, "name", newName)
            listModel.setProperty(idx, "value", newValue)
            listView.forceActiveFocus()
        }
    }
}