import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQml.Models

// https://forum.qt.io/topic/121818/how-to-make-qfilesystemmodel-work-with-a-listview/2


ApplicationWindow {

    visible: true
    width: listView.implicitWidth
    height: 300
    title: "File System ListView"

    property var fsModel
    property var rootIndex

    DelegateModel {

        id: fileDelegateModel

        model: fsModel
        delegate: MyDelegate {}
    }
    
    Connections {
        target: fsModel
        function onDirectoryLoaded(path) {
            fileDelegateModel.rootIndex = rootIndex
        }
    }


    ListView {
        id: listView
        
        anchors.fill: parent
        model: fileDelegateModel
        
        implicitWidth: 200
        implicitHeight: count * 40
        
        focus: true
        highlightFollowsCurrentItem: true
        highlight: Rectangle {
            color: "orange"
            opacity: 0.2
        }
        
        ScrollBar.vertical: ScrollBar {}
        
        onCurrentIndexChanged: () => {
            console.log("Current index changed: " + currentIndex)
        }
    }
    
    component MyDelegate: Rectangle {
    
        id: root
        
        required property int index
        required property string fileName
        required property string filePath

        width: 200
        height: 40
        color: ListView.isCurrentItem ? "transparent" :
               (ListView.index % 2 === 0 ? "#f0f0f0" : "#dcdcdc")
        
        RowLayout {
            anchors.fill: parent
            anchors.margins: 8
            
            Label { 
                text: fileName
                Layout.fillWidth: true
            }
        }
        
        MouseArea {
            anchors.fill: parent
            onClicked: {
                root.ListView.view.currentIndex = index
                console.log("Clicked: " +
                    "Current index: " + index +
                    " Name: " + fileName + " Path: " + filePath)
            }
        }
    }
}