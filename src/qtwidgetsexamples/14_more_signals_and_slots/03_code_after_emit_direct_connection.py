import sys
from PySide6.QtCore import Signal, QThread
from PySide6.QtWidgets import (QApplication, 
    QWidget, QPushButton, QVBoxLayout)


class Window(QWidget):
    
    custom_signal = Signal()
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.button = QPushButton('Click me!')
        layout.addWidget(self.button)
        
        self.button.clicked.connect(self.on_button_clicked)
        
        self.custom_signal.connect(self.on_custom_signal_1)
        self.custom_signal.connect(self.on_custom_signal_2)
        self.custom_signal.connect(self.on_custom_signal_3)
    
    def on_button_clicked(self):
        print('Emitting custom signal')
        self.custom_signal.emit()
        print('Continue the button click slot execution')
        
    def on_custom_signal_1(self):
        print('First custom slot executed')
        QThread.sleep(1)
        
    def on_custom_signal_2(self):
        print('Second custom slot executed')
        QThread.sleep(1)
        
        
    def on_custom_signal_3(self):
        print('Third custom slot executed')
        QThread.sleep(1)


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()
    
    sys.exit(app.exec())

