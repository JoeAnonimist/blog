import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import examples.qthreadsubclass


ApplicationWindow {

    id: root
    visible: true
    title: "moveToThread Example"
    
    Component {
        id: wtComponent
        WorkerThread {
            id: wThread
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
                wThread.cleanup()
            }
        }
    }

    ColumnLayout {
        
        anchors.fill: parent
        
        Button {
            
            Layout.fillWidth: true
            text: "Start background thread"
            
            onClicked: {
                var workerThread = wtComponent.createObject(root)
                workerThread.objectName = "Worker thread " + Qt.formatDateTime(new Date(), "hhmmss")
                workerThread.start()
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