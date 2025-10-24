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
        x: 200
        y: 80
        text: "Click me"

        PropertyAnimation {
            id: animation
            target: button
            property: "x"
            to: target.x === 200 ? 100 : 200
            duration: 300
        }

        onClicked: () => {
            console.log("clicked")
            animation.running = true
        }
    }
}
