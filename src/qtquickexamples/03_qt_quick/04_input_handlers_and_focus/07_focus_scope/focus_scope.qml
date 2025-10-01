import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

// https://www.vcreatelogic.com/index.php/2023/07/14/what-exactly-does-focusscope-do-in-qml/


ApplicationWindow {
    visible: true
    width: 300
    height: 200

    component MyComponent: FocusScope {
        width: 200
        height: 40

        Rectangle {
            anchors.fill: parent
            border { color: "steelblue"; width: 1 }
            //activeFocusOnTab: true

            Row {
                anchors.fill: parent
                spacing: 6
                anchors.margins: 6

                Rectangle {
                    width: (parent.width - parent.spacing) / 2
                    height: parent.height
                    border.width: 1
                    border.color: "steelblue"
                    Text { text: "Name"; anchors.centerIn: parent }
                }

                Rectangle {
                    id: valueRect
                    width: (parent.width - parent.spacing) / 2
                    height: parent.height
                    border.width: 1
                    border.color: activeFocus ? "orange" : "steelblue"

                    Text { text: "Value"; anchors.centerIn: parent }

                    activeFocusOnTab: true

                    onActiveFocusChanged: {
                        opacity = activeFocus ? 0.8 : 1
                    }
                }
            }

            onActiveFocusChanged: {
                border.color = activeFocus ? "orange" : "steelblue"
                opacity = activeFocus ? 0.8 : 1
            }
        }
    }

    Column {
        anchors.centerIn: parent
        spacing: 6

        MyComponent { focus: true }
        MyComponent {}
        MyComponent {}
    }
}
