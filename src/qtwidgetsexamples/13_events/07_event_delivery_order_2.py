import sys

from PySide6.QtCore import QObject, QEvent
from PySide6.QtWidgets import (QApplication, QWidget, 
    QPushButton, QVBoxLayout)


class MyCustomApplication(QApplication):
    
    def notify(self, receiver, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            if receiver.objectName() == 'button1':
                print('QApplication.notify() for:', receiver.objectName())
        return super().notify(receiver, event)


class MousePressFilter(QObject):
        
    def eventFilter(self, watched, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            print(self.objectName(), 'for: ', watched.objectName())
        return super().eventFilter(watched, event)


class MyCustomButton(QPushButton):
    
    def event(self, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            print('MyCustomButton.event() for: ', self.objectName())
        return super().event(event)
    
    def mousePressEvent(self, event):
        print('MyCustomButton.mousePressEvent() for: ', self.objectName())
        super().mousePressEvent(event)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        self.setObjectName('Main Window')
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        button1 = MyCustomButton('Button 1')
        button1.setObjectName('button1')
        
        self.filter_obj = MousePressFilter()
        self.filter_obj.setObjectName('MyCustomButton event filter')
        button1.installEventFilter(self.filter_obj)
        
        button1.clicked.connect(self.on_button_clicked)
        
        layout.addWidget(button1)
        layout.addStretch()
        
    def on_button_clicked(self):
        print('Button clicked: ', self.sender().objectName())
      

if __name__ == '__main__':

    app = MyCustomApplication(sys.argv)
    
    filter_obj = MousePressFilter()
    filter_obj.setObjectName('QApplication event filter')
    app.installEventFilter(filter_obj)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())


'''
[1] QEvent generated (MouseButtonPress, spontaneous, ID1)
    │
    ▼
[2] Qt event dispatcher
    │
    ├── [2a] 🌍 App-level event filters (pre-notify)
    │         e.g., app.installEventFilter(MousePressFilter())
    │         └─ filter.eventFilter(receiver=window, event=ID1)
    │              └─ print("watched:", watched.objectName(), "event:", id(event))  # Not in code anymore
    │              └─ If watched == 'button1': print("QApplication event filter for:", watched)
    │              Output: (None, condition fails for watched='Main WindowWindow')
    │              Note: Would print "watched: Main WindowWindow event: <ID1>" if print was active
    │
    └── [2b] Calls QApplication::notify(receiver=window, event=ID1)
          │
          ├── [2b1] 🔍 Your custom notify()
          │         └─ If receiver == 'button1': print("QApplication.notify() for:", receiver.objectName())
          │         (No print for window, condition fails)
          │
          └── [2b2] super().notify(window, ID1)
                │
                ├── [2b2a] Qt's QApplication::notify (for window, ID1)
                │    │
                │    ├── Check focus, tooltips, etc.
                │    ├── Pick child: pickMouseReceiver(window, globalPos) → button1
                │    ├── Create new QMouseEvent (ID2, localPos for button1)
                │    └── Direct recursive call: this->notify(button1, ID2)
                │          │
                │          ├── [2b2a1] 🔍 Your custom notify()
                │          │         └─ print("QApplication.notify() for: button1")
                │          │         Output: **1** "QApplication.notify() for: button1"
                │          │
                │          └── [2b2a2] super().notify(button1, ID2)
                │                │
                │                ├── [3a] 🌍 App-level event filters (inside notify_helper)
                │                │         └─ filter.eventFilter(button1, ID2)
                │                │              └─ print("QApplication event filter for: button1")
                │                │              Output: **2** "QApplication event filter for: button1"
                │                │
                │                ├── [3b] 🎯 Object-specific filters
                │                │         └─ button1's filter.eventFilter(button1, ID2)
                │                │              └─ print("MyCustomButton event filter for: button1")
                │                │              Output: **3** "MyCustomButton event filter for: button1"
                │                │
                │                ├── [3c] 🔄 button1.event(ID2)
                │                │         └─ print("MyCustomButton.event() for: button1")
                │                │         └─ Dispatches to mousePressEvent
                │                │         Output: **4** "MyCustomButton.event() for: button1"
                │                │
                │                ├── [3d] 🖱️ mousePressEvent(ID2)
                │                │         └─ print("MyCustomButton.mousePressEvent() for: button1")
                │                │         └─ Base QPushButton accepts event
                │                │         Output: **5** "MyCustomButton.mousePressEvent() for: button1"
                │                │
                │                └── [3e] 🔔 Signals (on separate MouseButtonRelease)
                │                          └─ emit clicked()
                │                          Output: **6** "Button clicked: button1"
                │
                └── [2b2b] If event unaccepted, propagate to parent (not here, ID2 accepted)
'''