import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {

    visible: true
    width: 400
    height:200
    title: "ScrollView"
    
    RowLayout {
        
        anchors.fill: parent

        ScrollView {

            Layout.fillWidth: true
            Layout.fillHeight: true

            ScrollBar.horizontal.policy: ScrollBar.AlwaysOn
            ScrollBar.vertical.policy: ScrollBar.AlwaysOn 

            TextArea {
                text: "123"
                focus: true
    
                anchors.fill: parent
                
                background: Rectangle {
                    color: "#BEB4E5"
                }
            }
        }
    }
}