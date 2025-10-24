import QtQuick
import QtQuick.Controls

ApplicationWindow {
    id: root
    visible: true
    width: 400
    height: 200
    title: "Easing Cycle Animation"

    property var easingTypes

    property int curIndex: 0

    Button {
        id: button
        height: 46
        width: 100
        x: 10
        y: 80
        text: "Click me\n" + root.easingTypes[0]
        contentItem: Text {
            text: parent.text
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            wrapMode: Text.WordWrap
        }

        PropertyAnimation {
            id: animation
            objectName: "animation"
            target: button
            property: "x"
            duration: 1000
        }

        onClicked: {
            try {
                button.text = "Click me\n"
                    + root.easingTypes[curIndex]
                animation.to = (button.x < 200) ? 290 : 10
                animation.easing.type = root.easingTypes[curIndex]
                console.log("Easing:", root.easingTypes[curIndex])
                animation.running = true
            } catch (e) {
                console.log("Easing:",
                    root.easingTypes[curIndex], "missing")
            }
            curIndex = (curIndex + 1) % root.easingTypes.length
        }
    }
}
