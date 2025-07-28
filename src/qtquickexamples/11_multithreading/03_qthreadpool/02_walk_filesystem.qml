import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {

    visible: true
    title: "moveToThread Example"
    
    property QtObject controller
    
    Connections {
        target: controller
        function onProgress (result) {
            print(result)
            label.text = result
        }
        function onError (message) {
            print(message)
        }
    }
    
    onClosing: (closeEvent) => {
        if (controller !== null) {
            controller.cancel_runnable()
        }
    }

    ColumnLayout {
        
        anchors.fill: parent
        
        Button {
            
            id: startButton
            Layout.fillWidth: true
            text: "Start background thread"
            
            onClicked: {
                enabled = false
                cancelButton.enabled = true
                controller.run_task()
            }
        }
        
        Button {
            
            id: cancelButton
            Layout.fillWidth: true
            enabled: false
            text: "Cancel"
            
            onClicked: {
            enabled = false
            startButton.enabled = true
                controller.cancel_runnable()
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