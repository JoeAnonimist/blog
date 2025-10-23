import QtQuick
import QtQuick.Controls

TableViewDelegate {

    id: root

    implicitWidth: 120
    implicitHeight: 40

    contentItem: Rectangle {
        anchors.fill: parent
        border.width: 1
        border.color: "lightsteelblue"
        Text {
            id: delegateText
            anchors.centerIn: parent
            text: root.model.display
        }
    }
}
