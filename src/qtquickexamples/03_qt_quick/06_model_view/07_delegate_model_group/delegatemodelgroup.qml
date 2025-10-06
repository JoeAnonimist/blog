import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQml.Models


ApplicationWindow {

    visible: true
    width: listView.implicitWidth
    height: 300
    title: "DelegateModelGroup"

    property var fsModel
    property var rootIndex

    DelegateModel {

        id: fileDelegateModel

        model: fsModel
        delegate: MyDelegate {}
        
        items.includeByDefault: false
        
        groups: [
            DelegateModelGroup {
                id: filesGroup
                name: "files"
            },
            DelegateModelGroup {
                id: dirsGroup
                name: "dirs"
            }
        ]
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
        model: dirsGroup
        
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
        
        required property var model
        required property int index
        required property string fileName
        required property string filePath
        required property bool isDir

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
                    "current index " + index +
                    ", name " + fileName)
				    console.log(isDir)
            }
        }
        
        Component.onCompleted: () => {
            DelegateModel.inFiles = !isDir
            DelegateModel.inDirs = isDir
        }
    }
}