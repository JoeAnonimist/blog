import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Rectangle {
    id: root

    required property int index
    required property var model
    
    property var viewModel

    width: 200
    height: 40
    color: index === viewModel.currentIndex ?
           "transparent" :
           index % 2 === 0 ? "#f0f0f0" : "#dcdcdc"

    RowLayout {
        anchors.fill: parent
        anchors.margins: 8

        Label { text: model.name }
        Label { text: model.value }
    }

    MouseArea {
        anchors.fill: parent
        onClicked: {
            viewModel.selectItem(index)
        }
    }
}