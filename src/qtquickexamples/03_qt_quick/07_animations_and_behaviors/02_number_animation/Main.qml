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

        NumberAnimation on scale {
            id: animation
            to: button.scale === 1 ? 1.2 : 1
            duration: 300
            running: false
        }

        onClicked: () => {
            animation.running = true
        }
    }
}
