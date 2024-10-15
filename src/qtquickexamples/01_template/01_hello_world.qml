import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

// 1. Create an instance of 
//    the ApplicationWindow Qml type

ApplicationWindow {

    visible: true
    width: 400
    height:200
    title: "Template App"
    
    // 2. Add a layout to the application window
    //    and add a Label Qml type instance to it.
    
    RowLayout {
        
        anchors.fill: parent
            
        Label {
        
            text: "Hello Qml!"

            Layout.fillWidth: true
            Layout.fillHeight: true
            
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            
            font.pointSize:24
            font.bold: true
            color: "steelblue"

        }
    }
}