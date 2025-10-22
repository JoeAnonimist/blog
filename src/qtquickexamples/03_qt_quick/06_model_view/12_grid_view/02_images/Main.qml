import QtQuick
import QtQuick.Controls

ApplicationWindow {

    visible: true
    width: 360
    height: 320
    title: "GridModel with Images"

    GridView {

        id: gridView

        anchors.fill: parent
        anchors.margins: 10
        cellWidth: 80
        cellHeight: 100

        focus: true

        highlight: Rectangle {
            z: 100
            border.color: "steelblue"
            border.width: 2
            radius: 2
            color: "transparent"
        }
        highlightMoveDuration: 300

        delegate: Delegate {}
        model: Model {}

        ScrollBar.vertical: ScrollBar {}

        onCurrentIndexChanged: () => {
            console.log( "Current index changed: "
            + currentIndex)
        }
    }
}
