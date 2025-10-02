import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {

    visible: true
    width: 250
    height: 250
    title: "Panning"

    Flickable {
    
        anchors.fill: parent
        
        contentWidth: 400
        contentHeight: 400
        flickableDirection: Flickable.HorizontalAndVerticalFlick
        clip: true
        
        Rectangle {
        
            width: 400
            height: 400
            color: "lightsteelblue"
            border.color: "steelblue"
            
            Text {
                
                anchors.centerIn: parent
                text: "Scroll me!"
                font.pixelSize: 24
            }
        
        }

	}
}
