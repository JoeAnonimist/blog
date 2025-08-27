import sys
import psutil

from PySide6.QtCore import Qt, QEvent, QTimer, QObject
from PySide6.QtWidgets import (QApplication, 
    QWidget, QLabel, QVBoxLayout)


class SystemMemoryEvent(QEvent):
    
    event_type = QEvent.Type(QEvent.registerEventType())
    
    def __init__(self, used):
        super().__init__(SystemMemoryEvent.event_type)
        self.used = used
    

class MemoryEventFilter(QObject):
        
    def eventFilter(self, watched, event):
        if event.type() == SystemMemoryEvent.event_type:
            print('In eventFilter(): ', event.used)
            watched.setText(str(event.used))
        return super().eventFilter(watched, event)

class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        self.resize(300, 200)
        self.setAcceptDrops(True)
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.label = QLabel('Hello, events!')
        self.label.setAlignment(Qt.AlignCenter)
        
        self.filter = MemoryEventFilter()
        self.label.installEventFilter(self.filter)
        layout.addWidget(self.label)
        
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.on_timeout)
        self.timer.start()
        
    def on_timeout(self):
        mem = psutil.virtual_memory().used / (1024 * 1024 * 1024)
        QApplication.postEvent(self.label, SystemMemoryEvent(mem))        
        QApplication.postEvent(self, SystemMemoryEvent(mem))

    def event(self, event):
        if event.type() == SystemMemoryEvent.event_type:
            print('In event(): ', event.used)
        return QWidget.event(self, event)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
