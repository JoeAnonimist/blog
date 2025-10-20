import QtQuick
import QtQuick.Controls

ApplicationWindow {

    visible: true
    width: listView.implicitWidth
    height: listView.implicitWidth
    title: "ListModel Sections Demo"

    ListView {

        id: listView

        anchors.fill: parent
        model: Model {}

        implicitWidth: 210
        anchors.leftMargin: 4
        anchors.rightMargin: 4
        spacing: 4
        clip: true

        focus: true

        section.property: "parity"
        section.labelPositioning: ViewSection.InlineLabels | ViewSection.CurrentLabelAtStart
                                  | ViewSection.NextLabelAtEnd
        section.delegate: Rectangle {
            height: 20
            color: "#87CEEB"
            anchors.left: parent.left
            anchors.right: parent.right
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
                                   console.log(
                                       "Current index changed: "
                                       + currentIndex)
                               }
    }
}
