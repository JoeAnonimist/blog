import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {

    visible: true
    width: listView.implicitWidth
    height: listView.implicitWidth
    title: "Header and Footer"

    ListView {
    
        readonly property int headerHeight: 40
        readonly property int footerHeight: 40
    
        id: listView
        
        anchors.fill: parent
        model: Model { }
        implicitWidth: 210
        anchors.margins: 4
        spacing: 4
        clip: true

        focus: true

        preferredHighlightBegin: headerHeight + 4
        preferredHighlightEnd: height - footerHeight - 4
        highlightRangeMode: ListView.ApplyRange
        
        header: Rectangle {
            height: listView.headerHeight
            width: listView.width
            color: "lightsteelblue"
            z: 100
            Text {
                anchors.centerIn: parent
                text: "ListView Header Example"
            }
        }
        headerPositioning: ListView.OverlayHeader
        
        footer: Rectangle {
            height: listView.footerHeight
            width: listView.width
            color: "lightsteelblue"
            z: 100
            Text {
                anchors.centerIn: parent
                text: "Current Index: " + 
                    parent.ListView.view.currentIndex
            }
        }
        footerPositioning: ListView.OverlayFooter
        
        delegate: Delegate { }
        
        ScrollBar.vertical: ScrollBar {}
        
        onCurrentIndexChanged: {
            console.log("Current index changed: " + currentIndex)
        }
    }
}