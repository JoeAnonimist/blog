import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ItemDelegate {

    id: itemDelegate

    required property string name
    required property var type
    required property int index

    width: itemDelegate.GridView.view.cellWidth - 10
    height: itemDelegate.GridView.view.cellHeight - 10
    anchors.margins: 10

    contentItem:
        ColumnLayout {
            Image {
                Layout.alignment: Qt.AlignHCenter
                source: itemDelegate.type === Model.Type.File ?
                    "file.png" : "folder.png"
            }
            Text {
            Layout.alignment: Qt.AlignHCenter
            text: itemDelegate.name
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
        }
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
