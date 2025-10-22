import QtQuick
import QtQuick.Controls

TableViewDelegate {

    implicitWidth: 120
    implicitHeight: 40

    TableView.onCommit: () => {
        console.log("commit")
    }
}
