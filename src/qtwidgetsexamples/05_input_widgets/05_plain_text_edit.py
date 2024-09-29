# The QPlainTextEdit class provides a widget 
# that is used to edit and display plain text.
#
# It's a multi-line text edit control.
# The text is stored in a QTextDocument
# which is automatically created with QPlainTextEdit
# and which you can access with QPlainTextEdit.document().
# You can also access the whole text 
# using QPLainTextEdit.plainText().

from PySide6.QtWidgets import (QApplication, 
    QWidget, QVBoxLayout, QPlainTextEdit, QLabel)
import sys


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1 - Create the plain text edit widget
        
        self.plain_text_edit = QPlainTextEdit()
        
        # These are for displaying document stats.
        
        self.label_char_count = QLabel()
        self.label_cursor_position = QLabel()
        
        # 2 - Add the plain text edit to the layout
        
        layout.addWidget(self.plain_text_edit)
        layout.addWidget(self.label_char_count)
        layout.addWidget(self.label_cursor_position)
        
        self.plain_text_edit.textChanged.connect(self.on_text_changed)
        self.plain_text_edit.cursorPositionChanged.connect(
            self.on_cursor_position_changed)
    
    # 3 - Get the underlying QTextDocument properties
    
    # This slot handles text changed events
            
    def on_text_changed(self):
        char_count = self.plain_text_edit.document().characterCount()
        self.label_char_count.setText('Char count: ' + str(char_count))
    
    # This one handles cursor position changes
    
    def on_cursor_position_changed(self):
        cursor = self.plain_text_edit.textCursor()
        self.label_cursor_position.setText(
            'x: ' + str(cursor.block().blockNumber()) + 
            ', y: ' + str(cursor.positionInBlock()))
        


if __name__ == '__main__':

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())