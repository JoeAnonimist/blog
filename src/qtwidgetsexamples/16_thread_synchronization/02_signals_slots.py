from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import QObject, QThread, Signal, Slot
import sys

# --- Counter Object ---
class CounterObject(QObject):
    def __init__(self):
        super().__init__()
        self.counter = 0

    @Slot()
    def increment(self):
        self.counter += 1  # NOT atomic!


# --- Worker Thread ---
class Worker(QThread):
    finished = Signal()

    def __init__(self, counter_object: CounterObject):
        super().__init__()
        self.counter_object = counter_object

    def run(self):
        for _ in range(100_000):
            self.counter_object.increment()
        self.finished.emit()


# --- Main GUI ---
class RaceConditionDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Race Condition Demo (Encapsulated Counter in QThread)")
        self.resize(400, 100)

        self.label = QLabel("Click to start", self)
        self.button = QPushButton("Start Threads", self)
        self.button.clicked.connect(self.start_threads)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.threads = []

    def start_threads(self):
        self.label.setText("Running...")
        self.button.setEnabled(False)

        # Create counter object and move to its own thread
        self.counter_object = CounterObject()
        self.counter_thread = QThread()
        self.counter_object.moveToThread(self.counter_thread)
        self.counter_thread.start()

        # Start two workers that increment the counter
        self.completed = 0
        self.threads.clear()

        for _ in range(2):
            worker = Worker(self.counter_object)
            worker.finished.connect(self.on_worker_done)
            self.threads.append(worker)
            worker.start()

    def on_worker_done(self):
        self.completed += 1
        if self.completed == 2:
            # All done: read final counter value
            final = self.counter_object.counter
            self.label.setText(f"Final counter: {final}")
            self.button.setEnabled(True)

            # Clean up the counter thread
            self.counter_thread.quit()
            self.counter_thread.wait()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = RaceConditionDemo()
    win.show()
    sys.exit(app.exec())

