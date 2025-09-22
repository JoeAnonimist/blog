import sys
from PySide6.QtWidgets import (QApplication, 
    QWidget, QPushButton, QVBoxLayout)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        self.setObjectName('Main Window')
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.create_button = QPushButton('Create button')
        self.create_button.clicked.connect(self.create_external_button)
        
        self.adopt_button = QPushButton('Adopt button')
        self.adopt_button.clicked.connect(self.adopt_external_button)
        
        layout.addWidget(self.create_button)
        layout.addWidget(self.adopt_button)
        
        self.orphans = []
        
    def create_external_button(self):

        button = QPushButton(f'button-{len(self.orphans)}')
        self.orphans.append(button)
        button.show()
        
    def adopt_external_button(self):
        
        if self.orphans:
            button = self.orphans.pop()
            button.setParent(self)
            self.layout().addWidget(button)


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()
    
    sys.exit(app.exec())
