import sys
from PySide6.QtCore import QTimer, Slot, QTime
from PySide6.QtWidgets import (QApplication, QWidget,
    QPushButton,  QVBoxLayout, QPlainTextEdit)

class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.start_button = QPushButton('Start timers')
        self.start_button.clicked.connect(self.on_start_button_clicked)
        layout.addWidget(self.start_button)
        
        self.stop_button = QPushButton('Stop timers')
        self.stop_button.setDisabled(True)
        self.stop_button.clicked.connect(self.on_stop_button_clicked)
        layout.addWidget(self.stop_button)
        
        self.text_edit = QPlainTextEdit()
        layout.addWidget(self.text_edit)
        
        self.timer1 = QTimer()
        self.timer1.setSingleShot(True)
        self.timer1.timeout.connect(self.slot2)
        
        self.timer2 = QTimer()
        self.timer2.setSingleShot(True)
        self.timer2.timeout.connect(self.slot1)
    
    @Slot()
    def on_start_button_clicked(self):
        
        self.should_terminate = False
        self.start_button.setDisabled(True)
        self.stop_button.setEnabled(True)
        self.slot1()
        
    @Slot()
    def on_stop_button_clicked(self):
        self.should_terminate = True
        self.stop_button.setDisabled(True)
        self.start_button.setEnabled(True)
        
    @Slot()
    def slot1(self):
        self.text_edit.appendPlainText(f'in slot1(): {QTime.currentTime().toString("mm:ss")}')
        if not self.should_terminate:
            self.timer1.start(2000)
        
    @Slot()
    def slot2(self):
        self.text_edit.appendPlainText(f'in slot2(): {QTime.currentTime().toString("mm:ss")}')
        if not self.should_terminate:
            self.timer2.start(3000)
      

if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())