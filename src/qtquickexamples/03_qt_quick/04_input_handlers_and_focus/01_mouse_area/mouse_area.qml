import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {

    visible: true
    width: 300
    height:200
    title: "Mouse Area"
    
    Rectangle {

        anchors.centerIn: parent
        
        width: 100
        height: 40
        
        border {color: "steelblue"; width: 1}
        
        radius: 4
        color: "lightsteelblue"
        
        MouseArea {
        
            anchors.fill: parent
            acceptedButtons: Qt.AllButtons            
            
            onClicked: (mouse) => {
                console.log("Clicked!")
                console.log("Accepted: " + mouse.accepted)
                console.log("Button: " + mouse.button)
                console.log("Buttons: " + mouse.buttons)
                console.log("Flags: " + mouse.flags)
                console.log("Modifiers: " + mouse.modifiers)
                console.log("Was held: " + mouse.wasHeld + "\n")
            }
            
            onDoubleClicked: (mouse) => {
                console.log("Double-clicked" + "\n")
            }
            
            onWheel: (wheel) => {
                console.log("Wheel")
                console.log("Accepted: " + wheel.accepted)
                console.log("Inverted: " + wheel.inverted)
                console.log("Angle delta: " + wheel.angleDelta)
                console.log("Pixel delta: " + wheel.pixelDelta + "\n")
            }

            onPressAndHold: (mouse) => {
                console.log("Press and hold detected")
                console.log("Was held: " + mouse.wasHeld + "\n")
            }
        }
    }
}