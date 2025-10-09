import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {

    visible: true
    width: 250
    height: 400
    title: "Resizable ListModel"

    ListModel {

        id: listModel

        ListElement { name: "Item 0"; value: 0 }
        ListElement { name: "Item 1"; value: 1 }
        ListElement { name: "Item 2"; value: 2 }
        ListElement { name: "Item 3"; value: 3 }
        ListElement { name: "Item 4"; value: 4 }
        ListElement { name: "Item 5"; value: 5 }
        ListElement { name: "Item 6"; value: 6 }
        ListElement { name: "Item 7"; value: 7 }
        ListElement { name: "Item 8"; value: 8 }
        ListElement { name: "Item 9"; value: 9 }
    }
    
    ColumnLayout {
        
        anchors.fill: parent
        anchors.margins: 6
    
	    ListView {
	        id: listView
	        Layout.fillWidth: true
	        Layout.fillHeight: true
	        model: listModel
	        focus: true
	        highlightFollowsCurrentItem: true
	
	        highlight: Rectangle {
	            color: "orange"
	            opacity: 0.2
	        }
	
	        delegate: MyDelegate {}
	        
            ScrollBar.vertical: ScrollBar {}
	    }
	    
	    RowLayout {
	    
	        id: formLayout
	        
	        Layout.fillWidth: true
	        Layout.preferredHeight: implicitHeight
	        spacing: 6
	        
	        TextField {
	            id: nameField
	            Layout.fillWidth: true
	            placeholderText: "Name"
	            text: {
			        if (listView.currentIndex >= 0 &&
                        listView.currentIndex < listModel.count)
                        return listModel.get(listView.currentIndex).name
			        return ""
			    }
	            onAccepted: () => {
	                listModel.setProperty(
	                    listView.currentIndex, "name", text)
	                listView.forceActiveFocus()
	            }
	        }
	        
	        SpinBox {
	            id: valueSpinbox
	            Layout.preferredWidth: 70
	            from: 0; to: 100
	            editable: true
	            value: {
	                if (listView.currentIndex >= 0 &&
	                    listView.currentIndex < listModel.count)
	                    return listModel.get(listView.currentIndex).value
	                return 0
	            }
	            onValueModified: () => {
                    listModel.setProperty(
                        listView.currentIndex, "value", value)
                    listView.forceActiveFocus()
	            }
	        }
	        
	        Button {
	            text: "➕"
	            Layout.preferredWidth: implicitHeight
	            onClicked: () => {
	                listModel.append({ name: "New Item", value: 0 });
	                listView.currentIndex = listModel.count - 1;
                    listView.positionViewAtIndex(
	                    listView.currentIndex, ListView.End);
	            }
	        }
	        
            Button {
                text: "➖"
                enabled: listModel.count > 0
                Layout.preferredWidth: implicitHeight
                onClicked: () => {
                    listModel.remove(listView.currentIndex, 1);
                    listView.currentIndex = Math.max(
                        0, listView.currentIndex - 1);
                }
            }
	    }
	}

    component MyDelegate: Rectangle {

        id: root

        required property int index
        required property string name
        required property int value

        width: 220
        height: 40
        color: index === ListView.view.currentIndex
            ? "transparent"
            : index % 2 === 0 ? "#f0f0f0" : "#dcdcdc"

        RowLayout {
            anchors.fill: parent
            anchors.margins: 8

            Label {
                text: name
                Layout.fillWidth: true
            }
            Label {
                id: displayControl
                text: value
                horizontalAlignment: Text.AlignRight
            }
        }

        MouseArea {
            anchors.fill: parent
            onClicked: (mouse) => {
                root.ListView.view.currentIndex = index
            }
        }
    }
}
