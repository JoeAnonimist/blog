import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {

    visible: true
    width: 400
    height:200
    title: "Template App"
    
    LoggingCategory {
        id: c1
        name: "ignoreme"
    }
    
    Component.onCompleted: {
        console.log(c1, "")
    }

    RowLayout {
        
        anchors.fill: parent
            
        Button {
        
            objectName: "button"
            text: "Click me!"

            Layout.fillWidth: true
            Layout.fillHeight: true
            
            font.pointSize:24
            font.bold: true
            
            property var logger

            onClicked: {
                logger.log("Message from QML");
            }
        }
    }
}