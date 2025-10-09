import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Rectangle {
    id: root

    required property int index
    required property string name
    required property int value
    required property bool isSelected
    
    signal clicked()

    width: 220
    height: 40
    color: isSelected ? "transparent"
        : index % 2 === 0 ? "#f0f0f0" : "#dcdcdc"

    RowLayout {
        anchors.fill: parent
        anchors.margins: 8

        Label {
            text: name
            Layout.fillWidth: true
        }
        Label {
            text: value
            horizontalAlignment: Text.AlignRight
        }
    }

    MouseArea {
        anchors.fill: parent
        onClicked: root.clicked()
    }
}