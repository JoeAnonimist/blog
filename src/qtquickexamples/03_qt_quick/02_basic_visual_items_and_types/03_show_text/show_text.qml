import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {

    visible: true

    ColumnLayout {
        
        anchors.fill: parent
            
	    Text {
	    
	        id: myText
	    
	        Layout.alignment: Qt.AlignCenter
	        text: "Your text here"
	        
	        font.family: "Georgia"
	        font.pointSize: 14
	        
        }
        
        Button {
            text: "Mirror horizontally"
            Layout.fillWidth: true
        }
        
        Button {
            text: "Mirror vertically"
            Layout.fillWidth: true
        }
    }
}