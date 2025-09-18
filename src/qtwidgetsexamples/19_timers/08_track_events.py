import sys
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QInputEvent
from PySide6.QtWidgets import (QApplication, 
    QWidget, QLabel, QVBoxLayout)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.resize(300, 200)
        # self.setMouseTracking(True)
        
        self.label = QLabel('Stop user activity to sleep')
        self.label.setStyleSheet('border: 1px solid grey;')
        self.label.setAlignment(
            Qt.AlignmentFlag.AlignHCenter |
            Qt.AlignmentFlag.AlignVCenter)
        # self.label.setMouseTracking(True)
        layout.addWidget(self.label)
        
        self.timer = QTimer()
        self.timer.setInterval(3000)
        self.timer.timeout.connect(self.on_timeout)
        self.timer.start()
        
    def on_timeout(self):
        print('timeout')
        self.label.setStyleSheet('background: lightgrey;')
        self.label.setText('Sleeping...')
        
    def event(self, event):
        if isinstance(event, QInputEvent):
            print(event)
            self.label.setStyleSheet('border: 1px solid grey;')
            self.label.setText('Stop user activity to sleep')
            self.timer.start()
        return super().event(event)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
