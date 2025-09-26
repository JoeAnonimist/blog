import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {

    visible: true
    title: "Sprites"

    ColumnLayout {
        anchors.fill: parent
        
        // For single sprite sheet.
        // For multiple connected animations use SpriteSequence

        AnimatedSprite {
        
            id: mySprites

            Layout.preferredWidth: 117
            Layout.preferredHeight: 116
            Layout.alignment: Qt.AlignCenter

            source: "sprites.png"

            frameCount: 6
            frameDuration: 100
            frameWidth: 117
            frameHeight: 116
            
            interpolate: false
            running: true
        }

        Button {
            text: "Pause / Resume"
            Layout.fillWidth: true
            onClicked: {
                mySprites.running = !mySprites.running
            }
        }
    }
}
