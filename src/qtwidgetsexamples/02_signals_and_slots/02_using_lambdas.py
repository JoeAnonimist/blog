# If the signature of a signal matches 
# the signature of the receiving slot
# you can use the signal's arguments in the slot.
# If a slot has a shorter signature 
# than the signal it is connected with 
# the extra arguments are ignored

# Demonstrate using a Python lambda function
# as a slot. Lambdas are anonymous functions,
# ie. they have no name.


import sys

from PySide6.QtWidgets import (QApplication, 
    QWidget, QPushButton, QVBoxLayout)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1 - Create the widget, same as in the basic example
        
        button = QPushButton('Click me!')
        button.setCheckable(True)
        
        # 2 - In this case the slot is a Python lambda
        #     placed in the button.clicked.connect() call.
        
        button.clicked.connect(lambda: print('Clicked...'))
        button.clicked.connect(lambda checked: print(checked))
        
        layout.addWidget(button)
        

if __name__ == '__main__':
    
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    main_window = Window()
    main_window.show()
    
    sys.exit(app.exec())
