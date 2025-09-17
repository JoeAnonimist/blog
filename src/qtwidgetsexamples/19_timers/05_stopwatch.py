import sys
from PySide6.QtCore import QTimer, QTime, Slot, Qt
from PySide6.QtWidgets import (QApplication, QWidget,
    QPushButton, QLabel, QVBoxLayout)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        self.elapsed_time = QTime(0, 0, 0, 0)
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.start_button = QPushButton('Start')
        self.start_button.clicked.connect(self.on_start_button_clicked)
        layout.addWidget(self.start_button)
        
        self.pause_button = QPushButton('Pause')
        self.pause_button.setDisabled(True)
        self.pause_button.clicked.connect(self.on_pause_button_clicked)
        layout.addWidget(self.pause_button)
        
        self.reset_button = QPushButton('Reset')
        self.reset_button.clicked.connect(self.on_reset_button_clicked)
        layout.addWidget(self.reset_button)

        self.label = QLabel(self.elapsed_time.toString('mm:ss.z'))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.on_timeout)
    
    @Slot()
    def on_start_button_clicked(self):
        self.start_button.setDisabled(True)
        self.pause_button.setEnabled(True)
        self.timer.start()
        
    @Slot()
    def on_pause_button_clicked(self):
        self.timer.stop()
        self.start_button.setEnabled(True)
        self.pause_button.setDisabled(True)
    
    @Slot()
    def on_reset_button_clicked(self):
        self.elapsed_time = QTime(0, 0, 0, 0)
        self.label.setText(self.elapsed_time.toString('mm:ss.z'))
        
    @Slot()
    def on_timeout(self):
        self.elapsed_time = self.elapsed_time.addMSecs(100)
        self.label.setText(self.elapsed_time.toString('mm:ss.z'))
      

if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
