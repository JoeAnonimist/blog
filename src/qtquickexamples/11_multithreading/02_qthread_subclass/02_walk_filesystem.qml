import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import examples.qthreadsubclass


ApplicationWindow {

    id: root
    visible: true
    title: "moveToThread Example"
    
    property var workerThread: null
    
    Component {
        id: wtComponent
        WorkerThread {
            onProgress: (file_name) => {
                label.text = file_name
            }
            onFinished: {
                cleanup()
            }
        }
    }
    
    onClosing: (closeEvent) => {
        if (workerThread !== null) {
            workerThread.safelyRequestInterruption()
            workerThread.destroy()
            workerThread = null
        }
    }

    ColumnLayout {
        
        anchors.fill: parent
        
        Button {
            
            id: startButton
            Layout.fillWidth: true
            text: "Start background thread"
            
            onClicked: {
                workerThread = wtComponent.createObject(root)
                workerThread.objectName = "Worker thread " + Qt.formatDateTime(new Date(), "hhmmss")
                workerThread.start()
                enabled = false
                cancelButton.enabled = true
                print(root)
                print(root.children)
                //enumerateChildren(root)
            }
        }
        
        Button {
            
            id: cancelButton
            Layout.fillWidth: true
            text: "Cancel"
            enabled: false
            onClicked: {
                workerThread.safelyRequestInterruption()
                workerThread.destroy()
                workerThread = null
                enabled = false
                startButton.enabled = true
                print("canceled")
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