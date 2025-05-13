import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {

    visible: true
    width: 200
    height:80
    title: "Stack Layout Example"
    
    function rotateRectangles () {
        label.text = Math.floor(
            Math.random() * 100 + 1)
    }
    
    ColumnLayout {
        
        anchors.fill: parent
            
        Button {
        
            Layout.fillWidth: true
            Layout.alignment: Qt.AlignTop
            text: "Rotate rectangles"
            
            onClicked: rotateRectangles()
        }
        
        Label {

            id: label
            
            Layout.fillWidth: true
            Layout.fillHeight: true
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
        }
    }
}