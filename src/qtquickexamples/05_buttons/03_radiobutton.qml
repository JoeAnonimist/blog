import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {

    id: root

    visible: true
    width: 200
    height:100
    title: "RadioButton example"
    
    function getState (btn) {
        label.text = btn.text
        labelbg.color = btn.text
    }
    
    ColumnLayout {

        anchors.fill: parent
            
        RadioButton {
            Layout.fillWidth: true
            text: "red"
            onToggled: getState(this)
        }
        
        RadioButton {
            Layout.fillWidth: true
            text: "green"
            onToggled: getState(this)
        }
        
        RadioButton {
            Layout.fillWidth: true
            text: "blue"
            onToggled: getState(this)
        }
        
        Label {

            id: label
            
            background: Rectangle {
                id: labelbg
                color: root.color
            }
            
            Layout.fillWidth: true
            Layout.fillHeight: true
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
        }
    }
}