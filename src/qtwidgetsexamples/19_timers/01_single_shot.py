import sys
from PySide6.QtCore import QTimer, Slot
from PySide6.QtWidgets import (QApplication, 
    QWidget, QPushButton, QLabel, QVBoxLayout)

class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.button = QPushButton('Start timer')
        self.button.clicked.connect(self.on_button_clicked)
        layout.addWidget(self.button)
        
        self.label = QLabel('Start the timer')
        layout.addWidget(self.label)
        
        self.timer = QTimer()
    
    @Slot()
    def on_button_clicked(self):
        self.button.setDisabled(True)
        self.label.setText('Waiting...')
        self.timer.singleShot(1000, self.on_single_shot)
        
    @Slot()
    def on_single_shot(self):
        self.label.setText('Done!')
        self.button.setEnabled(True)
        
      

if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
