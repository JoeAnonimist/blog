import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {

    visible: true
    title: "Row positioner"
    width: column.implicitWidth + 10
    height: column.implicitHeight + 10
    
    Row {
    
        id: column
        spacing: 5
        anchors.centerIn: parent

        Rectangle {
        
            id: rect1

            width: 100
            height: 30
            border.color: "steelblue"
            radius: 1
            color: "#d0d0d0"
            
            Text {
                anchors.centerIn: parent
                text: "What's the time"
            }
            
            MouseArea {
                anchors.fill: parent
                onClicked: () => {
                    timeText.text = Qt.formatDateTime(
                        new Date(), "hh:mm:ss")
                }
            }
        }
        
        Text {
            id: timeText
            width: 100
            height: 30
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
        }
    }
}