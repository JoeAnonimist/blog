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
        
        move: Transition {
            NumberAnimation {
                properties: "x,y"
                duration: 300
                easing.type: Easing.OutCubic
            }
        }

        Repeater {
            model: 10

            Rectangle {
            
                id: rect
            
                width: 100
                height: 30
                border.color: "steelblue"
                radius: 3

                color: root.generateLightColor()

                Text {
                    id: label
                    anchors.centerIn: parent
                    text: "Index: " + rect.Positioner.index
                    color: "black"
                }

                MouseArea {
                    anchors.fill: parent
                    onClicked: {
                        console.log(
                            "Index: " +
                            rect.Positioner.index +
                            ", Is first: " +
                            rect.Positioner.isFirstItem +
                            ", Is last: " +
                            rect.Positioner.isLastItem)
                    }
                }
            }
        }
    }
}