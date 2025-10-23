import QtQuick
import QtQuick.Controls

ApplicationWindow {

    id: root

    visible: true
    width: 340
    height: 200
    title: "TableView QStandardItemModel"

    property var tableModel

    HorizontalHeaderView {
        id: horizontalHeader
        anchors.left: verticalHeader.right
        anchors.top: parent.top
        anchors.topMargin: 10
        anchors.leftMargin: 10
        syncView: tableView
        clip: true
    }

    VerticalHeaderView {
        id: verticalHeader
        anchors.top: horizontalHeader.bottom
        anchors.left: parent.left
        anchors.leftMargin: 10
        anchors.topMargin: 10
        syncView: tableView
        clip: true
    }

    TableView {

        id: tableView

        anchors.left: verticalHeader.right
        anchors.top: horizontalHeader.bottom
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        anchors.margins: 10
        rowSpacing: -1
        columnSpacing: -1

        focus: true

        editTriggers: TableView.DoubleTapped | TableView.EditKeyPressed
        selectionBehavior: TableView.SelectCells
        selectionModel: ItemSelectionModel{ }

        delegate: Delegate {}
        model: root.tableModel

        Connections {
            target: root.tableModel
            function onDataChanged(topLeft, bottomRight, roles) {
                console.log(root.tableModel.data(
                    root.tableModel.index(topLeft.row, topLeft.column)))
            }
        }
    }
}
