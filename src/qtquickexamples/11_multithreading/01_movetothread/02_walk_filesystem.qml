import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import examples.workerthread


ApplicationWindow {

    visible: true
    title: "moveToThread Example"
    
    Controller {
    
        id: controller
        
        onFinished: {
            label.text = "Worker finished"
        }

        onProgress: (file_name) => {
            label.text = file_name
            console.log(file_name)
        }
    }

    ColumnLayout {
        
        anchors.fill: parent
        
        Button {
            
            id: startButton
            Layout.fillWidth: true
            text: "Start background thread"
            enabled: true
            
            onClicked: {
                enabled = false
                cancelButton.enabled = true
                controller.start_working()
            }
        }
        
        Button {
            
            id: cancelButton
            Layout.fillWidth: true
            text: "Cancel"
            enabled: false
            
            onClicked: {
                enabled = false
                startButton.enabled = true
                controller.stop_working()
            }
        }
        
        Label {
            
            id: label
            Layout.fillWidth: true
            horizontalAlignment: Text.AlignHCenter
            text: "Results"
        }
        
        Item {
            Layout.fillHeight: true
        }
    }
}