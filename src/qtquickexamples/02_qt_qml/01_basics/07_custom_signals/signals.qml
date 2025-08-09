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
	    
	    onLogged: (now) => {
	        console.log("Logger.logged emitted: ",
	            Qt.formatTime(new Date(), "hh:mm:ss"))
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
                myLogger.severity = Math.floor(Math.random() * 6)
                myLogger.filename = "signals.qml"
                myLogger.log()
            }
        }
    }
    
    Component.onCompleted: () => {
        console.log(myLogger.logged)
        console.log(myLogger.onLogged)
    }
}