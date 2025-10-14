import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


Rectangle {
    
    id: root

    width: ListView.view.width
    height: 90
    color: "transparent"
    border.color: "lightgrey"
    border.width: 1
    
    required property var model
    required property int index
    
    RowLayout {
    
        anchors.fill: parent
        anchors.margins: 8

        ColumnLayout {
            Layout.fillWidth: true
	        Label {
	            text: model.property1
	            Layout.fillWidth: true
	            horizontalAlignment: Text.AlignHCenter
	        }
	        	        Label {
	            text: model.property2
	            Layout.fillWidth: true
	            horizontalAlignment: Text.AlignHCenter
	        }
	        	        Label {
	            text: model.property3
	            Layout.fillWidth: true
	            horizontalAlignment: Text.AlignHCenter
	        }
	        	        Label {
	            text: model.property4
	            Layout.fillWidth: true
	            horizontalAlignment: Text.AlignHCenter
	        }
        }
    }
}