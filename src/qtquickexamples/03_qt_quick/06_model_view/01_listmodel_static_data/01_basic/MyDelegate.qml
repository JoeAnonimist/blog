import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ItemDelegate {

    id: root

    required property int index
    required property string name
    required property int value

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
        anchors.margins: 8

        Label { text: name }
        Label { text: value }
    }

    onClicked: {
        root.ListView.view.currentIndex = index
        console.log("Clicked: " +
            "Current index: " + root.ListView.view.currentIndex +
            " Name: " + name + " Value: " + value)
    }
}