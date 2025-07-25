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
    }

    ColumnLayout {
        
        anchors.fill: parent
        
        Button {
            
            Layout.fillWidth: true
            text: "Start background thread"
            
            onClicked: {
                enabled = false
                controller.start_working()
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