import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQml.XmlListModel

ApplicationWindow {
    visible: true
    width: listView.implicitWidth
    height: listView.implicitWidth
    title: "XmlListModel"

    XmlListModel {
        id: xmlModel

        source: "data.xml"
        query: "/organization/person"

        XmlListModelRole {
            name: "firstname"
            elementName: "firstname"
        }

        XmlListModelRole {
            name: "lastname"
            elementName: "lastname"
        }

        XmlListModelRole {
            name: "profession"
            elementName: "profession"
        }
    }

    ListView {
        id: listView

        anchors.fill: parent
        model: xmlModel

        implicitWidth: 200
        implicitHeight: count * 40

        focus: true
        highlightFollowsCurrentItem: true
        highlight: Rectangle {
            color: "orange"
            opacity: 0.2
        }

        delegate: MyDelegate {}

        ScrollBar.vertical: ScrollBar {}

        onCurrentIndexChanged: () => {
            console.log("Current index changed: " + currentIndex)
        }
    }

    component MyDelegate: Rectangle {
        id: root

        required property int index
        required property var model

        required property string firstname
        required property string lastname
        required property string profession

        width: 200
        height: 40
        color: index === ListView.view.currentIndex ?
            "transparent" :
            index % 2 === 0 ? "#f0f0f0" : "#dcdcdc"

        RowLayout {
            anchors.fill: parent
            anchors.margins: 8

            Label { text: firstname + " " + lastname }
            Label { text: profession }
        }

        MouseArea {
            anchors.fill: parent
            onClicked: {
                root.ListView.view.currentIndex = index
                console.log("Clicked: " +
                    "Current index: " + root.ListView.view.currentIndex +
                    " Name: " + model.firstname + " " + model.lastname + " Value: " + model.profession)
            }
        }
    }
}