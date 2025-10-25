import QtQuick
import QtQuick.Controls

ApplicationWindow {

    visible: true
    width: 400
    height: 200
    title: "Basic State Change"

    Button {

        id: button

        height: 40
        width: 100
        x: 10
        y: 80
        text: "Click me"

        state: "left"
        states: [
            State {
                name: "left"
                PropertyChanges {
                    target: button
                    x: 10
                }
            },
            State {
                name: "right"
                PropertyChanges {
                    target: button
                    x: 280
                }
            }
        ]

        onClicked: () => {
            console.log("clicked", button.background)
            button.state = button.state === "left" ? "right" : "left"
        }
    }
}
