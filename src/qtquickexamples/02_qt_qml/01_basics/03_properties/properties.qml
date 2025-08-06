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
	    
	Logger {
	    id: myLogger
	}

    Rectangle {

        anchors.fill: parent
        color: appWindow.backgroundColor
        
        Button {
        
            text: appWindow.title + " example"
            anchors.centerIn: parent
            width: implicitWidth + 10
            height: 50
        }
    }
    
	Component.onCompleted: () => {
	    print(myLogger.filename)
	    myLogger.filename = "properties.gml"
	    print("myLogger.filename = ", myLogger.filename)
	}
}