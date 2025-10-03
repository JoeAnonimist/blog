import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {

    visible: true
    width: listView.implicitWidth
    height: listView.implicitWidth
    title: "ListModel with static data"
    
    ListModel {

        id: listModel

        ListElement {name: "Item 1"; value: 1}
        ListElement {name: "Item 2"; value: 2}
        ListElement {name: "Item 3"; value: 3}
        ListElement {name: "Item 4"; value: 4}
        ListElement {name: "Item 5"; value: 5}
        ListElement {name: "Item 6"; value: 6}
        ListElement {name: "Item 7"; value: 7}
        ListElement {name: "Item 8"; value: 8}
    }

    ListView {
    
        id: listView
        
        anchors.fill: parent
        model: listModel
        
        implicitWidth: 200
        implicitHeight: count * 40
        
        delegate: Rectangle {
        
            width: 200
            height: 40
            color: index % 2 === 0 ? "#f0f0f0" : "#dcdcdc"
            border.width: 1
            border.color: "lightgrey"
            
            RowLayout {
            
                anchors.fill: parent
                anchors.margins: 8
                
                Label { text: name }
                Label { text: value }
            }
        }
    }
}