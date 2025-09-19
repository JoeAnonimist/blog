import sys
from PySide6.QtCore import Slot
from PySide6.QtNetwork import QTcpSocket
from PySide6.QtWidgets import (QApplication, QWidget,
    QPushButton,  QVBoxLayout, QLineEdit, QPlainTextEdit)

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
        self.socket.connected.connect(self.send_message)
        self.socket.readyRead.connect(self.read_response)
        self.socket.errorOccurred.connect(self.handle_error)
        self.socket.disconnected.connect(self.on_disconnected)
    
    @Slot()
    def on_send_button_clicked(self):
        self.send_button.setDisabled(True)
        self.response_edit.appendPlainText('Connecting...')
        self.socket.connectToHost('tcpbin.com', 4242)
        
    @Slot()
    def send_message(self):
        # for some reason needs newline
        message = self.message_edit.text() + '\n'
        self.socket.write(message.encode())
        self.response_edit.appendPlainText(f'Sent: {message.strip()}')
        self.message_edit.clear()

    @Slot()
    def read_response(self):
        response = self.socket.readAll().data().decode()
        self.response_edit.appendPlainText(f'Received: {response.strip()}')
        self.socket.disconnectFromHost()
        
    @Slot(QTcpSocket.SocketError)
    def handle_error(self, error):
        self.socket.abort()
        self.response_edit.appendPlainText(f'Error: {self.socket.errorString()}')
        self.send_button.setEnabled(True)
        
    @Slot()
    def on_disconnected(self):
        self.response_edit.appendPlainText('Disconnected.')
        self.send_button.setEnabled(True)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())