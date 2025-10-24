import QtQuick
import QtQuick.Controls

ApplicationWindow {

    visible: true
    width: 400
    height: 200
    title: "Property Animation"

    Button {

        id: button

        height: 40
        width: 100
        anchors.centerIn: parent
        text: "Click me"

        background: Rectangle {
            id: background
            color: "lightsteelblue"
        }

        ColorAnimation{
            id: animation
            target: background
            property: "color"
            // === does not work here as color is an object
            to: Qt.colorEqual(background.color, "lightsteelblue") ?
                "lightgrey" : "lightsteelblue"
            duration: 1000
            running: false
        }

        onClicked: () => {
            animation.running = true
        }
    }
}
