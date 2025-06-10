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
        
            label: StackLayout {
                id: labelStack
                currentIndex: radioCheckable.checked ? 1 : 0

                Label {
                    text: "Group box"
                }

                CheckBox {
                    id: groupCheckBox
                    text: "Options"
                    checked: true
                    enabled: true
                    onCheckedChanged: groupBox.contentItem.enabled = checked
                }
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
}