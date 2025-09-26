import QtQuick
import QtQuick.Window

Window {
    width: 200
    height: 200
    visible: true
    title: "Vector2D Positioning"

    property vector2d pos: Qt.vector2d(50, 50)

    Rectangle {
        x: pos.x
        y: pos.y
        width: 30
        height: 30
        color: "steelblue"
        border.color: "lightsteelblue"
        border.width: 2
    }

    MouseArea {
        anchors.fill: parent
        onClicked: {
            pos = Qt.vector2d(
                Math.random() * (width - 100),
                Math.random() * (height - 100))
        }
    }
}