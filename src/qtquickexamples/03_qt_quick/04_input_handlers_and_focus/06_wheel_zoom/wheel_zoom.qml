import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {

    id: appWindow

    visible: true
    width: 300
    height:250
    title: "Mouse Wheel Zoom"
    
    Rectangle {
    
        id: rect

        anchors.centerIn: parent
        
        width: 100
        height: 40
        scale: 1.0
        border {color: "steelblue"; width: 1}
        radius: 4
        color: "lightsteelblue"
        
        WheelHandler {
            onWheel: (event) => {
                const delta = event.angleDelta.y / 120.0
                if (delta > 0) {
                    rect.scale = Math.min(rect.scale * 1.1, 3.0)
                } else if (delta < 0) {
                    rect.scale = Math.max(rect.scale / 1.1, 0.5)
                }
                event.accepted = true
            }
        }
    }
}