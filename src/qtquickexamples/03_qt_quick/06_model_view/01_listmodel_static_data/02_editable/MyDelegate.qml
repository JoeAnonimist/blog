import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ItemDelegate {

    id: root

    required property int index
    required property string name
    required property int value

    property int originalValue

    width: ListView.view.width
    height: 40

    highlighted: ListView.isCurrentItem

    background: Rectangle {
        color: highlighted ?
            "transparent" :
            (index % 2 === 0 ?
                "#f0f0f0" : "#dcdcdc")
    }

    contentItem: RowLayout {

        anchors.fill: parent
        anchors.leftMargin: 10
        anchors.rightMargin: 10
        spacing: 10
        height: 40

        Label { 
            text: name
            Layout.fillWidth: true
        }

        StackLayout {

            id: valueStack
            Layout.preferredWidth: 25
            Layout.fillHeight: true
            Layout.rightMargin: 10

            currentIndex: root.state === "edit" ? 1 : 0

            Label {
                id: displayControl
                text: value
                horizontalAlignment: Text.AlignRight
                verticalAlignment: Text.AlignVCenter
                Layout.alignment: Qt.AlignVCenter
                Layout.preferredWidth: 25
            }

            SpinBox {
                id: editControl
                Layout.preferredWidth: 25
                Layout.alignment: Qt.AlignVCenter
                focus: root.state === "edit"
                from: 0; to: 100; editable: true
                value: root.value

                onValueModified: () => {
                    listModel.setProperty(index, "value", value)
                }

                onActiveFocusChanged: () => {
                    if (!activeFocus && root.state === "edit") {
                        root.state = ""
                    }
                }

                Keys.onReturnPressed: { root.state = "" }
                Keys.onEnterPressed: { root.state = "" }
                Keys.onEscapePressed: {
                    console.log(root.originalValue)
                    listModel.setProperty(
                        index, "value", root.originalValue)
                    editControl.value = root.originalValue
                    root.state = ""
                }
            }
        }
    }

    onClicked: {
        root.ListView.view.currentIndex = index
    }

    onDoubleClicked: (mouse) => {
        console.log("dbl click")
        originalValue = value
        root.state = "edit"
        editControl.forceActiveFocus()
    }
}