import sys
from PySide6.QtCore import QTimer, Slot
from PySide6.QtWidgets import (QApplication,
    QWidget, QPushButton, QLabel, QVBoxLayout)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        self.counter = 0
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.start_button = QPushButton('Start timer')
        self.start_button.clicked.connect(self.on_start_button_clicked)
        layout.addWidget(self.start_button)
        
        self.stop_button = QPushButton('Stop timer')
        self.stop_button.clicked.connect(self.on_stop_button_clicked)
        self.stop_button.setEnabled(False)
        layout.addWidget(self.stop_button)
        
        self.label = QLabel(str(self.counter))
        layout.addWidget(self.label)
        
        self.timer = QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.on_timeout)
    
    @Slot()
    def on_start_button_clicked(self):
        self.start_button.setDisabled(True)
        self.stop_button.setEnabled(True)
        self.timer.start()
        
    @Slot()
    def on_stop_button_clicked(self):
        self.start_button.setEnabled(True)
        self.stop_button.setDisabled(True)
        self.timer.stop()
        
    @Slot()
    def on_timeout(self):
        self.counter += 1
        self.label.setText(str(self.counter))
      

if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
