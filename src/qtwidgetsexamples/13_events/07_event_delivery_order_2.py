import sys

from PySide6.QtCore import QObject, QEvent
from PySide6.QtWidgets import (QApplication, QWidget, 
    QPushButton, QVBoxLayout)


class MyCustomApplication(QApplication):
    
    def notify(self, receiver, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            print('1. - QApplication.notify() for:',
                  receiver.objectName(),
                  id(event))
            #return True
        return super().notify(receiver, event)


class GlobalEventFilter(QObject):
        
    def eventFilter(self, watched, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            print('2. - Global event filter for: ',
                  watched.objectName(),
                  id(event))
            #return True
        return super().eventFilter(watched, event)


class TargetEventFilter(QObject):
        
    def eventFilter(self, watched, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            print('3. - Target event filter for: ',
                  watched.objectName(),
                  id(event))
            #return True
        return super().eventFilter(watched, event)


class MyCustomButton(QPushButton):
    
    def event(self, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            print('4. - MyCustomButton.event() for: ',
                  self.objectName(),
                  id(event))
            #return True
        return super().event(event)
    
    def mousePressEvent(self, event):
        print('5. - MyCustomButton.mousePressEvent() for: ',
              self.objectName(),
              id(event))
        super().mousePressEvent(event)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        self.setObjectName('Main Window')
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        button1 = MyCustomButton('Button 1')
        button1.setObjectName('button1')
        
        self.target_filter = TargetEventFilter()
        self.target_filter.setObjectName('Target event filter')
        button1.installEventFilter(self.target_filter)
        
        button1.clicked.connect(self.on_button_clicked)
        
        layout.addWidget(button1)
        layout.addStretch()
        
    def on_button_clicked(self):
        print('Button clicked: ', self.sender().objectName())
      

if __name__ == '__main__':

    app = MyCustomApplication(sys.argv)
    
    global_filter = GlobalEventFilter()
    global_filter.setObjectName('Global event filter')
    app.installEventFilter(global_filter)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())

