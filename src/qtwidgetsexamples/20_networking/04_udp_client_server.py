import sys
from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtNetwork import QUdpSocket, QHostAddress
from PySide6.QtWidgets import (QApplication, QWidget,
    QPushButton,  QVBoxLayout, QLineEdit, QPlainTextEdit)


class UdpEndpoint(QObject):

    messageReceived = Signal(str)
    
    def __init__(self, bind_port=7755, dest_port=7755, parent=None):
        
        super().__init__(parent)
        
        self.dest_port = dest_port
        self.client = QUdpSocket(self)
        
        self.server = QUdpSocket(self)
        self.server.bind(QHostAddress.SpecialAddress.LocalHost, bind_port)
        self.server.readyRead.connect(self.read_datagrams)
    
    @Slot()
    def send_message(self, message):
        datagram = message.encode()
        self.client.writeDatagram(datagram,
            QHostAddress.SpecialAddress.LocalHost, self.dest_port)
    
    @Slot()
    def read_datagrams(self):
        while self.server.hasPendingDatagrams():
            datagram = self.server.receiveDatagram()
            message = bytes(datagram.data()).decode()
            self.messageReceived.emit(message)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.send_button = QPushButton('Send message')
        self.send_button.clicked.connect(self.write_datagram)
        layout.addWidget(self.send_button)
        
        self.message_edit = QLineEdit()
        self.message_edit.setPlaceholderText('Enter message here')
        layout.addWidget(self.message_edit)
        
        self.response_edit = QPlainTextEdit()
        self.response_edit.setReadOnly(True)
        layout.addWidget(self.response_edit)
        
        self.datagram_sender = UdpEndpoint(bind_port=7756, dest_port=7755)
        
        self.datagram_receiver = UdpEndpoint(bind_port=7755, dest_port=7756)
        self.datagram_receiver.messageReceived.connect(
            self.update_message_edit)
    
    @Slot()
    def write_datagram(self):
        message = self.message_edit.text()
        self.datagram_sender.send_message(message)
        self.response_edit.appendPlainText(f'Sent: {message}')
        
    @Slot()
    def update_message_edit(self, message):
        self.response_edit.appendPlainText(f'Received: {message}')


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())