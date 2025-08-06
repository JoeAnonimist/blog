import QtQuick
import QtQuick.Controls

ApplicationWindow {

    id: appWindow

    visible: true
    width: 300
    height:200
    title: "QML object properties"
    
    property QtObject myColors: QtObject {
        property color mistyRose: "mistyrose"
        property color honeyDew: "honeydew"
        property color aliceBlue: "aliceblue"
    }
    
	property color backgroundColor:
	    if (width > height) myColors.mistyRose
	    else if (width < height) myColors.honeyDew
	    else myColors.aliceBlue
    
    Logger {
        id: myLogger
    }
    
    Rectangle {

        width: appWindow.width
        height: appWindow.height
        color: appWindow.backgroundColor
        
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