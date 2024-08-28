# Displays a Hello, World! message in QLabel

# Import QLabel and QVBoxLayout

import sys
from PySide6.QtWidgets import (QApplication, 
    QWidget, QLabel, QVBoxLayout)

# 1 - Create a class that inherits from QMainWindow

class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        # 2 - Set window layout
        
        layout = QVBoxLayout()
        self.setLayout(layout)

        # 3 - Create a QLabel instance
        #     and add it to the window layout
        
        label = QLabel('Hello, World!', self)
        layout.addWidget(label)

# The boilerplate code is the same as in helloworld.py        

if __name__ == '__main__':

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
