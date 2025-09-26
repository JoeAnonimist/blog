import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {

    visible: true
    title: "Load Image"
    id: mainWindow

    ColumnLayout {
        
        anchors.fill: parent
            
	    AnimatedImage {
	    
	        id: myImage
	    
	        Layout.preferredWidth: 50
	        Layout.preferredHeight: 50
	        Layout.alignment: Qt.AlignCenter
	        	
	        source: "spinner.gif"
	        fillMode: Image.PreserveAspectFit
	        
	        onCurrentFrameChanged: parent.updateStats()
        }
        
        Button {
            text: "Pause/Resume"
            Layout.fillWidth: true
            onClicked: {
                myImage.paused = ! myImage.paused
                parent.updateStats()
            }
        }
        
        Button {
            text: "Stop playing"
            Layout.fillWidth: true
            onClicked: {
                myImage.playing = ! myImage.playing
                parent.update.Stats()
            }
        }
        
        Button {
            text: "Slow down"
            Layout.fillWidth: true
            onClicked: {
                if (myImage.speed >= 0.4) {
                    myImage.speed -= 0.2;
                } else {
                    myImage.speed = 1
                }
                parent.updateStats()
            }
        }
        
        Text {
            id: stats
        }
        
        Item {
            Layout.fillHeight: true
        }
        
        // Toggle playing resets animation
        // Toggle pause pauses and continues
        
        function updateStats() {
            stats.text =
`Current frame: ${myImage.currentFrame}
Frame count: ${myImage.frameCount}
Paused: ${myImage.paused}
Playing: ${myImage.playing}
Source: ${myImage.source}
Speed: ${myImage.speed}`;
        }
    }
}