import QtQuick
import QtQuick.Controls

ApplicationWindow {

    id: appWindow

    visible: true
    width: 300
    height:200
    title: "QML id attribute"
    
    Logger {
        id: myLogger
    }
            
    Rectangle {

        width: appWindow.width
        height: appWindow.height
        color: "ghostwhite"
        
        Button {
        
            text: appWindow.title + " example"

            x: (appWindow.width - width) / 2
            y: (appWindow.height - height) / 2

            width: implicitWidth + 10
            height: 50
            
            onClicked: () => {
                print(myLogger)
                print(myLogger.id)
            }
        }
    }
}