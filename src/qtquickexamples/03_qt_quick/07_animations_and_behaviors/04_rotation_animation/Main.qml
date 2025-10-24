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

        RotationAnimation on rotation{
            id: animation
            from: 0
            to: 360
            loops:3
            duration: 500
            running: false
        }

        onClicked: () => {
            console.log("clicked")
            if (animation.running) {
                animation.paused ? animation.resume() : animation.pause()
            } else {
                animation.running = true
            }
        }
    }
}
