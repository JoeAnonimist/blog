import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {

    id: root

    visible: true
    width: 200
    height:100
    title: "DelayButton example"
    
    function logProgress () {
            console.log(delayButton.progress)
            if (delayButton.progress % 0.2 < 0.003) {
                var remainingSeconds = 5 * (1 - delayButton.progress)
                label.text = "This message will self destruct in " 
                + Math.round(remainingSeconds)
            }
    }
    
    ColumnLayout {

        anchors.fill: parent
            
        DelayButton {
            
            id: delayButton
            Layout.fillWidth: true
            delay: 6000
            text: "Delay"
            
            onProgressChanged: logProgress()
            onActivated: {
                label.text += "Activated"
            }
        }
        
        Label {

            id: label
            
            Layout.fillWidth: true
            Layout.fillHeight: true
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
        }
    }
}