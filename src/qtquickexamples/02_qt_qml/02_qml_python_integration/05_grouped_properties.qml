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
        message: "Log message"
        details {
            severity: 1
            filename: "filename.qml"
        }
        
        onMessageChanged: function (msg) {
            console.log("Message changed: ", msg);
        }
            
        details.onSeverityChanged: function (severity) {  
            console.log("Severity changed: ", severity);
        }
        
        details.onFilenameChanged: function (filename) {
            console.log("File name changed: ", filename);
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
            
            // 3. Use the grouped properties

            onClicked: {
                logger.message = "Some message";
                logger.details.severity = 5
                logger.details.filename = "05_grouped_properties.qml";
                console.log(logger.details.severity);
                console.log(logger.details.filename);
                console.log(logger.message);
            }
        }
    }
}