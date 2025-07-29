import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import examples.qthreadsubclass


ApplicationWindow {

    id: root
    visible: true
    title: "moveToThread Example"
    /*
    Component {
        id: wtComponent
        WorkerThread {
            id: workerThread
            onResult_ready: (result) => {
                print(result)
                label.text = result
            }
            onFinished: {
                // Log available members
                // print("WorkerThread members:")
                // for (var prop in workerThread) {
                //     print("  " + prop)
                // }
                workerThread.cleanup()
            }
        }
    }*/
    
    Controller {
        id: controller
        onResult_ready: (result) => {
            label.text = result
        }
    }

    ColumnLayout {
        
        anchors.fill: parent
        
        Button {
            
            Layout.fillWidth: true
            text: "Start background thread"
            
            onClicked: {
                controller.start_thread()
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