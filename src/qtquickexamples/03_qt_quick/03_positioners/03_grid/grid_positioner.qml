import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {

    visible: true
    title: "Grid positioner"
    width: grid.implicitWidth + 10
    height: grid.implicitHeight + 10
    
    Grid {
    
        id: grid
        spacing: 5
        anchors.centerIn: parent
        
        columns: 4
        
        Repeater {
            
            model: 16

            Rectangle {

                width: 100
                height: 30
                border.color: "steelblue"
                radius: 1
                color: "#d0d0d0"
                
                Text {
                    id: caption
                    anchors.centerIn: parent
                    text: "Row: " + Math.floor(parent.Positioner.index / grid.columns)
                    + " Col: " + (parent.Positioner.index % grid.columns)
                }
                
                MouseArea {
                    anchors.fill: parent
                    onClicked: {
                        console.log(caption.text)
                    }
                }
            }
        }
    }
}