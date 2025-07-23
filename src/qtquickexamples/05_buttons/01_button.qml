import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {

    visible: true
    width: 200
    height:80
    title: "Button Example"
    
    function generateRandNumber () {
        label.text = Math.floor(
            Math.random() * 100 + 1)
    }
    
    ColumnLayout {
        
        anchors.fill: parent
            
        Button {
        
            Layout.fillWidth: true
            Layout.alignment: Qt.AlignTop
            text: "Generate random number"
            
            onClicked: generateRandNumber()
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