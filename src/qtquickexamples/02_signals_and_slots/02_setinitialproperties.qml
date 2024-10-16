import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {

    id: mainWindow

    visible: true
    width: 400
    height:200
    title: "Template App"
    
    // 1. Add a property named timer to the root object
    
    property variant timer
    
    RowLayout {
        
        anchors.fill: parent
            
        Label {
        
            id: label
        
            text: "Hello Qml!"

            Layout.fillWidth: true
            Layout.fillHeight: true
            
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            
            font.pointSize:24
            font.bold: true
            color: "steelblue"
            
            // 3. Use the Qml Connections type to connect
            //    QTimer.timeout to the Qml slot
            //    Target is the slot owner (ie QTimer)
            //    and the slot name, onTimeout matches
            //    the signal name, timeout
            
            Connections {
            
                target: mainWindow.timer
                
                function onTimeout () {
                    label.text = 
                        Qt.formatTime(new Date, "hh:mm:ss")
                }
            }
        }
    }
}