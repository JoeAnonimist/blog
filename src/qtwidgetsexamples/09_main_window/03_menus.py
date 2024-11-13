# The QMenu class provides a menu widget for use 
# in menu bars, context menus, and other popup menus. 

# The QAction class provides an abstraction for user commands
# Same action objects can be added to 
# menus, toolbars and keyboard shortcuts.

import sys

from PySide6.QtGui import QAction
from PySide6.QtWidgets import (QApplication, QMainWindow,
    QTextEdit, QLabel, QMessageBox)


class Editor(QMainWindow):
    
    def __init__(self):

        super().__init__()

        self.text_edit = QTextEdit()        
        self.setCentralWidget(self.text_edit)

        self.label = QLabel()
        self.statusBar().addWidget(self.label)
        
        self.text_edit.textChanged.connect(self.on_text_changed)
        
        # You can access the main window QMenuBar
        # using QMainWindow.menuBar()
        
        menu_bar = self.menuBar()
        
        # 1 - Create a QMenu instance using QMenuBar.addMenu() 
        #     Use the ampersand to make keyboard shortcuts work.
        
        file_menu = menu_bar.addMenu('&File')
        
        # 2 - Create a QAction instance.
        #     Connect a slot to its triggered signal.
        #     Set Editor as QAction's parent.
        
        exit_action = QAction(self)
        exit_action.setText('Exit')
        exit_action.setShortcut('Alt+X')
        exit_action.triggered.connect(QApplication.quit)
        
        # 3 - Add action to the menu.
        
        file_menu.addAction(exit_action)
        
        
        # Repeat the steps for each menu item
        
        help_menu = menu_bar.addMenu('&Help')
        
        about_action = QAction(self)
        about_action.setText('About')
        about_action.triggered.connect(self.show_messagebox)
        
        help_menu.addAction(about_action)
    
    def on_text_changed(self):
        
        cursor = self.text_edit.textCursor()
        
        size = len(self.text_edit.toPlainText())
        x = str(cursor.blockNumber() + 1)
        y = str(cursor.columnNumber() + 1)
        
        self.label.setText('Chars: {}, Ln: {}, Col: {}'.format(size, x, y))
        
    def show_messagebox(self):
        
        messagebox = QMessageBox()
        messagebox.setText('PySide6 menu example')
        messagebox.exec()


if __name__ == '__main__':

    app = QApplication(sys.argv)

    editor = Editor()
    editor.show()

    sys.exit(app.exec())
