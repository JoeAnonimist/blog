import QtQuick
import QtQuick.Controls

Rectangle {

    id: root
    required property string value
    required property int index

    width: ListView.view.width
    height: 40

    color: "transparent"
    border.color: "lightgrey"
    border.width: 1

    Label {
        anchors.fill: parent
        anchors.margins: 8
        verticalAlignment: Text.AlignVCenter
        text: root.value
    }

    MouseArea {
        id: mouse
        anchors.fill: parent
        onClicked: mouse => {
                       root.ListView.view.currentIndex = root.index
                   }
    }
}
