import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {

    visible: true
    title: "Load Image"

    ColumnLayout {
        
        anchors.fill: parent
            
	    Image {
	    
	        id: myImage
	    
	        Layout.preferredWidth: 100
	        Layout.preferredHeight: 100
	        Layout.alignment: Qt.AlignCenter
	        	
	        source: "image.png"
	        fillMode: Image.PreserveAspectFit
        }
        
        Button {
            text: "Mirror horizontally"
            Layout.fillWidth: true
            onClicked: {
                myImage.mirror = ! myImage.mirror
            }
        }
        
        Button {
            text: "Mirror vertically"
            Layout.fillWidth: true
            onClicked: {
                myImage.mirrorVertically = ! myImage.mirrorVertically
            }
        }
    }
}