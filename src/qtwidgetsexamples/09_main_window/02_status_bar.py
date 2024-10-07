#  The QStatusBar class provides a horizontal bar 
# suitable for presenting status information. 

import sys

from PySide6.QtWidgets import (QApplication, QMainWindow,
    QTextEdit, QLabel)


class QEditor(QMainWindow):
    
    def __init__(self):

        super().__init__()

        self.text_edit = QTextEdit()        
        self.setCentralWidget(self.text_edit)
        
        # 1 - Create a widget to display information
        
        self.label = QLabel()
        
        # 2 - Add the widget to QStatusBar
        #     You access the status bar using QMainWindow.statusBar()
        
        self.statusBar().addWidget(self.label)
        
        self.text_edit.textChanged.connect(self.on_text_changed)
    
    # 3 - Display some stats in the widget associated
    #     with the status bar.
    
    def on_text_changed(self):
        
        cursor = self.text_edit.textCursor()
        
        size = len(self.text_edit.toPlainText())
        x = str(cursor.blockNumber() + 1)
        y = str(cursor.columnNumber() + 1)
        
        self.label.setText('Chars: {}, Ln: {}, Col: {}'.format(size, x, y))


if __name__ == '__main__':

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    editor = QEditor()
    editor.show()

    sys.exit(app.exec())
