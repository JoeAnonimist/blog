import QtQuick
import QtQuick.Controls

ApplicationWindow {

    id: appWindow

    visible: true
    width: 300
    height:200
    title: "QML grouped properties"
    
    Logger {
        id: myLogger
        message: "Some message"
        details.severity: 5
        details.filename: "grouped_properties.qml"
    }
    
    Rectangle {

        anchors.fill: parent
        color: "ghostwhite"
        
        Button {
        
            text: appWindow.title + " example"
            anchors.centerIn: parent

            font.pixelSize: 14
            font.bold: true

            width: implicitWidth + 10
            height: 50

            onClicked: () => {
                console.log(myLogger.message)
                console.log(myLogger.details.severity)
                console.log(myLogger.details.filename)
            }
        }
    }
}