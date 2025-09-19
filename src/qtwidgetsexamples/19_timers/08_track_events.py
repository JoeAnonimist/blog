import sys
import time
from PySide6.QtCore import QObject, QTimer, Qt
from PySide6.QtGui import QInputEvent
from PySide6.QtWidgets import (QApplication, 
    QWidget, QLabel, QVBoxLayout)


class IdleFilter(QObject):
    
    def __init__(self, parent, window):
        
        super().__init__(parent)

        self.window = window
        self.is_idle = False
        self.last_ui_update = 0
        
        self.timer = QTimer()
        self.timer.setInterval(3000)
        self.timer.timeout.connect(self.on_timeout)
        self.timer.start()
        
    def on_timeout(self):
        
        print('timeout')
        self.window.label.setStyleSheet('background: lightgrey;')
        self.window.label.setText('Sleeping...')
        self.window.setWindowOpacity(0.8)
        self.is_idle = True

    def eventFilter(self, obj, event):
        
        if isinstance(event, QInputEvent):
            
            current_time = time.time()

            if self.is_idle and (current_time - self.last_ui_update >= 0.1):
                self.window.label.setStyleSheet('border: 1px solid grey;')
                self.window.label.setText('Stop user activity to sleep')
                self.window.setWindowOpacity(1.0)
                self.is_idle = False
                self.last_ui_update = current_time
            self.timer.start() # restarts timer
        return super().eventFilter(obj, event)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.resize(300, 200)
        self.setMouseTracking(True)
        
        self.label = QLabel('Stop user activity to sleep')
        self.label.setStyleSheet('border: 1px solid grey;')
        self.label.setAlignment(
            Qt.AlignmentFlag.AlignHCenter |
            Qt.AlignmentFlag.AlignVCenter)
        self.label.setMouseTracking(True)
        layout.addWidget(self.label)

        self.idle_filter = IdleFilter(self, self)
        QApplication.instance().installEventFilter(self.idle_filter)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
