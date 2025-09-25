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
	        Layout.fillWidth: true
	        wrapMode: Text.WordWrap
	        horizontalAlignment: Text.AlignHCenter
	        verticalAlignment: Text.AlignVCenter
	        text: "Your text here"
	        
	        font.family: "Serif"
	        font.pointSize: 20
	        
        }
        
        Button {
            text: "Toggle Bold"
            Layout.fillWidth: true
            onClicked: () => {
                myText.font.bold = ! myText.font.bold
            }
        }
        
        Button {
            text: "Toggle Italic"
            Layout.fillWidth: true
            onClicked: () => {
                myText.font.italic = ! myText.font.italic
            }
        }
        
        Item {
            Layout.fillHeight: true
        }
    }
}