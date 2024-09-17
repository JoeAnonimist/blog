# Demonstrate how to stack widgets vertically
# using QVBoxLayout. 
# QVBoxLayout stands for 'vertical box layout object'

from PySide6.QtWidgets import (QApplication, 
    QWidget, QPushButton, QVBoxLayout)
import sys


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        # 1 - Create the layout object
        #     and set it as our window layout
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 2 - Create widgets
        
        button_1 = QPushButton('Button 1')
        button_2 = QPushButton('Button 2')
        button_3 = QPushButton('Button 3')
        
        # 3 - Add widgets to the layout
        
        layout.addWidget(button_1)
        layout.addWidget(button_2)
        layout.addWidget(button_3)
        
        # Handle button events for demonstration purposes
        # Note how I reused the same method (on_button_clicked)
        # as the slot for all three button widgets.

        button_1.clicked.connect(self.on_button_clicked)
        button_2.clicked.connect(self.on_button_clicked)
        button_3.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self) :
        
        # Inside the slot use self.sender()
        # to check which button was clicked:
        
        print(self.sender().text() + ' clicked.')



if __name__ == '__main__':

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())