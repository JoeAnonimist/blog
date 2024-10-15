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
        
        Button {
            
            // 1. Make the button available to Python
            //    by giving it a name
            
            objectName: "button"
            
            Layout.fillWidth: true
            Layout.fillHeight: true
            
            text: "Click Me!"
        }
    }
}