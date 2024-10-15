import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

// 2. Import the class

import examples.logger


ApplicationWindow {

    visible: true
    width: 400
    height:200
    title: "Template App"
    
    Logger {
        id: logger
    }

    RowLayout {
        
        anchors.fill: parent
        
        Button {
        
            Layout.fillWidth: true
            Layout.fillHeight: true
            
            text: "Click Me!"
            
            // 3. Connect Qml Button.clicked signal 
            //    to Logger.log slot
            
            onClicked: {
                logger.log("You clicked me!")
            }
        }
    }
}