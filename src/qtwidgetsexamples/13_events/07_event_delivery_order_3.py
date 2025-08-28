import sys
from PySide6.QtCore import QObject, QEvent
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class MyCustomApplication(QApplication):
    
    def notify(self, receiver, event):
        if event.type() == QEvent.Type.Resize:
            if isinstance(receiver, (MyCustomButton, MyCustomWindow)):
                print(f'QApplication.notify() for: {receiver.objectName()}', flush=True)
        return super().notify(receiver, event)


class MyCustomButton(QPushButton):
    
    def event(self, event):
        if event.type() == QEvent.Type.Resize:
            print(f'MyCustomButton.event() for: {self.objectName()}', flush=True)
        return super().event(event)
    
    def resizeEvent(self, event):
        print(f'MyCustomButton.resizeEvent() for: {self.objectName()}', flush=True)
        super().resizeEvent(event)


class MyCustomWindow(QWidget):
    
    def event(self, event):
        if event.type() == QEvent.Type.Resize:
            print(f'MyCustomWindow.event() for: {self.objectName()}', flush=True)
        return super().event(event)
    
    def resizeEvent(self, event):
        print(f'MyCustomWindow.resizeEvent() for: {self.objectName()}', flush=True)
        super().resizeEvent(event)


class ResizeEventFilter(QObject):
        
    def eventFilter(self, watched, event):
        if event.type() == QEvent.Type.Resize:
            print(f'{self.objectName()} for: {watched.objectName()}', flush=True)
        return super().eventFilter(watched, event)


class Window(MyCustomWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setObjectName('Main Window')
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        button1 = MyCustomButton('Button 1')
        button1.setObjectName('button1')
        
        self.filter_obj = ResizeEventFilter()
        self.filter_obj.setObjectName('MyCustomWindow event filter')
        self.installEventFilter(self.filter_obj)  # Fix: Install filter on Main Window
        button1.installEventFilter(self.filter_obj)
        
        layout.addWidget(button1)
        layout.addStretch()


if __name__ == '__main__':
    app = MyCustomApplication(sys.argv)
    app.setObjectName('My custom app')
    
    filter_obj = ResizeEventFilter()
    filter_obj.setObjectName('QApplication event filter')
    app.installEventFilter(filter_obj)

    main_window = Window()
    main_window.show()
    main_window.resize(400, 300)  # Trigger Resize event
    app.processEvents()  # Ensure Resize is processed

    sys.exit(app.exec())