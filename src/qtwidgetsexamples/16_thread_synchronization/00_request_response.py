import sys
from random import randint
from PySide6.QtCore import QObject, QThread, Signal, Slot
from PySide6.QtWidgets import (QApplication, QWidget,
    QVBoxLayout, QPushButton, QLabel)


class Worker(QObject):
    
    sendValue = Signal(int)

    def __init__(self):
        super().__init__()
        self.value = 123

    @Slot()
    def handleRequest(self):
        print('[Worker] Received value request')
        self.sendValue.emit(self.value)
        
    @Slot(int)
    def updateValue(self, value):
        print('[Worker] Received update request: ', value)
        self.value = value


class MainWindow(QWidget):

    requestValue = Signal()
    requestUpdate = Signal(int)

    def __init__(self):
        
        super().__init__()

        self.setMinimumSize(300, 100)

        self.label = QLabel('Click to get value', self)
        
        self.request_button = QPushButton('Request Value', self)
        self.request_button.clicked.connect(self.getValueFromWorker)
        
        self.update_button = QPushButton('Update value', self)
        self.update_button.clicked.connect(self.on_update_clicked)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.request_button)
        layout.addWidget(self.update_button)

        self.thread = QThread(self)
        self.worker = Worker()
        self.worker.moveToThread(self.thread)

        self.requestValue.connect(self.worker.handleRequest)
        self.worker.sendValue.connect(self.receiveValue)
        self.requestUpdate.connect(self.worker.updateValue)

        self.thread.start()

    def getValueFromWorker(self):
        print('[Main] Requesting value from worker...')
        self.requestValue.emit()

    @Slot(int)
    def receiveValue(self, value):
        print(f'[Main] Received value from worker: {value}')
        self.label.setText(f'Value from worker: {value}')
        
    @Slot()
    def on_update_clicked(self):
        value = randint(0, 200)
        self.requestUpdate.emit(value)
        self.label.setText('Click to get value')

    def closeEvent(self, event):

        self.thread.quit()
        self.thread.wait()
        super().closeEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
