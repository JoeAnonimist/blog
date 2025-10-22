import QtQuick
import QtQuick.Controls

ApplicationWindow {

    visible: true
    width: 340
    height: 200
    title: "GridModel with static data"

    GridView {

        id: gridView

        anchors.fill: parent
        anchors.margins: 10
        cellWidth: 80
        cellHeight: 60

        focus: true

        highlight: Rectangle {
            z: 100
            color: "transparent"
            border.color: "steelblue"
            border.width: 2
            radius: 2
        }
        highlightMoveDuration: 300

        delegate: Delegate {}
        model: Model {}

        ScrollBar.vertical: ScrollBar {}

        onCurrentIndexChanged: () => {
            console.log( "Current index changed: "
            + currentIndex)
        }

        ContextMenu.menu: Menu {
            MenuItem {
                text: "Add new item"
                onTriggered: () => {
                    gridView.model.addItem();
                    gridView.currentIndex = gridView.model.count - 1
                }
            }
        }
    }
}
