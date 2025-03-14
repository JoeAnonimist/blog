import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

// 1. Use the QML_IMPORT_NAME value
//    to import the Logger class    

import examples.logger

ApplicationWindow {

    visible: true
    width: 400
    height:200
    title: "Template App"
    
    // 2. Create a Logger object
    
    Logger {
        id: logger
        // 3. the signal name follows a convention:
        //    messageLogged handler name becomes onMessageLogged 
        onMessageLogged: {
            console.log("The messageLogged signal emitted");
        }
    }

    RowLayout {
        
        anchors.fill: parent
            
        Button {
            text: "Click me!"

            Layout.fillWidth: true
            Layout.fillHeight: true
            
            font.pointSize:24
            font.bold: true
            
            onClicked: {
                logger.log("Log message")
            }
        }
    }
}