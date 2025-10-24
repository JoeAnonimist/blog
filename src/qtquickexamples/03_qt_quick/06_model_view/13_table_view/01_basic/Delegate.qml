import QtQuick
import QtQuick.Controls

TableViewDelegate {

    id: root

    implicitWidth: 120
    implicitHeight: 40

    contentItem: Rectangle {
        anchors.fill: parent
        color: "transparent"
        border.width: 1
        border.color: "lightsteelblue"
        Text {
            id: delegateText
            anchors.centerIn: parent
            text: root.model.display
        }
    }

    TableView.editDelegate: TextField {

        anchors.fill: parent
        horizontalAlignment: TextInput.AlignHCenter
        verticalAlignment: TextInput.AlignVCenter
        text: edit
        TableView.onCommit: () => {
            console.log("commit")
            edit = text
            display = text
            console.log(display, edit)
        }
    }
}
