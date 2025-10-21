import QtQuick
import QtQuick.Controls


SwipeDelegate {

    id: root

    width: ListView.view.width

    required property string value
    required property int index

    text: value

    contentItem: Text {
        text: root.value
        horizontalAlignment: Text.AlignHCenter
    }

    onClicked: () => {
        root.ListView.view.currentIndex = index
    }

    swipe.right: Label {

        width: parent.width
        height: parent.height
        horizontalAlignment: Text.AlignHCenter

        verticalAlignment: Text.AlignVCenter
        text: "Delete " + root.value
        color: "red"

        SwipeDelegate.onClicked: () => {
            console.log("Swipe clicked")
            root.ListView.view.model.remove(root.index)
        }
    }
}
