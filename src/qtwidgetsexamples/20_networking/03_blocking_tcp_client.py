import sys

from PySide6.QtCore import (QObject, QRunnable,
    QThreadPool, Slot, Signal, Qt)
from PySide6.QtNetwork import (QTcpSocket, QTcpServer,
    QHostAddress)
from PySide6.QtWidgets import (QApplication, QWidget, 
    QPlainTextEdit, QLineEdit, QPushButton, QVBoxLayout)


class Signals(QObject):
    connected = Signal()
    sent = Signal(str)
    received = Signal(str)
    disconnected = Signal()

class Runnable(QRunnable):
    
    def __init__(self, message, parent=None):
        super().__init__(parent)
        self.signals = Signals()
        self.message = message

    def run(self):
        
        socket = QTcpSocket()
        socket.connectToHost('localhost', 1234)
        socket.waitForConnected()
        #print('connected')
        self.signals.connected.emit()
        socket.write(self.message.encode())
        socket.waitForBytesWritten()
        self.signals.sent.emit(self.message)
        #print('bytes written')
        socket.waitForReadyRead()
        #print(socket.readAll().data().decode())
        response = socket.readAll().data().decode()
        self.signals.received.emit(response)
        socket.waitForDisconnected()
        print('Disconnected')
        self.signals.disconnected.emit()
        self.signals.deleteLater()


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.send_button = QPushButton('Send message')
        self.send_button.clicked.connect(self.on_send_button_clicked)
        layout.addWidget(self.send_button)
        
        self.message_edit = QLineEdit()
        self.message_edit.setPlaceholderText('Enter message here')
        layout.addWidget(self.message_edit)
        
        self.response_edit = QPlainTextEdit()
        self.response_edit.setReadOnly(True)
        layout.addWidget(self.response_edit)
        
        self.socket = QTcpSocket(self)
        
        self.server = QTcpServer(self)
        ok = self.server.listen(
            QHostAddress.SpecialAddress.LocalHost, 1234)
        self.server.newConnection.connect(self.on_new_connection)

    @Slot()
    def on_send_button_clicked(self):
        
        runnable = Runnable(self.message_edit.text())
        runnable.signals.connected.connect(lambda: self.response_edit.appendPlainText('Connected'))
        runnable.signals.sent.connect(self.on_sent)
        runnable.signals.received.connect(self.on_received)
        runnable.signals.disconnected.connect(lambda: self.response_edit.appendPlainText('Disconnected'))
        QThreadPool.globalInstance().start(runnable)
        
    @Slot()
    def on_sent(self, message):
        self.response_edit.appendPlainText(f'Sent: {message}')
        
    @Slot()
    def on_received(self, message):
        self.response_edit.appendPlainText(f'Received: {message}')

    @Slot()
    def on_new_connection(self):
        socket = self.server.nextPendingConnection()
        socket.readyRead.connect(lambda s=socket: self.handle_server_read(s))
        socket.disconnected.connect(socket.deleteLater)
        
    @Slot()
    def handle_server_read(self, socket):
        data = socket.readAll().data().decode()
        print(f'Server received: {data.strip()}')
        socket.write(f'Echo: {data}'.encode())
        socket.disconnectFromHost()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())

