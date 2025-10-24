import QtQuick
import QtQuick.Controls

ApplicationWindow {
    visible: true
    width: 300
    height: 300
    title: "Property Animation"

    Path {
        id: circlePath

        PathAngleArc {
            centerX: 100
            centerY: 130
            radiusX: 100
            radiusY: 100
            startAngle: 180
            sweepAngle: 360
        }
    }

    Button {
        id: button

        height: 40
        width: 100
        x: 0
        y: 130
        text: "Click me"

        PathAnimation {
            id: animation
            target: button
            path: circlePath
            duration: 1000
            loops: 1
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
