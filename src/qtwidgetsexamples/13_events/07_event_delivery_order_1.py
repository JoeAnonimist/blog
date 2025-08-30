import sys

from PySide6.QtCore import QObject, QEvent
from PySide6.QtWidgets import (QApplication, QWidget)


class MyCustomApplication(QApplication):
    
    def notify(self, receiver, event):
        if event.type() == QEvent.Type.Show:
            print('1. - QApplication.notify() for: ', receiver.objectName())
            # return True
        return super().notify(receiver, event)


class GlobalEventFilter(QObject):
        
    def eventFilter(self, watched, event):
        if event.type() == QEvent.Type.Show:
            print('2. - Global event filter for: ', watched.objectName())
            # return True
        return super().eventFilter(watched, event)


class TargetEventFilter(QObject):
        
    def eventFilter(self, watched, event):
        if event.type() == QEvent.Type.Show:
            print('3. - Target event filter for: ', watched.objectName())
            # return True
        return super().eventFilter(watched, event)


class Window(QWidget):
        
    def event(self, event):
        if event.type() == QEvent.Type.Show:
            print('4. - Window.event() for: ', self.objectName())
            # return True
        return super().event(event)
    
    def showEvent(self, event):
        print('5. - Window.showEvent() for: ', self.objectName())
        super().showEvent(event)


if __name__ == '__main__':

    app = MyCustomApplication(sys.argv)
   
    global_filter = GlobalEventFilter()
    app.installEventFilter(global_filter)

    main_window = Window()
    main_window.setObjectName('MyWindow')
    
    target_filter = TargetEventFilter()
    main_window.installEventFilter(target_filter)
    
    main_window.show()

    sys.exit(app.exec())