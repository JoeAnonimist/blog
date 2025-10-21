import QtQuick
import QtQuick.Controls

ItemDelegate {

    id: root

    required property var modelData

    width: ListView.view.width
    text: modelData

    contentItem: Text {
        text: root.modelData
        horizontalAlignment: Text.AlignHCenter
    }

    background: Rectangle {
        anchors.fill: parent
        border.color: "lightgrey"
    }
}
