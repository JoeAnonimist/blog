import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {

    visible: true
    width: 300
    height:200
    title: "Key presses"
    
    Rectangle {
        
        id: rect1

        anchors.centerIn: parent
        
        width: 100
        height: 40
        border {color: "steelblue"; width: 1}
        radius: 4
        color: "lightsteelblue"
        
        Text {
            
            anchors.fill: parent
            text: "Type something"
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            
            focus: true
            
            Keys.onPressed: (event) => {
                text = event.text
                console.log(event.text)
            }
        }

    }
}