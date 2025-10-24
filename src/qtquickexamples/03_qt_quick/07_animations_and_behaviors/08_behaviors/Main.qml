import QtQuick
import QtQuick.Controls

ApplicationWindow {

    visible: true
    width: 400
    height: 200
    title: "Property Animation"

    Button {

        id: button

        height: 40
        width: 100
        anchors.centerIn: parent
        text: "Click me"

        Behavior on width {
            NumberAnimation { duration: 200 }
        }

        onClicked: () => {
            console.log("clicked")
            width = width === 100 ? 120 : 100
        }
    }
}
