import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import examples.longRunningTask


ApplicationWindow {

    visible: true
    title: "Block Gui thread"
    
    Task {
        id: task
        onProgress: (file_name) => {
            label.text = file_name
            console.log(file_name)
        }
    }

    ColumnLayout {
        
        anchors.fill: parent
        
        Button {
            
            Layout.fillWidth: true
            text: "Start working"
            
            onClicked: {
                enabled = false
                task.do_work()
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