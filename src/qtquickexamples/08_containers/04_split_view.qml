import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {

    visible: true
    width: 300
    height:300
    title: "SplitView"
    
    SplitView {
    
        id: splitView
        anchors.fill: parent
    
        GroupBox {
        
            title: "Options"
            SplitView.preferredWidth: parent.width / 3
            
            ColumnLayout {
            
                RadioButton {
                    checked: true
                    text: "Horizontal"
                    onCheckedChanged: {
                        if (checked)
                        splitView.orientation = Qt.Horizontal
                    }
                }
                RadioButton {
                    text: "Vertical"
                    onCheckedChanged: {
                        if (checked)
                        splitView.orientation = Qt.Vertical
                    }
                }
            }
        }
        GroupBox {
            title: "GroupBox 2"
            SplitView.preferredWidth: parent.width / 3
        }
        GroupBox {
            title: "GroupBox 3"
            SplitView.preferredWidth: parent.width / 3
        }
    }
}