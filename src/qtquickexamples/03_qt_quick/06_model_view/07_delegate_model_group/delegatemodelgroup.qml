import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQml.Models

ApplicationWindow {
    visible: true
    width: 320
    height: 500
    title: "DelegateModelGroup Demo"

    property var fsModel
    property var rootIndex

    Component.onCompleted: {
        if (!fsModel) {
            console.error("fsModel is not set!")
        } else {
            // Trigger initial categorization
            Qt.callLater(categorizeItems)
        }
    }

    function categorizeItems() {
        if (!fileDelegateModel.items) {
            console.warn("Items not ready yet")
            return
        }
        
        console.log("Categorizing", fileDelegateModel.items.count, "items")
        
        for (var i = 0; i < fileDelegateModel.items.count; i++) {
            var item = fileDelegateModel.items.get(i)
            var isDirectory = item.model.isDir === true
            
            item.inDirs = isDirectory
            item.inFiles = !isDirectory
            
            console.log("Item", i, ":", item.model.fileName, "isDir:", isDirectory)
        }
    }

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

        // Categorize items when model changes
        onCountChanged: {
            Qt.callLater(categorizeItems)
        }

        // This is called when items are inserted into the model
        filterOnGroup: undefined
        
        items.onChanged: {
            // When items change, recategorize
            Qt.callLater(categorizeItems)
        }
    }

    Connections {
        target: fsModel
        function onDirectoryLoaded(path) {
            console.log("Directory loaded:", path)
            fileDelegateModel.rootIndex = rootIndex
            Qt.callLater(categorizeItems)
        }
    }

    ColumnLayout {
        anchors.fill: parent
        spacing: 0

        // Filter buttons
        RowLayout {
            Layout.fillWidth: true
            Layout.margins: 4
            spacing: 4
            
            Button {
                text: "All (" + fileDelegateModel.count + ")"
                Layout.fillWidth: true
                Layout.preferredHeight: 36
                highlighted: fileDelegateModel.filterOnGroup === undefined
                onClicked: {
                    console.log("Showing all items")
                    fileDelegateModel.filterOnGroup = undefined
                }
            }
            Button {
                text: "Files (" + filesGroup.count + ")"
                Layout.fillWidth: true
                Layout.preferredHeight: 36
                highlighted: fileDelegateModel.filterOnGroup === "files"
                onClicked: {
                    console.log("Filtering to files only, count:", filesGroup.count)
                    fileDelegateModel.filterOnGroup = "files"
                }
            }
            Button {
                text: "Dirs (" + dirsGroup.count + ")"
                Layout.fillWidth: true
                Layout.preferredHeight: 36
                highlighted: fileDelegateModel.filterOnGroup === "dirs"
                onClicked: {
                    console.log("Filtering to dirs only, count:", dirsGroup.count)
                    fileDelegateModel.filterOnGroup = "dirs"
                }
            }
        }

        // Separator
        Rectangle {
            Layout.fillWidth: true
            Layout.preferredHeight: 1
            color: "#e0e0e0"
        }

        // File list
        ListView {
            id: listView
            Layout.fillWidth: true
            Layout.fillHeight: true
            model: fileDelegateModel

            focus: true
            clip: true
            highlightFollowsCurrentItem: true
            highlight: Rectangle {
                color: "#2196F3"
                opacity: 0.2
                radius: 4
            }

            ScrollBar.vertical: ScrollBar {
                policy: ScrollBar.AsNeeded
            }

            // Empty state
            Label {
                anchors.centerIn: parent
                text: "No items to display"
                visible: listView.count === 0
                color: "#999"
            }

            // Keyboard navigation
            Keys.onUpPressed: {
                if (currentIndex > 0) {
                    currentIndex--
                }
            }
            Keys.onDownPressed: {
                if (currentIndex < count - 1) {
                    currentIndex++
                }
            }
        }

        // Status bar
        Rectangle {
            Layout.fillWidth: true
            Layout.preferredHeight: 24
            color: "#f5f5f5"
            border.color: "#e0e0e0"
            border.width: 1

            Label {
                anchors.centerIn: parent
                text: listView.count + " item(s) | Files: " + filesGroup.count + " | Dirs: " + dirsGroup.count
                font.pixelSize: 11
                color: "#666"
            }
        }
    }

    component MyDelegate: Rectangle {
        id: root

        required property int index
        required property string fileName
        required property string filePath
        required property bool isDir

        implicitWidth: ListView.view ? ListView.view.width : 240
        implicitHeight: 44
        
        color: {
            if (ListView.isCurrentItem) return "transparent"
            return index % 2 === 0 ? "#fafafa" : "#f0f0f0"
        }

        // Hover effect
        Rectangle {
            anchors.fill: parent
            color: "#e3f2fd"
            opacity: mouseArea.containsMouse && !ListView.isCurrentItem ? 0.3 : 0
            visible: mouseArea.containsMouse && !ListView.isCurrentItem

            Behavior on opacity {
                NumberAnimation { duration: 150 }
            }
        }

        RowLayout {
            anchors.fill: parent
            anchors.leftMargin: 12
            anchors.rightMargin: 12
            spacing: 8

            // Icon
            Label {
                text: isDir ? "📁" : "📄"
                font.pixelSize: 20
            }

            // File name
            Label {
                text: fileName
                elide: Text.ElideMiddle
                Layout.fillWidth: true
                font.pixelSize: 13
            }

            // Directory indicator
            Label {
                text: "›"
                visible: isDir
                color: "#999"
                font.pixelSize: 16
            }
        }

        MouseArea {
            id: mouseArea
            anchors.fill: parent
            hoverEnabled: true
            
            onClicked: {
                root.ListView.view.currentIndex = index
                root.ListView.view.forceActiveFocus()
            }
            
            onDoubleClicked: {
                if (isDir) {
                    console.log("Navigate to:", filePath)
                    // TODO: Implement directory navigation
                }
            }
        }

        Rectangle {
            anchors.fill: parent
            color: "#000"
            opacity: mouseArea.pressed ? 0.05 : 0
            
            Behavior on opacity {
                NumberAnimation { duration: 100 }
            }
        }
    }
}