import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {
    visible: true
    width: 200
    height: 300
    title: "Flipable"

    Flipable {
    
        id: container
        anchors.fill: parent
        anchors.margins:10
        
        property bool flipped: false

        front: Rectangle {
            anchors.fill: parent
            color: "#B3E5FC"
            border.color: "#0288D1"
            border.width: 1

            Text {
                anchors.centerIn: parent
                text: "Front"
                font.pixelSize: 24
            }
        }

        back: Rectangle {
            anchors.fill: parent
            color: "#B9F6CA"
            border.color: "#388E3C"
            border.width: 1

            Text {
                anchors.centerIn: parent
                text: "Back"
                font.pixelSize: 24
            }
        }

        transform: Rotation {
            id: rotation
            origin.x: container.width / 2
            origin.y: container.height / 2
            axis.x: 1
            axis.y: 0
            axis.z: 0
            angle: 0
        }

        states: State {
            name: "back"
            when: container.flipped
            PropertyChanges { target: rotation; angle: 180 }
        }

        transitions: Transition {
            NumberAnimation {
                target: rotation;
                property: "angle";
                duration: 200
            }
        }

        MouseArea {
            anchors.fill: parent
            onClicked: () => {
                container.flipped = !container.flipped
                console.log("flip")
            }
        }
    }
}