import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQml.Models


ApplicationWindow {

    id: appWindow

    visible: true
    width: 300
    height: 400
    title: "DelegateModelGroup Example"

    property var fsModel
    property var rootIndex
    property bool showFiles: false

    DelegateModel {

        id: fileDelegateModel

        model: fsModel
        //rootIndex: appWindow.rootIndex
        delegate: MyDelegate {}
        
        groups: [
            DelegateModelGroup {
                id: filesGroup
                name: "files"
                includeByDefault: false
            },
            DelegateModelGroup {
                id: dirsGroup
                name: "dirs"
                includeByDefault: false
            }
        ]
        
        filterOnGroup: showFiles ? "files" : "dirs"
        
        items.onChanged: () => {
            for (var i = 0; i < items.count; i++) {
                var item = items.get(i)
                console.log(item.model.fileName, item.model.isDir)
                if (item.model.isDir === true) {
                    item.inDirs = true
                } else if (item.model.isDir === false) {
                    item.inFiles = true
                } else {
                    console.log("AAAAAAAaaaaaaa!")
                }
            }
        }
    }
    
    Connections {
        target: fsModel
        function onDirectoryLoaded(path) {
            fileDelegateModel.rootIndex = rootIndex
        }
    }

    Column {
        anchors.fill: parent
        spacing: 10
        padding: 10

        Row {
            spacing: 10

            Button {
                text: "Show Files"
                onClicked: showFiles = true
            }

            Button {
                text: "Show Directories"
                onClicked: showFiles = false
            }
            
            Label {
                anchors.verticalCenter: parent.verticalCenter
                text: "Count: " + listView.count
            }
        }

        ListView {

            id: listView
            
            model: fileDelegateModel
            
            width: parent.width - 20
            height: parent.height - 80
            
            clip: true
            focus: true
            highlightFollowsCurrentItem: true
            highlight: Rectangle {
                color: "orange"
                opacity: 0.2
            }
            
            ScrollBar.vertical: ScrollBar {}
            
            onCurrentIndexChanged: () => {
                console.log("Current index changed: " + currentIndex)
                var item = itemAtIndex(currentIndex)
                console.log(item.model.fileName)
            }
        }
    }
    
    component MyDelegate: Rectangle {
    
        id: root
        
        required property var model
        required property int index
        required property string fileName
        required property string filePath
        required property bool isDir

        width: ListView.view.width
        height: 40
        color: ListView.isCurrentItem ? "transparent" :
               (ListView.index % 2 === 0 ? "#f0f0f0" : "#dcdcdc")
        
        RowLayout {
            anchors.fill: parent
            anchors.margins: 8
            
            Label { 
                text: fileName + (isDir ? " [DIR]" : " [FILE]")
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
    }
}