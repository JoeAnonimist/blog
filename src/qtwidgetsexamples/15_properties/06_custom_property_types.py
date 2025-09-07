import sys
from PySide6.QtCore import Property, Signal, Qt, QThread, QObject, QMetaType
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PySide6.QtGui import QTextCursor

# Define the Message class
class Message:
    def __init__(self):
        self.cursor = QTextCursor()
        self.body = '<body>'
        self.headers = '<headers>'

# Worker class running in a separate thread
class Worker(QObject):
    messageSignal = Signal(QTextCursor)

    def __init__(self):
        super().__init__()

    def do_work(self):
        # Simulate work in another thread
        message = Message()
        message.body = 'Thread Body'
        message.headers = 'Thread Headers'
        self.messageSignal.emit(message.cursor)

class MyLabel(QLabel):
    
    messageChanged = Signal(QTextCursor, QTextCursor)

    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self._message = Message()

    def getMessage(self):
        return self._message.cursor

    def setMessage(self, cursor):
        old_cursor = self._message.cursor
        self._message.cursor = cursor
        self.messageChanged.emit(old_cursor, cursor)

    message = Property(QTextCursor, fget=getMessage, fset=setMessage, notify=messageChanged)

class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Register Message as a Qt meta-type (required for cross-thread signals)
        # Create a QMetaType instance for the Message type
        message_type = QMetaType(Message)
        message_type.registerType()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = MyLabel('Hello, World!', self)
        self.label.messageChanged.connect(self.on_message_changed, Qt.ConnectionType.QueuedConnection)

        layout.addWidget(self.label)

        button = QPushButton('Start Thread')
        layout.addWidget(button)
        button.clicked.connect(self.on_button_clicked)

        # Set up the worker thread
        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.worker.messageSignal.connect(self.label.setMessage, Qt.ConnectionType.QueuedConnection)
        self.thread.started.connect(self.worker.do_work)
        self.thread.start()

    def on_message_changed(self, old, new):
        print('Message changed:')
        print(old)
        print(new)

    def on_button_clicked(self):
        # Trigger the worker to emit a signal from the thread
        self.worker.do_work()

    def closeEvent(self, event):
        # Clean up the thread on window close
        self.thread.quit()
        self.thread.wait()
        super().closeEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Register the Message type before using it
    #message_type = QMetaType(Message)
    #message_type.registerType()

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())