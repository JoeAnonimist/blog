import QtQuick
import QtQuick.Controls

ApplicationWindow {

    visible: true
    width: listView.implicitWidth
    height: listView.implicitWidth
    title: "ListModel Filter"

    property var filterModel

    Model {
        id: sourceModel
        objectName: "sourceModel"
    }

    ListView {

        id: listView

        anchors.fill: parent

        implicitWidth: 210
        anchors.leftMargin: 4
        anchors.rightMargin: 4
        spacing: 4
        clip: true
        focus: true

        model: filterModel.model
        delegate: Delegate { }

        ScrollBar.vertical: ScrollBar {}

        onCurrentIndexChanged: () => {
            console.log(
                "Current index changed: "
                + currentIndex)
        }
    }

    ComboBox {

        anchors.left: parent.left
        anchors.right: parent.right
        anchors.bottom: parent.bottom

        model: ["View Even", "View Odd"]

        onCurrentIndexChanged: () => {
            if (currentIndex === 0) {
                filterModel.filter_even()
            } else {
                filterModel.filter_odd()
            }
        }
    }

    Component.onCompleted: () => {
        filterModel.model = sourceModel
        filterModel.filter_even()
    }
}
