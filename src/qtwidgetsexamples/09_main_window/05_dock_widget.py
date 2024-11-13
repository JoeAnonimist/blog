# The QDockWidget class provides a widget that can be 
# docked inside a QMainWindow or floated 
# as a top-level window on the desktop

import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon, QTextCharFormat, QFont
from PySide6.QtWidgets import (QApplication, QMainWindow,
    QTextEdit, QLabel, QMessageBox, QVBoxLayout, QPushButton,
    QSpinBox, QDockWidget, QWidget)


class QEditor(QMainWindow):
    
    def __init__(self):

        super().__init__()

        self.text_edit = QTextEdit()        
        self.setCentralWidget(self.text_edit)

        self.label = QLabel()
        self.statusBar().addWidget(self.label)
        
        self.text_edit.textChanged.connect(self.on_text_changed)
        
        menu_bar = self.menuBar()
        
        file_menu = menu_bar.addMenu('&File')
        
        exit_action = QAction(self)
        exit_action.setText('&Exit')
        exit_action.setIcon(QIcon('./icons/exit.png'))
        exit_action.triggered.connect(QApplication.quit)
        
        file_menu.addAction(exit_action)
          
        help_menu = menu_bar.addMenu('&Help')
        
        about_action = QAction(self)
        about_action.setText('&About')
        about_action.setIcon(QIcon('./icons/about.png'))
        about_action.triggered.connect(self.show_messagebox)
        
        help_menu.addAction(about_action)
        
        file_toolbar = self.addToolBar('File')
        file_toolbar.addAction(exit_action)
        file_toolbar.addAction(about_action)
        file_toolbar.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        
        # 1. Create the dock widget
            
        dock_widget = QDockWidget()
        dock_widget.setMaximumWidth(50)
        dock_widget.setAllowedAreas(
            Qt.DockWidgetArea.LeftDockWidgetArea | Qt.DockWidgetArea.RightDockWidgetArea)
            
        vbox = QVBoxLayout()
        
        button_bold = QPushButton()
        button_bold.setIcon(QIcon('./icons/bold.png'))
        button_bold.setCheckable(True)
        button_bold.setProperty('style', 'bold')
        button_bold.clicked.connect(self.on_button_bold_clicked)
        
        button_italic = QPushButton()
        button_italic.setIcon(QIcon('./icons/italic.png'))
        button_italic.setCheckable(True)
        button_italic.setProperty('style', 'italic')
        button_italic.clicked.connect(self.on_button_italic_clicked)
        
        font_size_spinbox = QSpinBox()
        font_size_spinbox.setMinimum(1)
        font_size_spinbox.setMaximum(24)
        font_size_spinbox.valueChanged.connect(self.on_value_changed)
        
        vbox.addWidget(button_bold)
        vbox.addWidget(button_italic)
        vbox.addWidget(font_size_spinbox)
        vbox.addStretch()
        
        container = QWidget()
        container.setLayout(vbox)
        
        dock_widget.setWidget(container)
        
        # 2. Add the dock widget to the main window
        
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, dock_widget)
    
    def on_text_changed(self):

        cursor = self.text_edit.textCursor()
        
        size = len(self.text_edit.toPlainText())
        x = str(cursor.blockNumber() + 1)
        y = str(cursor.columnNumber() + 1)
        
        self.label.setText('Chars: {}, Ln: {}, Col: {}'.format(size, x, y))
        
    def show_messagebox(self):
        
        messagebox = QMessageBox()
        messagebox.setText('PyQt menu example')
        messagebox.exec()
    
    # 3. Handle the dock widget children signals
    
    def on_button_bold_clicked(self):

        sender = self.sender()
        format = QTextCharFormat()
        
        if sender.isChecked():
            format.setFontWeight(QFont.Weight.Bold)
        else:
            format.setFontWeight(QFont.Weight.Normal)
        
        cursor = self.text_edit.textCursor()
        self.text_edit.mergeCurrentCharFormat(format)
        self.text_edit.setFocus(Qt.FocusReason.OtherFocusReason)
        
    def on_button_italic_clicked(self):
        
        sender = self.sender()
        format = QTextCharFormat()
        
        if self.sender().isChecked():
            format.setFontItalic(True)
        else:
            format.setFontItalic(False)
            
        cursor = self.text_edit.textCursor()
        self.text_edit.mergeCurrentCharFormat(format)
        self.text_edit.setFocus(Qt.FocusReason.OtherFocusReason)
        
    def on_value_changed(self, i):
        
        format = QTextCharFormat()
        format.setFontPointSize(i)
        
        cursor = self.text_edit.textCursor()
        self.text_edit.mergeCurrentCharFormat(format)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    editor = QEditor()
    editor.show()

    sys.exit(app.exec())
