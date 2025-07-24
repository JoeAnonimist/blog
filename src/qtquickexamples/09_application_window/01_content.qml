import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {

    visible: true
    width: 400
    height:200
    title: "Application Window"
    
    ScrollView {
    
        anchors.fill: parent
    
	    TextArea {
	        
	        id: textArea
	    }
	}
}