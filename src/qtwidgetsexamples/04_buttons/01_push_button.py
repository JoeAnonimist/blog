# QPushButton generates 'clicked' signals when you click it duh

from PySide6.QtWidgets import (QApplication, 
    QPushButton, QLabel, QWidget, QVBoxLayout)
from PySide6.QtCore import Qt
import sys
from random import randint


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1 - Create the button and add it to the window layout
        
        button = QPushButton('Generate random integer')
        
        # 3 - Connect the button clicked event with the slot
        
        button.clicked.connect(self.on_button_clicked)
        
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout.addWidget(button)
        layout.addWidget(self.label)
    
    # 2 - Create the method/function to use as the slot
    
    def on_button_clicked(self):
        self.label.setText(str(randint(0, 100)))


if __name__ == '__main__':

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())