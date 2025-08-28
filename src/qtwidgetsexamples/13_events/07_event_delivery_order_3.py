import sys

from PySide6.QtCore import QObject, QEvent
from PySide6.QtWidgets import (QApplication, QWidget, 
    QPushButton, QGroupBox, QVBoxLayout)


class MyCustomApplication(QApplication):
    
    def notify(self, receiver, event):
        if event.type() == QEvent.Type.KeyPress:
            print('1. - QApplication.notify() for:',
                  receiver.objectName(),
                  id(event))
            #return True
        return super().notify(receiver, event)


class GlobalEventFilter(QObject):
        
    def eventFilter(self, watched, event):
        if event.type() == QEvent.Type.KeyPress:
            print('2. - Global event filter for: ',
                  watched.objectName(),
                  id(event))
            #return True
        return super().eventFilter(watched, event)


class TargetEventFilter(QObject):
        
    def eventFilter(self, watched, event):
        if event.type() == QEvent.Type.KeyPress:
            print('3. - Target event filter for: ',
                  watched.objectName(),
                  id(event))
            #return True
        return super().eventFilter(watched, event)


class MyCustomButton(QPushButton):
    
    def event(self, event):
        if event.type() == QEvent.Type.KeyPress:
            print('4. - MyCustomButton.event() for: ',
                  self.objectName(),
                  id(event))
            #return True
        return super().event(event)
    
    def keyPressEvent(self, event):
        print('5. - MyCustomButton.keyPressEvent() for: ',
              self.objectName(),
              id(event))
        super().mousePressEvent(event)
        #return True


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        self.setObjectName('Main Window')
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        group_box = QGroupBox()
        group_box.setTitle('Parent groupbox')
        
        button1 = MyCustomButton('Button 1')
        button1.setObjectName('button1')
        group_box.setLayout(QVBoxLayout())
        group_box.layout().addWidget(button1)
        
        self.target_filter = TargetEventFilter()
        self.target_filter.setObjectName('Target event filter')
        button1.installEventFilter(self.target_filter)
        
        layout.addWidget(group_box)
        layout.addStretch()
      

if __name__ == '__main__':

    app = MyCustomApplication(sys.argv)
    
    global_filter = GlobalEventFilter()
    global_filter.setObjectName('Global event filter')
    app.installEventFilter(global_filter)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())

