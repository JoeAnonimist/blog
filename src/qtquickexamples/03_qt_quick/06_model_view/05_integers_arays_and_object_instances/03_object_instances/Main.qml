import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {

    visible: true
    width: listView.implicitWidth
    height: listView.implicitHeight
    title: "Arrays as models"

    ListView {
    
        id: listView
        
        anchors.fill: parent
        model: Model {}
        
        implicitWidth: 210
        implicitHeight: 100
        anchors.margins: 4
        spacing: 4
        
        focus: true
        
        delegate: Delegate {}
    }
}