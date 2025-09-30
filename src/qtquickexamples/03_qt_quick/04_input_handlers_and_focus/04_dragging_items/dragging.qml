import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {

    id: mainWindow

    visible: true
    width: 300
    height:200
    title: "Drag Handler"
    
    Rectangle {
    
        id: rect
        
        width: 100
        height: 40
        border.color: "steelblue"
        border.width: 1
        radius: 4
        color: "lightsteelblue"
        
        // opacity is the new transparency
        opacity: dragHandler.active ? 0.5 : 1.0
        
        // Cannot drag anchored items.
        anchors.centerIn: parent
        
        DragHandler {
        
            id: dragHandler
        
            xAxis.minimum: 0
            xAxis.maximum: mainWindow.width - rect.width
            yAxis.minimum: 0
            yAxis.maximum: mainWindow.height - rect.height
            
            onActiveChanged: {
                if (active) {
                    rect.anchors.centerIn = undefined
                }
            }
        }
    }
}