import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {

    visible: true
    width: listView.implicitWidth
    height: listView.implicitWidth
    title: "ListModel with static data"
    
    Data {
        id: listModel
    }

    ListView {
    
        id: listView
        
        anchors.fill: parent
        model: listModel
        
        implicitWidth: 200
        implicitHeight: count * 40
        
        focus: true
        highlightFollowsCurrentItem: true
        highlight: Rectangle {
            color: "orange"
            opacity: 0.2
        }
        
        delegate: Delegate {}
        
        ScrollBar.vertical: ScrollBar {}
        
        onCurrentIndexChanged: () => {
            console.log( "Current index changed: "
            + currentIndex)
        }
    }
}