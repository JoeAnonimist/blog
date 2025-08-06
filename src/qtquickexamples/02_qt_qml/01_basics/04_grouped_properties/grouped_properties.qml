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
        }
    }

	Component.onCompleted: () => {

	    myLogger.message = "Some message"
	    myLogger.details.severity = 5
	    myLogger.details.filename = "grouped_properties.qml"
	    
	    print(myLogger.message)
	    print(myLogger.details.severity)
	    print(myLogger.details.filename)
	}
}