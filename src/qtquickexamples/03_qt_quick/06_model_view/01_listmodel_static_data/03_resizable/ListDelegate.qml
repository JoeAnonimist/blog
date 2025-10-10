import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Rectangle {

    id: root

    required property int index
    required property string name
    required property int value
    required property var model
    
    property QtObject viewModel
    property bool editing: false    

    width: 200
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

        StackLayout {
            id: valueStack
            Layout.preferredWidth: 20
            Layout.fillHeight: true
            currentIndex: root.editing ? 1 : 0

            Label {
                id: displayControl
                text: value 
                horizontalAlignment: Text.AlignRight
            }

            SpinBox {
                id: editControl
                focus: root.editing
                from: 0; to: 100; editable: true
                value: root.value

                onActiveFocusChanged: {
                    if (!activeFocus && root.editing) {
                        commitEdit()
                    }
                }

                Keys.onReturnPressed: { commitEdit() }
                Keys.onEnterPressed: { commitEdit() }
                Keys.onEscapePressed: { root.editing = false }
            }
        }
    }

    MouseArea {

        anchors.fill: parent
        enabled: !root.editing

        onClicked: (mouse) => {
            viewModel.selectItem(index)
        }

        onDoubleClicked: (mouse) => {
            viewModel.selectItem(index)
            root.editing = true
            editControl.forceActiveFocus()
        }
    }
    
	function commitEdit() {
	    if (root.editing && editControl.value >= 0) {
	        viewModel.updateValue(editControl.value)
	    }
	    root.editing = false
	}
}