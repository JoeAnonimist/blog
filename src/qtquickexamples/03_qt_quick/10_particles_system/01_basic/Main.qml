import QtQuick
import QtQuick.Particles

Window {
    width: 640
    height: 480
    visible: true
    title: "Basic Particle System"

    Rectangle {
        anchors.fill: parent
        color: "black"

        ParticleSystem {
            id: particles
        }

        Emitter {
            system: particles
            emitRate: 10
            lifeSpan: 3000
            size: 16
            anchors.centerIn: parent

            velocity: AngleDirection {
                angle: 72
                magnitude: 100
            }
        }

        ItemParticle {
            system: particles
            delegate: Rectangle {
                width: 10
                height: 10
                radius: 5
                color: "orange"
            }
        }
    }
}
