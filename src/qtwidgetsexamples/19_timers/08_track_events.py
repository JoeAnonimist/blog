import sys

from PySide6.QtCore import QObject, QEvent
from PySide6.QtGui import QInputEvent
from PySide6.QtWidgets import (QApplication, 
    QWidget, QLabel, QVBoxLayout)


class MousePressFilter(QObject):
        
    def eventFilter(self, watched, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            print('Filter mouse press for: ', watched.objectName())
            if watched.objectName() == 'button2':
                return True
        return super().eventFilter(watched, event)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        label = QLabel()
        layout.addWidget(label)
        
        #event_filter = MousePressFilter(self)
        #self.installEventFilter(event_filter)
        
    def event(self, event):
        if isinstance(event, QInputEvent):
            print(event)
        return super().event(self, event)

      

if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
