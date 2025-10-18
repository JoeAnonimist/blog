import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {

    visible: true
    width: listView.implicitWidth
    height: listView.implicitHeight
    title: "ListModel highlight"

    ListView {
    
        id: listView
        
        anchors.fill: parent
        model: Model { }
        
        implicitWidth: 210
        implicitHeight: 310
        anchors.margins: 4
        spacing: 4
        clip: true
        
        focus: true
        
        delegate: Delegate {id: myDelegate}
        
        ScrollBar.vertical: ScrollBar { }
        
        highlight: Row {
            spacing: 1
            Repeater {
                model: listView.currentItem.barCount
                Rectangle {
                    width: 2
                    height: 40
                    color: "lightSteelBlue"
                }
            }
        }
    }
}