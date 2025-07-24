import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import examples.charcounter


ApplicationWindow {

    visible: true
    width: 400
    height:200
    title: "Application Window"
    
    CharCounter {
        id: charCounter
    }
    
    ScrollView {
    
        anchors.fill: parent
    
	    TextArea {
	        
	        id: textArea
	        
	        onCursorPositionChanged: {
	            let [row, col] = charCounter.cursor_position(
                    textDocument, cursorPosition)
                positionLabel.text = "row: " + row + ", col: " + col
                let char_count = charCounter.char_count(textDocument)
                charcountLabel.text = char_count
	        }
	    }
	}
	
	footer: ToolBar {
	    RowLayout {
	        anchors.fill: parent
		    Label {
		        id: positionLabel
		        text: "a"
		    }
		    Item {
		        Layout.fillWidth: true
		    }
		    Label {
		        id: charcountLabel
		        text: "b"
		    }
		}
	}
}