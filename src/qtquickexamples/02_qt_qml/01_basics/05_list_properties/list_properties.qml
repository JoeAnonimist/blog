import QtQuick
import QtQuick.Controls

ApplicationWindow {

    id: appWindow

    visible: true
    width: 300
    height:200
    title: "QML object properties"
    
    Logger {
    
        id: myLogger
        
        message: "Some message"
        details.severity: 3
        details.filename: "list_properties.qml" 
        
        targets: [
            ConsoleLogTarget {},
            PopupLogTarget {},
            FileLogTarget {}
        ]
    }
    
    Rectangle {
    
        id: backgroundRect

        anchors.fill: parent
        color: "ghostwhite"
        
        Button {
        
            text: appWindow.title + " example"
            anchors.centerIn: parent
            
            width: implicitWidth + 10
            height: 50
            
            onClicked: () => {
                let currTime = Qt.formatTime(
                    new Date() , "hh:mm:ss") 
                myLogger.log(
                    myLogger.details.severity,
                    "Logging at: " + currTime, 
                    myLogger.details.filename)
            }
        }
    }
}
