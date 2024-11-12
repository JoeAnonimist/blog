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
        
        # 1 - Create widgets to display information
        
        self.position_label = QLabel()
        self.charcount_label = QLabel()
        
        # 2 - Add the widget to QStatusBar
        #     You access the status bar using QMainWindow.statusBar()
        
        self.statusBar().addWidget(self.position_label)
        self.statusBar().addPermanentWidget(self.charcount_label)
        
        self.text_edit.textChanged.connect(self.on_text_changed)
        self.text_edit.copyAvailable.connect(self.on_copy_available)
    
    # 3 - Display some stats in the widget associated
    #     with the status bar.
    
    def on_text_changed(self):
        
        cursor = self.text_edit.textCursor()
        
        size = len(self.text_edit.toPlainText())
        x = str(cursor.blockNumber() + 1)
        y = str(cursor.columnNumber() + 1)
        
        self.position_label.setText('Ln: {}, Col: {}'.format(x, y))
        self.charcount_label.setText('Chars: {}'.format(size))        

    def on_copy_available(self):
        self.statusBar().showMessage('Copy available!', 2000)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    editor = QEditor()
    editor.show()

    sys.exit(app.exec())
