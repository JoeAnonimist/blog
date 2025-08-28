import sys

from PySide6.QtCore import QObject, QEvent
from PySide6.QtWidgets import (QApplication, QWidget, 
    QPushButton, QVBoxLayout)


class MyCustomApplication(QApplication):
    
    def notify(self, receiver, event):
        if event.type() == QEvent.Type.Show:
            if isinstance(receiver, MyCustomButton):
                print('QApplication.notify() for: ', receiver.objectName())
        return super().notify(receiver, event)


class MyCustomButton(QPushButton):
    
    def event(self, event):
        if event.type() == QEvent.Type.Show:
            print('MyCustomButton.event() for: ', self.objectName())
        return super().event(event)
    
    def showEvent(self, event):
        print('MyCustomButton.showEvent() for: ', self.objectName())
        super().showEvent(event)


class ShowEventFilter(QObject):
        
    def eventFilter(self, watched, event):
        if event.type() == QEvent.Type.Show:
            print(self.objectName(), 'for: ', watched.objectName())
        return super().eventFilter(watched, event)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        #self.setObjectName('Main Window')
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        button1 = MyCustomButton('Button 1')
        button1.setObjectName('button1')
        
        self.filter_obj = ShowEventFilter()
        self.filter_obj.setObjectName('MyCustomButton event filter')
        button1.installEventFilter(self.filter_obj)
        
        layout.addWidget(button1)
        layout.addStretch()


if __name__ == '__main__':

    app = MyCustomApplication(sys.argv)
    app.setObjectName('My custom app')
    
    filter_obj = ShowEventFilter()
    filter_obj.setObjectName('QApplication event filter')
    app.installEventFilter(filter_obj)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())