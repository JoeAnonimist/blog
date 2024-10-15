import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {

    visible: true
    width: 400
    height:400
    title: "Grid Layout Example"
    
    function setLabelText (name, row, column) {
        label.text = "Button: " + name + "\n" 
            + "row: " +  row + "\n"
            + "column: " + column
    }
    
    GridLayout {
        
        anchors.fill: parent
        columns: 2
            
        Button {

            // Layout.row: 0
            // Layout.column: 1
        
            Layout.fillWidth: true
            Layout.fillHeight: true
            text: "Button 1"
            
            onClicked: setLabelText(
                text, Layout.row, Layout.column)
        }
        
        Button {
            
            // Layout.row: 0
            // Layout.column: 0
        
            Layout.fillWidth: true
            Layout.fillHeight: true
            text: "Button 2"
            
            onClicked: setLabelText(
                text, Layout.row, Layout.column)
        }
        
        Button {
            
            // Layout.row: 1
            // Layout.column: 1
        
            Layout.fillWidth: true
            Layout.fillHeight: true
            text: "Button 3"
            
            onClicked: setLabelText(
                text, Layout.row, Layout.column)
        }
        
        Button {
            
            // Layout.row: 1
            // Layout.column: 0
        
            Layout.fillWidth: true
            Layout.fillHeight: true
            text: "Button 4"
            
            onClicked: setLabelText(
                text, Layout.row, Layout.column)
        }
        
        Label {
        
            id: label
            
            // Layout.row: 2
            // Layout.column: 0
            Layout.columnSpan: 2
            
            Layout.minimumHeight: 200
            Layout.maximumHeight: 200
            Layout.fillWidth: true
            Layout.fillHeight: true
            
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            
            text: "text"
        }
    }
}