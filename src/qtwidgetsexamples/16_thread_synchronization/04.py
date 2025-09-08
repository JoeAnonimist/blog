import sys
from PySide6.QtCore import QObject, QThread, Signal, Slot
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel


class Worker(QObject):
    
    sendValue = Signal(int)

    def __init__(self):
        super().__init__()
        self.value = 0

    @Slot()
    def handleRequest(self):
        print('[Worker] Received value request')
        self.sendValue.emit(self.value)
        
    @Slot(int)
    def updateValue(self, value):
        print('[Worker] Received update request: ', value)
        self.value = value
        
    def do_something(self):
        QThread.sleep(0)
        
class Updater(QObject):
    
    finished = Signal()

    def __init__(self, worker, parent=None):
        super().__init__(parent)
        self.worker = worker
    
    def update(self):
        local_val = self.worker.value
        local_val += 1000
        print('updating')
        self.worker.do_something()
        self.worker.value = local_val
        self.finished.emit()


class MainWindow(QWidget):

    requestValue = Signal()
    requestUpdate = Signal(int)

    def __init__(self):
        
        super().__init__()

        self.thread_count = 5
        self.amount = 1000
        self.updaters = []

        self.label = QLabel('Click to get value', self)
        
        self.request_button = QPushButton('Request Value', self)
        self.request_button.clicked.connect(self.getValueFromWorker)
        
        self.update_button = QPushButton('Update value', self)
        self.update_button.clicked.connect(self.on_update_clicked)
        
        self.race_button = QPushButton('Test race condition', self)
        self.race_button.clicked.connect(self.startRace)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.request_button)
        layout.addWidget(self.update_button)
        layout.addWidget(self.race_button)

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
        value = 0
        self.requestUpdate.emit(value)
        self.label.setText('Click to get value')
        
    @Slot()
    def startRace(self):
        
        self.updaters.clear()

        for i in range(self.thread_count):
            background_thread = QThread(self)
            background_thread.setObjectName(f'Thread {i}')

            updater = Updater(self.worker)
            self.updaters.append(updater)
            updater.moveToThread(background_thread)
    
            background_thread.started.connect(updater.update)
            updater.finished.connect(background_thread.quit)
            updater.finished.connect(updater.deleteLater)
            background_thread.finished.connect(background_thread.deleteLater)
            
            background_thread.start()
        

    def closeEvent(self, event):

        self.thread.quit()
        self.thread.wait()
        super().closeEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
