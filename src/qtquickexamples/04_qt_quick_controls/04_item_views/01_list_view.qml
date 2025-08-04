import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {

    id: root

    visible: true
    width: 200
    height:200
    title: "ListView example"
    
    property var fsmodel

    ColumnLayout {

        anchors.fill: parent

        ListView {
            
            id: listView

            Layout.fillWidth: true
            Layout.fillHeight: true
            
            model: fsmodel
            
            delegate: ItemDelegate {
                width: listView.width
                text: model.display
                highlighted: ListView.isCurrentItem
                background: Rectangle {
                    color: mouse.hovered ? "lightsteelblue" : "transparent"
                }
                onClicked: listView.currentIndex = index
	            HoverHandler {
	                id: mouse
	                acceptedDevices: PointerDevice.Mouse
	            }
            }

            ScrollBar.vertical: ScrollBar {
                policy: ScrollBar.AlwaysOn
            }
            
            highlightFollowsCurrentItem: true

	        highlight: Rectangle {
	            color: "lightsteelblue"
	            width: 10
	        }
        }
    }
}