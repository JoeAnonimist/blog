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
        message: "Log message"
        Logger.severity: 1
        Logger.filename: "filename.qml"
        
        onMessageChanged: function (msg) {
            console.log("Message changed: ", msg);
        }
    }
    
    Connections {
        target: logger.Logger // The attached LogDetails instance
        function onSeverityChanged(severity) {
            console.log("Severity changed: ", severity)
        }
        function onFilenameChanged(filename) {
            console.log("File name changed: ", filename)
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
                Logger.severity = Logger.severity + 1
                Logger.filename = "10_attached_properties.qml";
                console.log(Logger.severity);
                console.log(logger.message);
            }
        }
    }
}