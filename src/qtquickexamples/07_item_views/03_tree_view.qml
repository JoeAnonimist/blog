import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {

    visible: true
    width: 600
    height: 400
    title: "TreeView QFileSystemModel"
    
    property variant fsmodel
    property variant home_index
    
    Item {
    
        anchors.fill: parent

	    HorizontalHeaderView {
            id: horizontalHeader
            anchors.top: parent.top
            anchors.left: treeView.left
            syncView: treeView
            model: ["Name", "Size", "Type", "Date Modified"]
            clip: true
            resizableRows: true
	    }

	    TreeView {
	    
	        id: treeView
            anchors.top: horizontalHeader.bottom
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.bottom: parent.bottom
            //anchors.margins: 10
	
	        model: fsmodel
	        rootIndex: home_index
	        
	        alternatingRows: false
	        
	        delegate: TreeViewDelegate {
	            Component.onCompleted: {
	                console.log("completed")
	                console.log(fileIcon)
	            }	
	        }
	        ScrollBar.vertical: ScrollBar {}
	        ScrollBar.horizontal: ScrollBar {}
	    }
	}
}
