import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {

    id: root
    visible: true
    width: 350
    height: 250

    function generateLightColor() {
        var randLightChannel = function() {
            return Math.floor(Math.random() * (255 - 180 + 1)) + 180;
        }
        var r = randLightChannel();
        var g = randLightChannel();
        var b = randLightChannel();
        return Qt.rgba(r / 255, g / 255, b / 255, 1.0);
    }

    Flow {
        id: flowPositioner
        spacing: 5
        anchors.fill: parent

        Repeater {
            model: 10

            Rectangle {
                width: Math.random() * (120 - 60) + 60
                height: Math.random() * (60 - 30) + 30
                border.color: "steelblue"
                radius: 1

                color: root.generateLightColor()

                Text {
                    id: label
                    anchors.centerIn: parent
                    text: "Index: " + index
                    color: "black"
                }

                MouseArea {
                    anchors.fill: parent
                    onClicked: {
                        console.log(label.text)
                    }
                }
            }
        }
    }
}