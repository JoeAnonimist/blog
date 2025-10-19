import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {

    visible: true
    width: listView.implicitWidth
    height: listView.implicitHeight
    title: "ListModel with static data"

    ListView {
    
        id: listView
        
        anchors.fill: parent
        model: Model {}
        
        implicitWidth: 210
        implicitHeight: count * 45
        anchors.margins: 4
        spacing: 4
        
        focus: true
        
        section.property: "parity"
        section.delegate: Rectangle {
            width: 210
            height: 20
            required property string section
            Text {
                anchors.centerIn: parent
                text: parent.section
            }
        }
        section.criteria: ViewSection.FullString
        
        delegate: Delegate {}
        
        ScrollBar.vertical: ScrollBar {}
        
        onCurrentIndexChanged: () => {
            console.log( "Current index changed: "
            + currentIndex)
        }
    }
}