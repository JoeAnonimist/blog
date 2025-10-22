import QtQuick
import QtQuick.Controls

ItemDelegate {

    id: itemDelegate

    required property string value
    required property int index

    width: itemDelegate.GridView.view.cellWidth - 10
    height: itemDelegate.GridView.view.cellHeight - 10
    anchors.margins: 10

    contentItem: Text {
        text: itemDelegate.value
        anchors.centerIn: parent
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter
    }

    background: Rectangle {
        anchors.fill: parent
        border.width: 2
        radius: 2
        color: "#dddedf"
        border.color: itemDelegate.down ?
            "steelblue" : "lightsteelblue"
    }

    onClicked: () => {
        console.log("clicked")
        GridView.view.currentIndex = index
    }
}
