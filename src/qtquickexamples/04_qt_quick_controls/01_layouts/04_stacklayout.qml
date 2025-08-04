import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {

    visible: true
    width: 400
    height:400
    title: "Stack Layout Example"
    
    function rotateRectangles () {
        console.log("rotating")
        if (layout.currentIndex == layout.count - 1) {
            layout.currentIndex = 0
        } else {
            layout.currentIndex ++
        }
    }
    
    ColumnLayout {
        
        anchors.fill: parent
            
        Button {
        
            Layout.fillWidth: true
            text: "Rotate rectangles"
            
            onClicked: rotateRectangles()
        }
        
        StackLayout {
            
            id: layout
            currentIndex: 0
            
            Rectangle {
                color: "yellow"
            }
            
            Rectangle {
                color: "red"
            }
            
            Rectangle {
                color: "blue"
            }
            
            Rectangle {
                color: "green"
            }
        }
    }
}