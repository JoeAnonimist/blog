import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    visible: true
    width: listView.implicitWidth
    height: listView.implicitHeight
    title: "ObjectModel"
    
    ObjectModel {
        id: objectModel
        
        Rectangle { 
            height: 40; width: 200; 
            color: "#FFB6C1"
            border.width: 1;
            border.color: "#FF69B4"
        }
        Rectangle { 
            height: 40; width: 200; 
            color: "#98FB98"
            border.width: 1;
            border.color: "#32CD32"
        }
        Rectangle { 
            height: 40; width: 200; 
            color: "#FFE4B5"
            border.width: 1;
            border.color: "#FFD700"
        }
        Rectangle { 
            height: 40; width: 200; 
            color: "#E0FFFF"
            border.width: 1;
            border.color: "#00BFFF"
        }
        Rectangle { 
            height: 40; width: 200; 
            color: "#DDA0DD"
            border.width: 1;
            border.color: "#BA55D3"
        }
        Button {
            height: 40; width: 200
            text: "My Button"
            onClicked: () => {
                console.log("Clicked")
            }
        }
    }

    ListView {
        id: listView
        
        anchors.fill: parent
        model: objectModel
        
        implicitWidth: 200
        implicitHeight: count * (40 + spacing) - spacing
        
        spacing: 2
        
        focus: true
        highlightFollowsCurrentItem: true
        highlight: Rectangle {
            z: 100
            color: "black"
            border.width: 10
            border.color: "black"
            opacity: 0.2
        }
        
        ScrollBar.vertical: ScrollBar {}
        
        onCurrentIndexChanged: console.log(
            "Current index changed: " + currentIndex)
    }
}