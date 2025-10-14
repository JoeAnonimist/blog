import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {

    visible: true
    width: 200
    height: 300
    title: "QAbstractListModel subclass as model"
    
    property var listModel
    
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
	            height: 40; width: 200
	            color: "#0078d7"; opacity: 0.2
	        }
	
	        ScrollBar.vertical: ScrollBar { }
	        
	        model: listModel
	
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
                currentIndex >= 0 && currentIndex < listView.model.length
            }

            TextField {
                id: valueField
                Layout.fillWidth: true
                placeholderText: "Value"
                text: {
                    if (parent.hasSelection) {
                        console.log(listView.model[parent.currentIndex])
                        listView.model[parent.currentIndex]
                    } else {
                        ""
                    }
                }
                onAccepted: {
                    if (parent.hasSelection) {
                        listView.model[parent.currentIndex] =  text
                        listView.forceActiveFocus()
                    }
                }
            }

            Button {
                text: "➕"
                Layout.preferredWidth: implicitHeight
                onClicked: () => {
                    listView.model.push("<new>")
                    listView.currentIndex = listView.model.length - 1
                    listView.positionViewAtIndex(listView.currentIndex, ListView.Center)
	                valueField.text = listView.model[parent.currentIndex]
                    listView.forceActiveFocus()
                }
            }

            Button {
                text: "➖"
                enabled: listView.model.length > 0
                Layout.preferredWidth: implicitHeight
                onClicked: () => {
	                if (listView.model.length > 0) {
		                listView.model.splice(listView.currentIndex, 1)
		                if (listView.currentIndex == listView.model.length) {
		                    listView.currentIndex = listView.currentIndex - 1
		                }
		                valueField.text = listView.model[parent.currentIndex]
		                listView.forceActiveFocus()
		            }
                }
            }
        }
	}
}