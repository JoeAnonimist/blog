import sys
import time
from PySide6.QtCore import QTimer, Slot, QTime, QElapsedTimer, QThread, Signal
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QVBoxLayout, QPlainTextEdit
)

# Adjustable interval (experiment with this)
TIME_INTERVAL_MS = 500   # ms


class Worker(QThread):
    """Simulates heavy load in a separate thread."""
    finished = Signal(int)  # emit worker ID when done

    def __init__(self, worker_id: int):
        super().__init__()
        self.worker_id = worker_id

    def run(self):
        # Simulate heavy calculation (~750ms)
        start = time.time()
        while time.time() - start < 0.75:
            pass
        self.finished.emit(self.worker_id)


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Set up layout
        layout = QVBoxLayout(self)
        self.setLayout(layout)

        # Time display label
        self.time_label = QLabel(f"Time: {QTime.currentTime().toString('hh:mm:ss:zzz')}")
        layout.addWidget(self.time_label)

        # Log text area (PlainTextEdit is faster than QTextEdit for logging)
        self.log_text = QPlainTextEdit()
        self.log_text.setReadOnly(True)
        layout.addWidget(self.log_text)

        # Start button
        self.start_button = QPushButton("Start Timers")
        self.start_button.clicked.connect(self.on_start_clicked)
        layout.addWidget(self.start_button)

        # Stop button
        self.stop_button = QPushButton("Stop Timers")
        self.stop_button.clicked.connect(self.on_stop_clicked)
        layout.addWidget(self.stop_button)

        # Time update timer
        self.time_timer = QTimer()
        self.time_timer.setInterval(TIME_INTERVAL_MS)
        self.time_timer.timeout.connect(self.on_time_timeout)

        # Load check timer
        self.load_timer = QTimer()
        self.load_timer.setInterval(10000)
        self.load_timer.timeout.connect(self.on_load_timeout)

        # Track last log time
        self.last_log_time = QElapsedTimer()
        self.last_log_time.start()
        self.prev_log_elapsed = 0

        # Keep worker references
        self.workers = []
        self.worker_counter = 0

    @Slot()
    def on_start_clicked(self):
        self.start_button.setDisabled(True)
        self.time_timer.start()
        self.load_timer.start()
        self.log(f"Started timers at {QTime.currentTime().toString('hh:mm:ss:zzz')}")
        self.last_log_time.restart()

    @Slot()
    def on_stop_clicked(self):
        self.time_timer.stop()
        self.load_timer.stop()
        self.start_button.setDisabled(False)
        self.log("Timers stopped")

    @Slot()
    def on_time_timeout(self):
        current_time = QTime.currentTime().toString("hh:mm:ss:zzz")
        self.time_label.setText(f"Time: {current_time}")

        # Log only if enough time has passed
        if self.last_log_time.elapsed() >= TIME_INTERVAL_MS:
            elapsed = self.last_log_time.elapsed()
            self.log(f"Time updated at {current_time} (+{elapsed}ms)")
            self.prev_log_elapsed = elapsed
            self.last_log_time.restart()

    @Slot()
    def on_load_timeout(self):
        """Simulate a heavy operation (two versions)."""
        self.log(f"*** Load check at {QTime.currentTime().toString('hh:mm:ss:zzz')}")

        # Version 1: non-blocking (singleShot)
        QTimer.singleShot(750, lambda: self.log("Load check finished (singleShot)"))

        # Version 2: simulated blocking in a worker thread
        self.worker_counter += 1
        worker = Worker(self.worker_counter)
        worker.finished.connect(self.on_worker_finished)
        self.workers.append(worker)
        worker.start()

        self.last_log_time.restart()

    @Slot(int)
    def on_worker_finished(self, worker_id: int):
        self.log(f"Load check finished (thread #{worker_id})")
        # Clean up finished worker
        for worker in self.workers[:]:
            if worker.worker_id == worker_id:
                self.workers.remove(worker)
                worker.deleteLater()
                break

    def log(self, text: str):
        """Append text to log, trimming old entries."""
        self.log_text.appendPlainText(text)
        if self.log_text.blockCount() > 500:
            self.log_text.clear()
            self.log_text.appendPlainText("---- log trimmed ----")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
