import sys
from PySide6.QtCore import QTimer, Slot, QTime
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
        
        self.label = QLabel()
        layout.addWidget(self.label)
        
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.on_timeout)
    
    @Slot()
    def on_button_clicked(self):
        self.button.setDisabled(True)
        self.timer.start()
        
    @Slot()
    def on_timeout(self):
        self.label.setText(
            QTime.currentTime().toString('hh:mm:ss'))
      

if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
