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
        
        width: parent.width / 2
        height: parent.height / 2
        
        color: "lightsteelblue"
        
        BorderImage {
            source: "image.png"
            anchors.fill: parent
            border {
                top: 10
                left: 4
                right: 4
                bottom: 4
            }
            horizontalTileMode: BorderImage.Stretch
            verticalTileMode: BorderImage.Stretch
        }
    }
}