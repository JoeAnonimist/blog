import QtQuick
import QtQuick.Controls

ApplicationWindow {

    visible: true
    width: 200
    height:200
    title: "QML Object Declaration"
    
    Logger {
    }
            
    Rectangle {

        height: 200
        width: 200
        color: "ghostwhite"
        
        Button {
            text: "Hello Qml!"
            x: 50
            y: 75
            width: 100
            height: 50
        }
    }
}