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
        model: ["one", "two", "three", "four", "five", "six"]
        
        implicitWidth: 210
        implicitHeight: count * 45
        anchors.margins: 4
        spacing: 4
        
        focus: true
        
        delegate: Delegate {}
        
        onCurrentIndexChanged: () => {
            for (let i = 0; i < model.length; i++) {
                console.log(model[i])
            }
        }
    }
}