import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {

    visible: true
    width: listView.implicitWidth
    height: listView.implicitHeight
    title: "Horizontal LIstView"

    ListView {
    
        id: listView
        
        anchors.fill: parent
        model: 6
        
        implicitWidth: count * 45
        implicitHeight: 210
        anchors.margins: 4
        spacing: 4
        
        orientation: ListView.Horizontal
        
        focus: true
        
        delegate: Delegate {}
        
        ScrollBar.horizontal: ScrollBar {}
        
        onCurrentIndexChanged: () => {
            console.log( "Current index changed: "
            + currentIndex)
        }
    }
}