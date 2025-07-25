import QtQuick
import QtQuick.Controls
import QtQuick.Dialogs
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
        ScrollBar.horizontal.policy: ScrollBar.AlwaysOn
        ScrollBar.vertical.policy: ScrollBar.AlwaysOn
    
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
	
	MessageDialog {
	    id: aboutDialog
	    text: "Qml menu example"
        buttons: MessageDialog.Ok
	}
	
    Action {
        id: exitAction
        text: "Exit"
        shortcut: "Alt+X"
        onTriggered: Qt.quit()
    }
    
    Action {
        id: aboutAction
        text: "About"
        shortcut: "Alt+A"
        onTriggered: aboutDialog.open()
    }
	
	menuBar: MenuBar {
	    Menu {
	        title: "&File"
	        MenuItem {
	            action: exitAction
	        }
	    }
	    Menu {
	        title: "&Help"
	        MenuItem {
                action: aboutAction
            }
	    }
	}
	
	header: ToolBar {
	    RowLayout {
	        anchors.fill: parent
	        ToolButton {
	            text: "Exit"
		        icon.source: "icons/exit.png"
		        action: exitAction
	        }
	        ToolButton {
	            text: "About"
		        icon.source: "icons/about.png"
		        action: aboutAction
	        }
		    Item {
		        Layout.fillWidth: true
		    }
	    }
	}
	
	footer: ToolBar {
	    RowLayout {
	        anchors.fill: parent
		    Label {
		        id: positionLabel
		    }
		    Item {
		        Layout.fillWidth: true
		    }
		    Label {
		        id: charcountLabel
		    }
		}
	}
}