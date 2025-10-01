import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {

    visible: true
    width: 300
    height:200
    
    
    component MyComponent: Rectangle {
        
        width: 200; height: 40
        border {color: "steelblue"; width: 1}
        
        Row {
        
            anchors.fill: parent
            spacing: 6
            anchors.margins: 6
        
            Rectangle {
                width: (parent.width - parent.spacing) / 2
                height: parent.height
                border.width: 1; border.color: "lightsteelblue"
                Text { text: "Name"; anchors.centerIn: parent }
            }
            Rectangle {
                width: (parent.width - parent.spacing) / 2
                height: parent.height
                border.width: 1; border.color: "lightsteelblue"
                Text { text: "Value"; anchors.centerIn: parent }
            }
        }
    }
    
    Column {
    
        anchors.centerIn: parent
        spacing: 6
    
	    MyComponent {focus: true}
	    MyComponent {focus: true}
	    MyComponent {}
	}
}