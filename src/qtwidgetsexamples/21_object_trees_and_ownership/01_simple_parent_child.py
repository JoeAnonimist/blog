import sys
from PySide6.QtWidgets import (QApplication, 
    QWidget, QPushButton, QVBoxLayout)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        self.setObjectName('Main Window')
        self.setMinimumHeight(150)
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        button1 = QPushButton('Button 1', self)
        button2 = QPushButton('Button 2')
        button3 = QPushButton('Button 3', self)
        button4 = QPushButton('Button 4')
        self.button5 = QPushButton('Button 5')
        
        button1.clicked.connect(self.on_button1_clicked)
        
        layout.addWidget(button1)
        layout.addWidget(button2)
        
        print('Button 1 parent: ', button1.parent().objectName())
        print('Button 2 parent: ', button2.parent().objectName())
        print('Button 3 parent: ', button3.parent().objectName())
        print('Button 4 parent: ', button4.parent())
        print('Button 5 parent: ', self.button5.parent())
        
    def on_button1_clicked(self):
        for member in dir(self):
            if member.startswith('button'):
                print(member)


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()
    
    sys.exit(app.exec())
