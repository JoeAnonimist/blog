import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import examples.logger

ApplicationWindow {

    visible: true
    width: 400
    height:200
    title: "Template App"

    Logger {
    
        id: logger
        objectName: "myLogger"
        message: "Log message"
        Logger.severity: 1
        Logger.filename: "filename.qml"
        
        onMessageChanged: function (msg) {
            console.log("Message changed: ", msg);
        }
        
        Logger.onFilenameChanged: (filename) => {
            console.log("In filename handler: ", filename)
        }

        Logger.onSeverityChanged: (severity) => {
                console.log("In severity event handler: ", severity)
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
                logger.message = "Some message";
                logger.Logger.severity = logger.Logger.severity + 1
                logger.Logger.filename = "10_attached_properties.qml";
                console.log(logger.Logger.severity);
            }
        }
    }
}