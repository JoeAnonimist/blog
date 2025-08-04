import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {

    id: root

    visible: true
    width: 300
    height:180
    title: "SpinBox and Dial example"

    ColumnLayout {

        anchors.fill: parent
            
        SpinBox {
            
            id: spinBox

            Layout.fillWidth: true
            from: 0
            to: 100
            stepSize: 5
            onValueChanged: {
                dial.value = value
                label.text = value
            }
        }
        
        Dial {
        
            id: dial
            
            Layout.fillWidth: true
            from: 0
            to: 100
            onValueChanged: spinBox.value = value
        }
        
        Label {

            id: label
            
            Layout.fillWidth: true
            Layout.fillHeight: true
            verticalAlignment: Text.AlignVCenter
        }
    }
}