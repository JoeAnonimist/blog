import sys
from PySide6.QtCore import QMetaObject, Slot
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.button_1 = QPushButton('Click me!')
        self.button_1.setObjectName('myButton')
        
        self.button_2 = QPushButton('Click me too!')
        self.button_2.setObjectName('myButton')
        
        layout.addWidget(self.button_1)  # Add button_1
        layout.addWidget(self.button_2)  # Add button_2 (fixed)
        
        QMetaObject.connectSlotsByName(self)  # Auto-connect signals to slots

    @Slot(bool)
    def on_myButton_clicked(self, checked):
        print(checked)
        print(self.sender())

    '''
    @Slot()
    def on_myButton_clicked(self):
        print(self.sender())
    '''   
    '''
    @Slot()
    def on_button1_clicked(self):  # Slot for button_2 (objectName="button1")
        print('Button 2 (button1) clicked')
    '''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())