import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {

    visible: true
    width: listView.implicitWidth
    height: listView.implicitHeight
    title: "Integers as models"

    ListView {
    
        id: listView
        
        anchors.fill: parent
        model: 6
        
        implicitWidth: 210
        implicitHeight: count * 45
        anchors.margins: 4
        spacing: 4
        
        focus: true
        
        delegate: Delegate {}
    }
}