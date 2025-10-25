import QtQuick
import QtQuick.Controls

ApplicationWindow {

    visible: true
    width: 400
    height: 200
    title: "Spring Animation"

    Button {

        id: button

        height: 40
        width: 100
        x: 10
        y: 80
        text: "Click me"

        Behavior on x { SpringAnimation { spring: 4; damping: 0.05 }}

        onClicked: () => {
            console.log("clicked")
            button.x = button.x === 10 ? 280 : 10
        }
    }
}
