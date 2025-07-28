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
        }
        function onError (message) {
            print(message)
        }
    }

    ColumnLayout {
        
        anchors.fill: parent
        
        Button {
            
            Layout.fillWidth: true
            text: "Start background thread"
            
            onClicked: {
                controller.run_task()
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