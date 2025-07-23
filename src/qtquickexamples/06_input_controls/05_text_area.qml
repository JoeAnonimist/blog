import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {

    id: root

    visible: true
    width: 300
    height:180
    title: "TextArea example"

    ColumnLayout {

        anchors.fill: parent
            
        TextArea {
            
            id: textArea

            Layout.fillWidth: true
            textFormat: TextEdit.MarkdownText

            text: `

# Heading

**This line is bold**<br/>
*This line is italic*<br/>
_This line is underlined_<br/>
You can use 
<span style="color:maroon">
Ctrl-c, Ctrl-v</span> 
and other standard key bindings.<br/>
Right click brings up the context menu.

`
            onTextChanged: markdownLabel.text = text
        }
        
        Label {

            id: markdownLabel
            
            Layout.fillWidth: true
            Layout.fillHeight: true
            verticalAlignment: Text.AlignVCenter
        }
    }
}