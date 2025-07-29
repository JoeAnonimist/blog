import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import examples.qthreadsubclass


ApplicationWindow {

    id: root
    visible: true
    title: "moveToThread Example"
    
    Controller {
        id: controller
        onProgress: (fileName) => {
            label.text = fileName
        }
    }

    onClosing: (closeEvent) => {
        controller.request_interruption()
    }

    ColumnLayout {
        
        anchors.fill: parent
        
        Button {
            
            id: startButton
            Layout.fillWidth: true
            text: "Start background thread"
            
            onClicked: {
                controller.start_thread()
                enabled = false
                cancelButton.enabled = true
            }
        }
        
        Button {
            
            id: cancelButton
            Layout.fillWidth: true
            text: "Cancel"
            enabled: false
            onClicked: {
                controller.request_interruption()
                enabled = false
                startButton.enabled = true
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