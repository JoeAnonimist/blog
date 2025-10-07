import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQml.Models


ApplicationWindow {

    id: window

    visible: true
    width: 600
    height: 400
    title: "Package Demo"

    property var fsModel
    property var rootIndex
    property int selectedIndex: -1

    Component {
        id: fileDelegateComponent
        
        Package {
            id: filePackage
            
            required property int index
            required property string fileName
            required property string filePath
            required property bool isDir
            
            Rectangle {
                Package.name: 'list'
                
                implicitWidth: 250
                implicitHeight: 40
                color: (window.selectedIndex === index) ? "#E3F2FD" :
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
                    onClicked: {
                        window.selectedIndex = index
                        listView.forceActiveFocus()
                        console.log("ListView clicked: " + fileName + " (isDir: " + isDir + ")")
                    }
                }
            }
            
            Rectangle {
                Package.name: 'grid'
                
                implicitWidth: 120
                implicitHeight: 80
                color: (window.selectedIndex === index) ? "#E3F2FD" :
                       (index % 2 === 0 ? "#f0f0f0" : "#dcdcdc")
                
                ColumnLayout {
                    anchors.fill: parent
                    anchors.margins: 8
                    
                    Image {
                        source: isDir ? "folder.png" : "file.png"
                        width: 48
                        height: 48
                        fillMode: Image.PreserveAspectFit
                        Layout.alignment: Qt.AlignHCenter
                    }
                    Label { 
                        text: fileName
                        elide: Text.ElideRight
                        horizontalAlignment: Text.AlignHCenter
                        Layout.fillWidth: true
                    }
                }
                
                MouseArea {
                    anchors.fill: parent
                    onClicked: {
                        window.selectedIndex = index
                        gridView.forceActiveFocus()
                        console.log("GridView clicked: " + fileName + " (isDir: " + isDir + ")")
                    }
                }
            }
        }
    }
    
    DelegateModel {

        id: fileDelegateModel

        model: fsModel
        rootIndex: rootIndex
        delegate: fileDelegateComponent
    }
    
    Connections {
        target: fsModel
        function onDirectoryLoaded(path) {
            fileDelegateModel.rootIndex = rootIndex
        }
    }

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 8
        
        Label {
            text: "File System Browser Demo (Synced Selection)"
            font.bold: true
            Layout.alignment: Qt.AlignHCenter
            Layout.bottomMargin: 8
        }

        Rectangle {
            Layout.fillWidth: true
            height: 1
            color: "#ccc"
        }

        RowLayout {
            Layout.fillWidth: true
            Layout.fillHeight: true
            
            ListView {
                id: listView
                Layout.preferredWidth: 250
                Layout.fillHeight: true
                model: fileDelegateModel.parts.list
                clip: true
                
                focus: true
                highlightFollowsCurrentItem: false  // Use custom selection color
                
                ScrollBar.vertical: ScrollBar {}
                
                onCurrentIndexChanged: {
                    console.log("ListView: Current index changed: " + currentIndex)
                }
            }
            
            Rectangle {
                Layout.preferredWidth: 1
                Layout.fillHeight: true
                color: "#ccc"
            }
            
            GridView {
                id: gridView
                Layout.fillWidth: true
                Layout.fillHeight: true
                model: fileDelegateModel.parts.grid
                cellWidth: 120
                cellHeight: 80
                clip: true
                
                focus: true
                highlightFollowsCurrentItem: false
                
                ScrollBar.vertical: ScrollBar {}
                
                onCurrentIndexChanged: {
                    console.log("GridView: Current index changed: " + currentIndex)
                }
            }
        }
    }
}