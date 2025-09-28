import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {
    visible: true
    width: 320
    height: 240
    title: "Circle Button"

    Canvas {
    
        id: circleButton
        anchors.centerIn: parent
        width: 100
        height: 100
        
        signal clicked()

        property bool pressed: false

        function drawPath(ctx) {
            var r = width / 2;
            ctx.beginPath();
            ctx.arc(r, r, r - 2, 0, 2 * Math.PI);
            ctx.closePath();
        }

        onPaint: {
            var ctx = getContext("2d");
            ctx.reset();
            ctx.clearRect(0, 0, width, height);

            drawPath(ctx);

            ctx.fillStyle = pressed ? "#3b82f6" : "#60a5fa";
            ctx.fill();

            ctx.lineWidth = 3;
            ctx.strokeStyle = "white";
            ctx.stroke();
        }

        MouseArea {

            anchors.fill: parent

            onPressed: (mouse) => {
                var ctx = circleButton.getContext("2d");
                circleButton.drawPath(ctx);
                if (ctx.isPointInPath(mouse.x, mouse.y)) {
                    circleButton.pressed = true;
                    circleButton.requestPaint();
                }
            }
            onReleased: (mouse) => {
                var ctx = circleButton.getContext("2d");
                circleButton.drawPath(ctx);
                if (ctx.isPointInPath(mouse.x, mouse.y)) {
                    circleButton.pressed = false;
                    circleButton.requestPaint();
                    console.log("Circle button clicked!");
                } else {
                    circleButton.pressed = false;
                    circleButton.requestPaint();
                }
            }
        }
    }
    
    Connections {
        target: circleButton
        function onClicked () {
            console.log("Button clicked");
        }
    }
}
