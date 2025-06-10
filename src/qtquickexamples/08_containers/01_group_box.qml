import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {

    visible: true
    width: 400
    height:200
    title: "GroupBox"
    
    RowLayout {
        
        anchors.fill: parent
        anchors.margins: 10
        
        GroupBox {
        
            id: groupBox
            title: "???"
        
            label: Loader {
                id: labelLoader
                sourceComponent: radioCheckable.checked ? checkBoxComponent : labelComponent
            }
        
            Layout.fillWidth: true
            Layout.fillHeight: true

            ColumnLayout {
            
	            RadioButton {
	                text: "Option 1"
	                checked: true
	            }
	            
	            RadioButton {
	                id: radioCheckable
	                text: "Set checkable"
	            }
	            
	            RadioButton {
	                id: radioNonCheckable
                    text: "Set non-checkable"
	            }
            }
	    }

        Label {
            
            id: label
            text: "Option 1"

            Layout.fillWidth: true
            Layout.fillHeight: true
            
            horizontalAlignment: Text.AlignLeft
            verticalAlignment: Text.AlignVCenter
        }
    }

    Component {
        id: checkBoxComponent
        CheckBox {
            id: groupCheckBox
            text: "Group box"
            checked: true
            enabled: true
            onCheckedChanged: groupBox.contentItem.enabled = checked
        }
    }

    Component {
        id: labelComponent
        Label {
            text: "Group box"
        }
    }
}