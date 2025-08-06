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

        }
    }
    
    Component.onCompleted: {
        myLogger.details.severity = 3
        myLogger.log("Some message")
    }
}
