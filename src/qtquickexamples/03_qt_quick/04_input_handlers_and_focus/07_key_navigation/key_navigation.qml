import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {

    visible: true
    title: "Key Navigation"
    width: grid.implicitWidth + 10
    height: grid.implicitHeight + 10
    
    Grid {
    
        id: grid
        spacing: 5
        anchors.centerIn: parent
        
        columns: 2
        
        Rectangle {
            width: 100; height: 30
            border.color: "steelblue"; color: "#d0d0d0"
        }
        
        Rectangle {
        
            id: first

            width: 120; height: 30
            border.color: focus ? "orange" : "steelblue"
            focus: true
            
            Text {
                anchors.centerIn: parent; text: "Value 1"
            }
            
            KeyNavigation.up: third
            KeyNavigation.down: second
        }

        Rectangle {
            width: 100; height: 30
            border.color: "steelblue"; color: "#d0d0d0"
        }
        
        Rectangle {
        
            id: second

            width: 120; height: 30
            border.color: focus ? "orange" : "steelblue"
            
            Text {
                anchors.centerIn: parent; text: "Value 2"
            }
            KeyNavigation.up: first
            KeyNavigation.down: third
        }

        Rectangle {
            width: 100; height: 30
            border.color: "steelblue"; color: "#d0d0d0"
         }
        
        Rectangle {
        
            id: third

            width: 120; height: 30
            border.color: focus ? "orange" : "steelblue"
            
            Text {
                anchors.centerIn: parent; text: "Value 3"
            }
            KeyNavigation.up: second
            KeyNavigation.down: first
        }
    }
}