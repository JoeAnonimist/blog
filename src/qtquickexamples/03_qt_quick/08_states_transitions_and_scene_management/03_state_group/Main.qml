import QtQuick
import QtQuick.Controls

ApplicationWindow {

    visible: true
    width: listView.implicitWidth
    height: listView.implicitWidth
    title: "ListModel Sections Demo"

    property bool refreshing: false
    property int pullTreshold: 60
    property real minContentY: 0

    Model {id: model}

    ListView {

        id: listView

        anchors.fill: parent

        implicitWidth: 210
        anchors.leftMargin: 4
        anchors.rightMargin: 4
        spacing: 4
        clip: true

        focus: true

        boundsBehavior: Flickable.DragOverBounds

        model: model.listModel
        delegate: Delegate {}

        ScrollBar.vertical: ScrollBar {}

        onContentYChanged: () => {
            if (listView.dragging) {
                minContentY = Math.min(minContentY, contentY)
            }
        }

        onMovementEnded: () => {
            if (minContentY < -pullTreshold && !refreshing) {
                refreshing = true
                console.log("refreshing")
                console.log(minContentY)
                //model.refresh()
                model.stateGroup.state = "updating"
                //model.stateGroup.state = "waiting"
            }
            minContentY = 0
            refreshing = false
        }

        onCurrentIndexChanged: () => {
           console.log(
               "Current index changed: "
               + currentIndex)
       }
    }
}
