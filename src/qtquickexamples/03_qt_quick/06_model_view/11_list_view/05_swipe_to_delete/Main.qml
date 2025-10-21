import QtQuick
import QtQuick.Controls

ApplicationWindow {

    visible: true
    width: listView.implicitWidth
    height: listView.implicitWidth
    title: "ListModel Swipe to Delete"

    ListView {

        id: listView

        anchors.fill: parent

        implicitWidth: 210
        anchors.leftMargin: 4
        anchors.rightMargin: 4
        spacing: 4
        clip: true
        focus: true

        model: Model {}
        delegate: Delegate {}

        ScrollBar.vertical: ScrollBar {}

        onCurrentIndexChanged: () => {
            console.log(
                "Current index changed: "
                + currentIndex)
        }
    }
}
