import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {

    visible: true
    width: 600
    height:200
    title: "Template App"
    
    property var timer
    property int counter

    RowLayout {
        
        anchors.fill: parent
            
        Button {
        
            id: startTimer
        
            text: "Start timer"

            Layout.fillWidth: true
            Layout.fillHeight: true
            Layout.margins: 20
            
            onClicked: {
                startTimer.enabled = false
                stopTimer.enabled = true
                timer.start()
            }
        }

        Button {
           
            id: stopTimer
        
            text: "Stop timer"

            Layout.fillWidth: true
            Layout.fillHeight: true
            Layout.margins: 20
            
            onClicked: {
                startTimer.enabled = true
                stopTimer.enabled = false
                timer.stop()
            }
        }

        Label {
        
            id: label

            Layout.minimumWidth: 200
            Layout.maximumWidth: 200
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            font.pixelSize: 48
            font.bold: true
        }
        
        Connections {
        
            target: timer
            
            function onTimeout () {
                counter++
                label.text = counter 
            }
        }
    }
}