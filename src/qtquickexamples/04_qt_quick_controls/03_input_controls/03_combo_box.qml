import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {

    id: root

    visible: true
    width: 200
    height:100
    title: "ComboBox example"

    ColumnLayout {

        anchors.fill: parent
            
        ComboBox {
                        
            Layout.fillWidth: true
            editable: true
            
            model:  ["Linux", "Windows", "Mac", "Android"]
            
            onEditTextChanged: {
                labelTextChanged.text = editText
            }
            
            onActivated: {
                labelTextActivated.text = currentText
            }
        }
        
        Label {

            id: labelTextChanged
            
            Layout.fillWidth: true
            Layout.fillHeight: true
            verticalAlignment: Text.AlignVCenter
        }

        Label {

            id: labelTextActivated
            
            Layout.fillWidth: true
            Layout.fillHeight: true
            verticalAlignment: Text.AlignVCenter
        }
    }
}