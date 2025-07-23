import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {

    visible: true
    width: 200
    height:100
    title: "CheckBox example"
    
    function getState (cbox) {
        let stateName = {
            0: "Unchecked",
            1: "Partially Checked",
            2: "Checked"
        } [cbox.checkState]
        label.text = cbox.text + "\n" + stateName
    }
    
    ColumnLayout {
        
        anchors.fill: parent
            
        CheckBox {
            Layout.fillWidth: true
            text: "Windows"
            onCheckStateChanged: getState(this)
        }
        
        CheckBox {
            Layout.fillWidth: true
            text: "Linux"
            onCheckStateChanged: getState(this)
        }
        
        CheckBox {
            Layout.fillWidth: true
            text: "macOs"
            tristate: true
            onCheckStateChanged: getState(this)
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