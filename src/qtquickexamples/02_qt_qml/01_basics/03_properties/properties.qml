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
	    severity: 4
	    filename: "properties.qml"
	}

    Rectangle {

        anchors.fill: parent
        color: "ghostwhite"
        
        Button {
        
            text: appWindow.title + " example"
            anchors.centerIn: parent
            
            width: implicitWidth + 10
            height: 50
            
            onClicked: () => {
                console.log(myLogger.severity)
                console.log(myLogger.filename)
            }
        }
    }
}