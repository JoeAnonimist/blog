import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    id: window

    visible: true
    width: listView.implicitWidth
    height: listView.implicitHeight
    title: "ListModel with static data"

    DataModel {
        id: dataModel
    }

    ListViewModel {
        id: viewModel
        model: dataModel
    }

    ListView {
        id: listView

        anchors.fill: parent
        model: viewModel.model

        implicitWidth: 200
        implicitHeight: viewModel.model.count * 40

        focus: true
        highlightFollowsCurrentItem: true
        highlightMoveDuration: 150
        highlight: Rectangle {
            color: "orange"
            opacity: 0.2
        }

        delegate: ListDelegate { }

        ScrollBar.vertical: ScrollBar { }

        Connections {
            target: viewModel
            function onSelected(index) {
                listView.currentIndex = index
            }
        }
    }
}