import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {

    id: mainWindow

    visible: true
    width: 300
    height:200
    title: "Tap Handler"
    
    Rectangle {
    
        id: rect
        
        width: 100
        height: 40
        border.color: "steelblue"
        border.width: 1
        radius: 4
        color: "lightsteelblue"
        anchors.centerIn: parent
        
        TapHandler {
        
            onTapped: () => {
                tappedLog.text = "Tapped! " + tapCount + " times" 
            }
            
            onSingleTapped: () => {
                singleTappedLog.text = "Single tapped! " 
            }
            
            onDoubleTapped: () => {
                doubleTappedLog.text = "Double tapped! " 
            }
            
            onLongPressed: () => {
                tappedLog.text = ""
                singleTappedLog.text = ""
                doubleTappedLog.text = ""
            }
        }
    }
    
    Text { 
	    id: tappedLog
	    anchors.top: rect.bottom
	    anchors.horizontalCenter: rect.horizontalCenter
	    horizontalAlignment: Text.AlignHCenter
	    verticalAlignment: Text.AlignVCenter
	}
	
    Text { 
	    id: singleTappedLog
	    anchors.top: tappedLog.bottom
	    anchors.horizontalCenter: rect.horizontalCenter
	    horizontalAlignment: Text.AlignHCenter
	    verticalAlignment: Text.AlignVCenter
	}
	
    Text { 
	    id: doubleTappedLog
	    anchors.top: singleTappedLog.bottom
	    anchors.horizontalCenter: rect.horizontalCenter
	    horizontalAlignment: Text.AlignHCenter
	    verticalAlignment: Text.AlignVCenter
	}
}