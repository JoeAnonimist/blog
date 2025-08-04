import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {

    visible: true
    width: 400
    height:200
    title: "Template App"
    
    RowLayout {
        
        anchors.fill: parent
            
        Label {
        
            id: label
            objectName: "label"
        
            text: "Hello Qml!"

            Layout.fillWidth: true
            Layout.fillHeight: true
            
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            
            font.pointSize:24
            font.bold: true
            color: "steelblue"
            
            // 1. Add a slot function to the label
            
            function updateText () {
                label.text = "Timeout event\n"
                    + Qt.formatTime(new Date, "hh:mm:ss")
            }
        }
    }
}