import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import examples.logger

ApplicationWindow {

    visible: true
    width: 400
    height:200
    title: "Template App"

    Connections {
        target: FileNameLogger
        function onFilenameChanged(fileName) {
            console.log("The filenameChanged signal emitted");
            console.log(fileName)
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
                FileNameLogger.filename = "09_singleton_create.qml";
                console.log(FileNameLogger.filename);
            }
        }
    }
}