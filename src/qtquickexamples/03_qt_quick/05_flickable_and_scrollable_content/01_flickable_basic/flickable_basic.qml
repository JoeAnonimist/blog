import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {

    visible: true
    width: 400
    height: 200
    title: "Flickable Example"

    Flickable {
    
        anchors.fill: parent
        clip: true
        
        contentWidth: width
        contentHeight: contentColumn.height
        
        flickableDirection: Flickable.VerticalFlick
        boundsBehavior: Flickable.DragAndOvershootBounds
        flickDeceleration: 1000
    
	    Column {
            
            id: contentColumn
	        spacing: 8
	        width: parent.width
	
	        Repeater {
	
	            model: 20
	
	            Rectangle {
	
	                anchors.horizontalCenter: parent.horizontalCenter
	                width: 200; height: 40
	                border.color: "lightsteelblue"
	                radius: 4
	                
	                Text {
	                    anchors.centerIn: parent
	                    text: index
	                }
	            }
	        }
	    }
	}
}
