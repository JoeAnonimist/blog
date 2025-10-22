import QtQuick
import QtQuick.Controls

ApplicationWindow {

    visible: true
    width: 340
    height: 200
    title: "TableView with static data"

    TableView {

        id: tableView

        anchors.fill: parent
        anchors.margins: 10

        focus: true

        editTriggers: TableView.DoubleTapped
        selectionBehavior: TableView.SelectCells
        selectionModel: ItemSelectionModel{ }

        delegate: Delegate {}
        model: Model {}
    }
}
