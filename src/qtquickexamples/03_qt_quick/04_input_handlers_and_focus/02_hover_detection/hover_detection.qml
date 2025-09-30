import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {

    visible: true
    width: 300
    height:200
    title: "Hover detection"
    
    Rectangle {
        
        id: rect1

        anchors.centerIn: parent
        
        width: 100
        height: 40
        border {color: "steelblue"; width: 1}
        radius: 4
        color: "lightsteelblue"
        
        HoverHandler {
            onHoveredChanged: () => {
                console.log("Hovered")
                hovered ? rect1.border.width = 2 :
                    rect1.border.width = 1;
            }
        }
    }
}