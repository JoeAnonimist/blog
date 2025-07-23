import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {

    visible: true
    width: 400
    height:400
    title: "Grid Layout Example"
    
    function setLabelText (name) {
        label.text = name + " clicked"
    }
    
    GridLayout {
        
        anchors.fill: parent
        columns: 2
            
        Button {
        
            Layout.fillWidth: true
            Layout.fillHeight: true
            text: "Button 1"
            
            onClicked: setLabelText(text)
        }
        
        Button {
        
            Layout.fillWidth: true
            Layout.fillHeight: true
            text: "Button 2"

            onClicked: setLabelText(text)
        }
        
        Button {
        
            Layout.fillWidth: true
            Layout.fillHeight: true
            text: "Button 3"
            
            onClicked: setLabelText(text)
        }
        
        Button {
        
            Layout.fillWidth: true
            Layout.fillHeight: true
            text: "Button 4"
            
            onClicked: setLabelText(text)
        }
        
        Label {
        
            id: label
            
            Layout.columnSpan: 2
            
            Layout.minimumHeight: 200
            Layout.maximumHeight: 200
            Layout.fillWidth: true
            Layout.fillHeight: true
            
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            
            //text: "text"
        }
    }
}