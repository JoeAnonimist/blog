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

        ParallelAnimation {

            id: animation
            running: false

            PathAnimation {
                target: button
                path: circlePath
                duration: 1000
                loops: 2
            }
            RotationAnimation {
                target: button
                from: 0
                to: 360
                duration: 1000
                loops: 2
            }
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
