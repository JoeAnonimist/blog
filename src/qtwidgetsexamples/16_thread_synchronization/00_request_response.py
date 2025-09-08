import sys
from PySide6.QtCore import QObject, QThread, Signal, Slot
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel


class Worker(QObject):
    sendValue = Signal(int)  # Signal to send value back

    def __init__(self):
        super().__init__()
        self._value = 123

    @Slot()
    def handleRequest(self):
        print("[Worker] Received value request")
        self.sendValue.emit(self._value)


class MainWindow(QWidget):
    requestValue = Signal()  # Signal to request the value from the worker

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Request Value Example")
        self.setMinimumSize(300, 100)

        # GUI elements
        self.label = QLabel("Click to get value", self)
        self.button = QPushButton("Request Value", self)
        self.button.clicked.connect(self.getValueFromWorker)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        # Thread and Worker
        self.thread = QThread(self)
        self.worker = Worker()
        self.worker.moveToThread(self.thread)

        # Connect signals
        self.requestValue.connect(self.worker.handleRequest)
        self.worker.sendValue.connect(self.receiveValue)

        # Start thread
        self.thread.start()

    def getValueFromWorker(self):
        print("[Main] Requesting value from worker...")
        self.requestValue.emit()

    @Slot(int)
    def receiveValue(self, value):
        print(f"[Main] Received value from worker: {value}")
        self.label.setText(f"Value from worker: {value}")

    def closeEvent(self, event):
        # Clean shutdown of thread
        self.thread.quit()
        self.thread.wait()
        super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
