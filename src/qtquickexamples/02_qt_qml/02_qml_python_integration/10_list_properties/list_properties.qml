import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import examples.logger
import examples.logger.logtargets

ApplicationWindow {

    visible: true
    width: 400
    height:200
    title: "Template App"

    Logger {
        id: logger
        targets: [
            ConsoleLogTarget {},
            PopupLogTarget {},
            FileLogTarget {}
        ]
    }

    RowLayout {
        
        anchors.fill: parent
            
        Button {
            text: "Click me!"

            Layout.fillWidth: true
            Layout.fillHeight: true
            
            font.pointSize:24
            font.bold: true

            onClicked: () => {
                let currTime = Qt.formatTime(
                    new Date(), "hh:mm:ss")
                logger.severity = 3
                logger.filename = "list_properties.qml";
                logger.log(
                    logger.severity,
                    "Logging at: " + currTime,
                    logger.filename);
            }
        }
    }
}