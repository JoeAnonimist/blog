import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {

    id: root

    visible: true
    width: 200
    height:100
    title: "RadioButton example"
    
    function getState () {
        [label.color, labelbg.color] = 
        [String(labelbg.color), String(label.color)]
    }
    
    ColumnLayout {

        anchors.fill: parent
            
        Switch {
            id: themeSwitch
            Layout.fillWidth: true
            text: "Switch theme"
            onCheckedChanged: getState(this)
        }
        
        Label {

            id: label
            text: "Some label"
            font.pixelSize: 16
            font.bold: true
            color: "lightsteelblue"
            
            background: Rectangle {
                id: labelbg
                color: "darkblue"
            }
            
            Layout.fillWidth: true
            Layout.fillHeight: true
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
        }
    }
}