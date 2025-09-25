import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {

    visible: true
    width: 300
    height:200
    title: "Display a colored Rectangle"
    
    Rectangle {

        anchors.centerIn: parent
        
        width: 100
        height: 100
        
        border {
            color: "steelblue"
            width: 2
        }
        
        radius: 6
        
        color: "lightsteelblue"
    }
}