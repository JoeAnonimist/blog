import QtQuick
import QtQuick.Controls

ApplicationWindow {

    id: appWindow

    visible: true
    width: 300
    height:200
    title: "QML object properties"
    
	property color backgroundColor:
	    if (width > height) "mistyrose"
	    else if (width < height) "honeydew"
	    else "aliceblue"

    Rectangle {

        width: appWindow.width
        height: appWindow.height
        color: appWindow.backgroundColor
        
        Button {
            text: appWindow.title + " example"
            x: (appWindow.width - width) / 2
            y: (appWindow.height - height) / 2
            width: implicitWidth + 10
            height: 50
        }
    }
}