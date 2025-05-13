import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {

    visible: true
    //width: 400
    //height:400
    title: "Stack Layout Example"
    
    function rotateRectangles () {
    }
    
    ColumnLayout {
        
        anchors.fill: parent
            
        Button {
        
            Layout.fillWidth: true
            text: "Rotate rectangles"
            
            onClicked: rotateRectangles()
        }
        
        Label {
        }
    }
}