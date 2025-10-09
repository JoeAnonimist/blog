import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {

    visible: true
    width: listView.implicitWidth
    height: listView.implicitWidth
    title: "Editable ListModel"

    MyModel { id: listModel }

    ListView {
        id: listView

        anchors.fill: parent
        model: listModel

        implicitWidth: 200
        implicitHeight: count * delegateHeight

        property int delegateHeight: 40

        focus: true
        highlightFollowsCurrentItem: true
        highlight: Rectangle { color: "orange"; opacity: 0.2 }

        delegate: MyDelegate { }

        ScrollBar.vertical: ScrollBar { }
    }
}
