# The QPlainTextEdit class provides a widget 
# that is used to edit and display plain text.
#
# It's a multi-line text edit control.
# The text is stored in a QTextDocument
# which is automatically created with QPlainTextEdit
# and which you can access with QPlainTextEdit.document().
# You can also access the whole text 
# using QPLainTextEdit.plainText().

import sys

from PySide6.QtCore import Slot
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QApplication,
    QWidget, QVBoxLayout, QPlainTextEdit, QLabel)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1 - Create the plain text edit widget
        #     and set its font and wrap mode.
        
        self.plain_text_edit = QPlainTextEdit()
        self.plain_text_edit.setLineWrapMode(
            QPlainTextEdit.LineWrapMode.NoWrap)
        self.font = QFont('Droid Sans Mono')
        self.font.setPixelSize(12)
        self.plain_text_edit.setFont(self.font)
        self.font.setStyleHint(QFont.StyleHint.Monospace)
        
        # These are for displaying document stats.
        
        self.label_char_count = QLabel()
        self.label_cursor_position = QLabel()
        
        # 3 - Add the QPlainTextEdit to the layout
        
        layout.addWidget(self.plain_text_edit)
        layout.addWidget(self.label_char_count)
        layout.addWidget(self.label_cursor_position)
        
        self.plain_text_edit.textChanged.connect(self.on_text_changed)
        self.plain_text_edit.cursorPositionChanged.connect(
            self.on_cursor_position_changed)
    
    # 2 - Get the underlying QTextDocument properties
    
    # This slot handles text changed events
    
    @Slot()        
    def on_text_changed(self):
        
        char_count = self.plain_text_edit.document().characterCount()
        self.label_char_count.setText(f'Char count: {str(char_count)}')
    
    # This one handles cursor position changes
    
    @Slot()
    def on_cursor_position_changed(self):
        
        cursor = self.plain_text_edit.textCursor()
        x = str(cursor.block().blockNumber() + 1)
        y = str(cursor.positionInBlock() + 1)
        
        self.label_cursor_position.setText(f'x: {x} y: {y}')


if __name__ == '__main__':

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
