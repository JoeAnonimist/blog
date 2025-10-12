import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {

    visible: true
    width: 200
    height: listView.implicitHeight
    title: "Editable ListModel"

    ListView {
    
        id: listView

        anchors.fill: parent
        implicitWidth: 200
        implicitHeight: count * 45
        anchors.margins: 4
        spacing: 4
        focus: true
        
        highlightFollowsCurrentItem: true
        highlight: Rectangle {
            height: 40; width: 200
            color: "#0078d7"; opacity: 0.2
        }

        ScrollBar.vertical: ScrollBar {}
        
        model: Model { id: listModel }

        delegate: Delegate {}
    }
}