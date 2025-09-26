import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    visible: true
    width: 300
    height: 200
    title: "Nine Patch Image"

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
            width: parent.width - 50
            height: parent.height - 50

            Rectangle {
                Layout.fillWidth: true
                Layout.fillHeight: true
                color: "#FCFCFC"

                Text {
                    anchors.centerIn: parent
                    text: "Click Me"
                    color: "#333"
                    font.bold: true
                    font.pointSize: 16
                }

                MouseArea {
                    anchors.fill: parent
                    onClicked: console.log("Rectangle clicked!")
                }
            }
        }
    }
}