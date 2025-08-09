import QtQuick
import QtQuick.Controls

ApplicationWindow {

    id: appWindow

    visible: true
    width: 300
    height:200
    title: "QML object signals"
	    
	Logger {

	    id: myLogger
	    
	    onMessageChanged: () => {
            console.log("Message changed :", message)
        }
        
        onSeverityChanged: () => {
            console.log("Severity changed :", severity)
        }
        
        onFilenameChanged: () => {
            console.log("File name changed :", filename)
        }
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
                myLogger.message = "Some message"
                myLogger.severity = Math.floor(Math.random() * 5)
                myLogger.filename = "signals.qml"
                myLogger.log()
            }
        }
    }
}