import QtQuick
import QtQuick.Controls

ApplicationWindow {
    visible: true
    width: 400
    height: 200
    title: "Easing Cycle Animation"

    property var easingTypes: [
        Easing.Linear,
        Easing.InQuad, Easing.OutQuad, Easing.InOutQuad,
        Easing.OutInQuad,
        Easing.InCubic, Easing.OutCubic, Easing.InOutCubic,
        Easing.InQuart, Easing.OutQuart, Easing.InOutQuart,
        Easing.InQuint, Easing.OutQuint, Easing.InOutQuint,
        Easing.InSine, Easing.OutSine, Easing.InOutSine,
        Easing.InExpo, Easing.OutExpo, Easing.InOutExpo,
        Easing.InCirc, Easing.OutCirc, Easing.InOutCirc,
        Easing.InElastic, Easing.OutElastic, Easing.InOutElastic,
        Easing.InBack, Easing.OutBack, Easing.InOutBack,
        Easing.InBounce, Easing.OutBounce, Easing.InOutBounce
    ]

    property int currentEasingIndex: 0

    Button {
        id: button
        height: 40
        width: 100
        x: 10
        y: 80
        text: "Click me"

        PropertyAnimation {
            id: animation
            target: button
            property: "x"
            duration: 1000
            // 'to' will be set dynamically in onClicked
        }

        onClicked: {
            console.log("clicked")

            // 1. Determine destination
            var nextX = (button.x < 200) ? 290 : 10  // 290 = 400 - 100 - 10 margin
            animation.to = nextX

            // 2. Cycle easing type
            animation.easing.type = easingTypes[currentEasingIndex]
            console.log("Easing:", getEasingName(easingTypes[currentEasingIndex]))

            currentEasingIndex = (currentEasingIndex + 1) % easingTypes.length

            // 3. Start animation
            animation.running = true
        }

        // Helper to get readable name
        function getEasingName(type) {
            for (var name in Easing) {
                if (Easing[name] === type) return name
            }
            return "Unknown"
        }
    }
}
