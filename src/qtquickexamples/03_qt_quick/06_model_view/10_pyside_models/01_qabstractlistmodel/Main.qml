import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {

    visible: true
    width: 200
    height: 300
    title: "QAbstractListModel subclass as model"
    
    property var csvModel
    
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
	        clip: true
	        
	        highlightFollowsCurrentItem: true
	        highlightMoveDuration: 150
	        highlight: Rectangle {
	            height: 40; width: parent.width
	            color: "#0078d7"; opacity: 0.2
	        }
	
	        ScrollBar.vertical: ScrollBar { }
	        
	        model: csvModel
	
	        delegate: Delegate {}

		    Keys.onEnterPressed: () => {
		        valueField.forceActiveFocus()
		        console.log("focus")
		    }
		    Keys.onReturnPressed: () => {
		        valueField.forceActiveFocus()
		        console.log("focus")
		    }
	    }
	    
        RowLayout {

            Layout.fillWidth: true
            spacing: 6

            property int currentIndex: listView.currentIndex
            property bool hasSelection: {
                currentIndex >= 0 && currentIndex < listView.model.rowCount()
            }

            TextField {
                id: valueField
                Layout.fillWidth: true
                placeholderText: "Value"
                text: {
                    if (parent.hasSelection) {
                        console.log(listView.model.data(listView.model.index(parent.currentIndex, 0)))
                        const index = listView.model.index(parent.currentIndex, 0)
                        listView.model.data(index)
                    } else {
                        ""
                    }
                }
                onAccepted: {
                    if (parent.hasSelection) {
                        const index = listView.model.index(parent.currentIndex, 0) 
                        listView.model.setData(index , text)
                        listView.forceActiveFocus()
                    }
                }
            }

            Button {
                text: "➕"
                Layout.preferredWidth: implicitHeight
                onClicked: () => {
                    const row = listView.model.rowCount()
                    listView.model.insertRows(row, 1)
                    listView.currentIndex = listView.model.rowCount() - 1
                    listView.positionViewAtIndex(listView.currentIndex, ListView.Center)
	                const index = listView.model.index(parent.currentIndex, 0)
	                valueField.text = listView.model.data(index)
                    listView.forceActiveFocus()
                }
            }

            Button {
                text: "➖"
                enabled: listView.model.rowCount() > 0
                Layout.preferredWidth: implicitHeight
                onClicked: () => {
	                if (listView.model.rowCount() > 0) {
		                listView.model.removeRows(listView.currentIndex, 1)
		                if (listView.currentIndex == listView.model.rowCount()) {
		                    listView.currentIndex = listView.currentIndex - 1
		                }
		                const index = listView.model.index(parent.currentIndex, 0)
		                valueField.text = listView.model.data(index)
		                listView.forceActiveFocus()
		            }
                }
            }
        }
	}
}