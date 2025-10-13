import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {

    visible: true
    width: 200
    height: 400
    title: "Editable ListModel"
    
    ColumnLayout {
    
        anchors.fill: parent
        anchors.margins: 4
    
	    ListView {
	    
	        id: listView
	
	        Layout.fillWidth: true
	        height: 250
	        anchors.margins: 4
	        spacing: 4
	        focus: true
	        
	        highlightFollowsCurrentItem: true
	        highlight: Rectangle {
	            height: 40; width: 200
	            color: "#0078d7"; opacity: 0.2
	        }
	
	        ScrollBar.vertical: ScrollBar {}
	        
	        model: Model { id: listModel }
	
	        delegate: Delegate {}
	    }
	    
        Button {
            Layout.fillWidth: true
            text: "Append new"
            onClicked: () => {
                listModel.append({"value": "<new>"})
                listView.currentIndex = listModel.count - 1
                listView.positionViewAtIndex(listView.currentIndex, ListView.End)
                listView.focus = true
                
            }
        }
        
        Button {
            Layout.fillWidth: true
            text: "Insert new"
            onClicked: () => {
	            var currentIndex = listView.currentIndex
	            if (currentIndex < 0) currentIndex = 0
	            listModel.insert(currentIndex, {"value": "<new>"})
	            listView.positionViewAtIndex(currentIndex, ListView.Center)
	            listView.focus = true
            }
        }
        
        Button {
            Layout.fillWidth: true
            enabled: listModel.count > 0
            text: "Remove current"
            onClicked: () => {
                if (listModel.count > 0) {
	                listModel.remove(listView.currentIndex)
	                if (listView.currentIndex == listModel.count) {
	                    listView.currentIndex = listView.currentIndex - 1
	                } 
	                listView.focus = true
	            }
            }
        }	    
	}
}