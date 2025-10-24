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

        NumberAnimation {
            id: animation
            target: button
            property: "scale"
            to: target.scale === 1 ? 1.2 : 1
            duration: 300
        }

        onClicked: () => {
            animation.running = true
        }
    }
}
