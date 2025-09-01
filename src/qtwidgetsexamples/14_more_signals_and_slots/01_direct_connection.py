import sys
from PySide6.QtWidgets import (QApplication, 
    QWidget, QPushButton, QVBoxLayout, )


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.button = QPushButton('Click me!')
        layout.addWidget(self.button)
        
        self.conn = self.button.clicked.connect(
            self.on_button_clicked)
        
        self.disconnect_button = QPushButton('Disconnect')
        layout.addWidget(self.disconnect_button)
        self.disconnect_button.clicked.connect(
            self.on_disconnect_button_clicked)
    
    def on_button_clicked(self):
        print('Button clicked')
        
    def on_disconnect_button_clicked(self):
        print('Disconnecting...')
        if self.conn:
            self.button.clicked.disconnect(self.conn)
        else:
            print('Already disconnected')


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()
    
    sys.exit(app.exec())