import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {
    id: root
    visible: true
    width: 290
    height: 150
    title: "TableView example"

    property var sqlmodel

    Item {
        anchors.fill: parent

        HorizontalHeaderView {
            id: horizontalHeader
            syncView: tableView
            anchors.top: parent.top
            anchors.right: parent.right
            height: 24
        }

        VerticalHeaderView {
            id: verticalHeader
            syncView: tableView
            anchors.bottom: parent.bottom
            anchors.left: parent.left
            width: 24
        }

        TableView {
            id: tableView
            anchors.top: horizontalHeader.bottom
            anchors.left: verticalHeader.right
            anchors.right: parent.right
            anchors.bottom: parent.bottom

            model: sqlmodel

            delegate: Rectangle {
                implicitWidth: 80
                implicitHeight: 44
                border.color: "lightgray"
                Text {
                    anchors.centerIn: parent
                    text: display
                }
            }

            ScrollBar.vertical: ScrollBar {
                policy: ScrollBar.AlwaysOn
            }
        }
    }
}
