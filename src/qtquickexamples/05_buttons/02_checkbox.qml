import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {

    visible: true
    width: 200
    height:80
    title: "CheckBox example"
    
    function getState (cbox) {
        console.log(cbox.text)
    }
    
    ColumnLayout {
        
        anchors.fill: parent
            
        CheckBox {
            text: "Windows"
            onCheckedChanged: getState(this)
        }
        
        CheckBox {
            text: "Linux"
            onCheckedChanged: getState(this)
        }
        
        CheckBox {
            text: "macOs"
            tristate: true
            onCheckedChanged: getState(this)
        }
        
        Label {

            id: label
            
            Layout.fillWidth: true
            Layout.fillHeight: true
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
        }
    }
}