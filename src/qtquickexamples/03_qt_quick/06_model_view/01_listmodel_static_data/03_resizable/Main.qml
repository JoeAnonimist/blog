import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    id: window

    visible: true
    width: listView.implicitWidth + 12
    height: 400
    title: "Resizable ListModel"

    DataModel {
        id: dataModel
    }

    ListViewModel {
        id: viewModel
        model: dataModel
    }
    
    ColumnLayout {
    
        anchors.fill: parent
        anchors.margins: 6
    
        ListView {
        
            id: listView
            Layout.fillWidth: true
            Layout.fillHeight: true
            
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
            
            property var listViewModel: viewModel
    
            delegate: ListDelegate {
                viewModel: listView.listViewModel
            }
    
            ScrollBar.vertical: ScrollBar { }
    
            Connections {
                target: viewModel
                function onSelected(index) {
                    listView.currentIndex = index
                }
            }
        }
        
        Button {
            Layout.fillWidth: true
            text: "Append new"
            onClicked: () => {
                viewModel.append()
            }
        }
        
        Button {
            Layout.fillWidth: true
            text: "Insert new"
            onClicked: () => {
                viewModel.insert()
                listView.positionViewAtIndex(viewModel.currentIndex, ListView.Center)
            }
        }
        
        Button {
            Layout.fillWidth: true
            text: "Remove current"
            onClicked: () => {
                viewModel.removeCurrent()
            }
        }
    }
}