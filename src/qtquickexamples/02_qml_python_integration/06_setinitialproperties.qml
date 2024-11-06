import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {

    visible: true
    width: 400
    height:200
    title: "Template App"
    
    // 2. Add a property named logger to ApplicationWindow
    
    property var logger

    RowLayout {
        
        anchors.fill: parent
            
        Button {
            text: "Click me!"

            Layout.fillWidth: true
            Layout.fillHeight: true
            
            font.pointSize:24
            font.bold: true
            

            onClicked: {
                logger.filename = "06_setinitialproperties.qml";
                logger.log("Message from QML");
            }
        }
    }
}