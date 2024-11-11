#  QMainWindow has its own layout to which you can add 
# QToolBars, QDockWidgets, a QMenuBar, and a QStatusBar. 
# The layout has a center area that can be occupied 
# by any kind of widget. In this case we use QTextEdit

import sys

from PySide6.QtWidgets import (QApplication, QMainWindow,
    QTextEdit)


# 1 - Create a class that inherits QMainWindow
class Editor(QMainWindow):
    
    def __init__(self):

        super().__init__()
        
        # 2 - Create a widget
        
        text_edit = QTextEdit()        
        
        # 3 - Set the widget as QMainWindow central widget
        
        self.setCentralWidget(text_edit)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    editor = Editor()
    editor.show()

    sys.exit(app.exec())
