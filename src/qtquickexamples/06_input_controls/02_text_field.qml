import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {

    id: root

    visible: true
    width: 200
    height:100
    title: "TextField example"

    ColumnLayout {

        anchors.fill: parent
            
        TextField {
                        
            Layout.fillWidth: true
            validator: RegularExpressionValidator {
                regularExpression: /^[a-zA-Z]*$/
            }
            onTextEdited: { 
                label.text = text
            }
        }
        
        Label {

            id: label
            
            Layout.fillWidth: true
            Layout.fillHeight: true
            verticalAlignment: Text.AlignVCenter
        }
    }
}