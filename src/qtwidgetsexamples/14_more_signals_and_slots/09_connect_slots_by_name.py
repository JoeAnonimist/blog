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
        
        layout.addWidget(self.button_1)
        layout.addWidget(self.button_2)
        
        QMetaObject.connectSlotsByName(self)

    @Slot()
    def on_myButton_clicked(self):
        print('Slot without the argument')
        
    # If this is commented out the above slot gets connected.
    # If this is not commented out the above slot
    # is skipped and this one gets connected.

    @Slot(bool)
    def on_myButton_clicked(self, checked):
        print('Slot with the argument')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())