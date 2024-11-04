# The QTextEdit class provides a widget that is used 
# to edit and display both plain and rich text.

import sys

from PySide6.QtGui import QTextCursor, QTextCharFormat, QColor
from PySide6.QtWidgets import (QApplication,
    QWidget, QVBoxLayout, QTextEdit, QLabel)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1 - Create the text edit widget
        
        self.text_edit = QTextEdit()
        
        self.previous_cursor = None
        self.previous_format = None
        
        # QTextEdit supports markdown and HTML:
        
        markdown = '''
# Heading

**This line is bold**<br/>
*This line is italic*<br/>
_This line is underlined_<br/>
You can use 
<span style="color:maroon">
Ctrl-c, Ctrl-v</span> 
and other standard key bindings.<br/>
Right click brings up the context menu. 
'''
        self.text_edit.setMarkdown(markdown)
        
        # 3 - Connect signals with the slots
        
        self.text_edit.cursorPositionChanged.connect(
            self.on_cursor_position_changed)
        self.text_edit.textChanged.connect(
            self.on_text_changed)
        
        self.markdown_label = QLabel()
        self.markdown_label.setText(markdown)
        self.stats_label = QLabel()
        
        layout.addWidget(self.text_edit)
        layout.addWidget(self.markdown_label)
        layout.addWidget(self.stats_label)
    
    # 2 - Write the slot methods.     
    
    def on_text_changed(self):
        self.markdown_label.setText(
            self.text_edit.toMarkdown())        
   
    def on_cursor_position_changed(self):

        if not self.previous_cursor is None:
            self.previous_cursor.setCharFormat(
                self.previous_format)

        cursor = self.text_edit.textCursor()
        cursor.select(QTextCursor.WordUnderCursor)

        self.previous_cursor = cursor
        self.previous_format = cursor.charFormat()
        word = cursor.selectedText()

        format = QTextCharFormat()
        format.setBackground(QColor('lightsteelblue'))
        cursor.mergeCharFormat(format)
        
        self.stats_label.setText(f'Current word: {word}')


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
