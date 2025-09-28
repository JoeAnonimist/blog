import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {

    visible: true
    title: "Column positioner"
    width: column.implicitWidth + 10
    height: column.implicitHeight + 10
    
    Column {
    
        id: column
        spacing: 5
        anchors.centerIn: parent

        Repeater {

            model: 3

            Rectangle {
            
                objectName: "rect" + index
            
                // Does not work in a column
                //anchors.centerIn: parent
                width: 80
                height: 30
                border.color: "steelblue"
                radius: 1
                color: "#d0d0d0"
                
                Text {
                    anchors.centerIn: parent
                    text: parent.objectName
                }
                
                MouseArea {
                    anchors.fill: parent
                    onClicked: () => {
                        print("Rectangle clicked: " +
                        parent.objectName)
                    }
                }
            }
        }
    }
}