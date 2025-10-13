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

        ScrollBar.vertical: ScrollBar {}
        
        model: Model { id: listModel }

        delegate: Delegate {}
        
        Keys.onUpPressed: (event) => {
            if (currentIndex > 0) {
                currentIndex--;
                positionViewAtIndex(currentIndex, ListView.CenterIndex);
            }
        }
        
        Keys.onDownPressed: (event) => {
            if (currentIndex < count - 1) {
                currentIndex++;
                positionViewAtIndex(currentIndex, ListView.CenterIndex);
            }
        }
    }
}