import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQml.Models

ApplicationWindow {
    visible: true
    width: 240
    height: 400
    title: "DelegateModelGroup Demo"

    property var fsModel
    property var rootIndex

    DelegateModel {
        id: fileDelegateModel

        model: fsModel
        rootIndex: rootIndex
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
    }
    
    Connections {
        target: fsModel
        function onDirectoryLoaded(path) {
            fileDelegateModel.rootIndex = rootIndex
            Qt.callLater(function() {
                for (var i = 0; i < fileDelegateModel.items.count; i++) {
                    var item = fileDelegateModel.items.get(i)
                    item.inDirs = false
                    item.inFiles = false
                    item.inDirs = item.model.isDir
                    item.inFiles = !item.model.isDir
                }
            })
        }
    }

    ColumnLayout {
        anchors.fill: parent
        
        RowLayout {
            spacing: 1
            Button {
                text: "All"
                Layout.preferredWidth: 80
                onClicked: fileDelegateModel.filterOnGroup = undefined
            }
            Button {
                text: "Files"
                Layout.preferredWidth: 80
                onClicked: fileDelegateModel.filterOnGroup = "files"
            }
            Button {
                text: "Dirs"
                Layout.preferredWidth: 80
                onClicked: fileDelegateModel.filterOnGroup = "dirs"
            }
        }

        ListView {
            id: listView
            Layout.fillWidth: true
            Layout.fillHeight: true
            model: fileDelegateModel
            
            focus: true
            highlightFollowsCurrentItem: true
            highlight: Rectangle {
                color: "orange"
                opacity: 0.2
            }
            
            ScrollBar.vertical: ScrollBar {}
        }
    }
    
    component MyDelegate: Rectangle {
        id: root
        
        required property int index
        required property string fileName
        required property string filePath
        required property bool isDir

        implicitWidth: 240
        implicitHeight: 40
        color: ListView.isCurrentItem ? "transparent" :
               (index % 2 === 0 ? "#f0f0f0" : "#dcdcdc")
        
        RowLayout {
            anchors.fill: parent
            anchors.margins: 8
            
            Label { 
                text: fileName
                elide: Text.ElideRight
                Layout.fillWidth: true
            }
        }
        
        MouseArea {
            anchors.fill: parent
            onClicked: root.ListView.view.currentIndex = index
        }
    }
}