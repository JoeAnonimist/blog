import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    visible: true
    width: 300
    height: 200
    title: "Nine Patch Image"
    flags: Qt.Window | Qt.WindowResizable

    Item {
        anchors.fill: parent
        anchors.margins: 20

        BorderImage {
            anchors.fill: parent
            source: "border.png"
            border.left: 60
            border.top: 60
            border.right: 60
            border.bottom: 60
            horizontalTileMode: BorderImage.Stretch
            verticalTileMode: BorderImage.Stretch
        }

        ColumnLayout {
            anchors.fill: parent
            anchors.margins: 25

            Rectangle {
                Layout.fillWidth: true
                Layout.fillHeight: true
                color: "lightgrey"
                focus: true

                Text {
                    anchors.centerIn: parent
                    text: "Click Me"
                    color: "#333"
                    font.bold: true
                    font.pointSize: 16
                }

                MouseArea {
                    id: mouseArea
                    anchors.fill: parent
                    onClicked: console.log("Rectangle clicked!")
                }
                
                scale: mouseArea.pressed ? 0.995 : 1.0
                
            }
        }
    }
}