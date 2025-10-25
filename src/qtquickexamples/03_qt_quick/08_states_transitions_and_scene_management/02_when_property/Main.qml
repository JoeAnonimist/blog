import QtQuick
import QtQuick.Controls

ApplicationWindow {

    visible: true
    width: 400
    height: 200
    title: "Basic State When Condition"

    Button {

        id: button

        checkable: true

        height: 40
        width: 100
        x: 10
        y: 80
        text: button.checked ? "ON" : "OFF"

        state: "OFF"
        states: [
            State {
                name: "OFF"
                PropertyChanges {
                    target: button
                    x: 10
                }
            },
            State {
                name: "ON"
                when: button.checked
                PropertyChanges {
                    target: button
                    x: 280
                }
            }
        ]

        transitions: Transition {
            NumberAnimation{
                property: "x"
                duration: 300
                easing.type: Easing.InOutQuad
            }
        }
    }
}
