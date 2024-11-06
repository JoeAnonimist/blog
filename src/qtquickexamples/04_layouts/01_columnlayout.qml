import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {

    visible: true
    width: 200
    height:300
    title: "Template App"

    ColumnLayout {
        
        anchors.fill: parent
            
        Button {
        
            objectName: "button1"
        
            text: "Button 1"

            Layout.fillWidth: true
            Layout.fillHeight: true
        }

        Button {
           
            objectName: "button2"
        
            text: "Button 2"

            Layout.fillWidth: true
            Layout.fillHeight: true
        }

        Button {
        
            objectName: "button3"
        
            text: "Button 3"

            Layout.fillWidth: true
            Layout.fillHeight: true
        }
    }
}