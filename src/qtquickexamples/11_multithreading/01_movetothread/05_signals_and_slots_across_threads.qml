import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import examples.workerthread


ApplicationWindow {

    visible: true
    title: "moveToThread Example"
    
    Controller {
        id: controller
    }

    ColumnLayout {
        
        anchors.fill: parent
        
        Button {
            
            id: autoButton
            Layout.fillWidth: true
            text: "Auto connection"
            onClicked: {
                console.log(controller.print_current_thread())
                controller.emitter.auto_signal()
            }
        }
        
        Button {
            
            id: directButton
            Layout.fillWidth: true
            text: "Direct connection"
            onClicked: {
                console.log(controller.print_current_thread())
                controller.emitter.direct_signal()
            }
        }
        
        Button {
            
            id: queuedButton
            Layout.fillWidth: true
            text: "Queued connection"
            onClicked: {
                console.log(controller.print_current_thread())
                controller.emitter.queued_signal()
            }
        }

        Button {
            
            id: blockingButton
            Layout.fillWidth: true
            text: "Blocking Queued connection"
            onClicked: {
                console.log(controller.print_current_thread())
                controller.emitter.blocking_signal()
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