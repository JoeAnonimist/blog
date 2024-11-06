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
    //    onFilenameChanged: Automatic handler!
    
    Logger {
        id: logger
        onFilenameChanged: {
            console.log("The filenameChanged signal emitted");
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
            
            // 3. Use the property

            onClicked: {
                logger.filename = "03_property.qml";
                console.log(logger.filename);
            }
        }
    }
}