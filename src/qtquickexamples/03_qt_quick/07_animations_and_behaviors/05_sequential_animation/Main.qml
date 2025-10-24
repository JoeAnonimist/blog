import QtQuick
import QtQuick.Controls

ApplicationWindow {

    visible: true
    width: 400
    height: 200
    title: "Sequencial Animation"

    Button {

        id: button

        height: 40
        width: 80
        x: 10
        y: 80
        text: "Click Me"

        SequentialAnimation {

            id: animation

            PropertyAnimation {
                target: button; property: "x";
                to: 110; duration: 500 }
            PauseAnimation { duration: 100 }

            PropertyAnimation {
                target: button; property: "x";
                to: 210; duration: 500 }
            PauseAnimation { duration: 100 }

            PropertyAnimation {
                target: button; property: "x";
                to: 310; duration: 500 }
            PauseAnimation { duration: 100 }

            PropertyAnimation {
                target: button; property: "x";
                from: 310; to: 10; duration: 500 }
        }

        onClicked: () => {
            console.log("clicked")
            animation.running = true
        }
    }
}
