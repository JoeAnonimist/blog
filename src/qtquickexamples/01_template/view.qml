import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {

    visible: true
    width: 400
    height:200
    title: "Template App"

    RowLayout {
        
        anchors.fill: parent
            
        Label {
        
            text: "Hello Qml!"

            Layout.fillWidth: true
            Layout.fillHeight: true
            
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            
            font.pointSize:24
            font.bold: true
            color: "steelblue"

        }
    }
}