# The QLineEdit widget is a one-line text editor. 

from PySide6.QtWidgets import (QApplication, 
    QWidget, QVBoxLayout, QLineEdit, QLabel)
import sys


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1 - Create a line edit widget instance
        
        self.line_edit = QLineEdit()
        self.label = QLabel()
        
        # 3 - Connect the signal and the slot
        
        self.line_edit.textChanged.connect(self.on_text_changed)
        
        layout.addWidget(self.line_edit)
        layout.addWidget(self.label)
        
        
    # 2 - Create a method to handle 
    #     line edit text changed events.
        
    def on_text_changed(self):
        self.label.setText(self.line_edit.text())


if __name__ == '__main__':

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())