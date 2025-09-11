from PySide6.QtCore import QThread, QMutex, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
import sys
import time

# Shared mutexes
mutex1 = QMutex()
mutex2 = QMutex()

class Thread1(QThread):
    def run(self):
        mutex1.lock()
        print("Thread1 locked mutex1")
        window.update_status("Thread1 locked mutex1")
        time.sleep(0.1)  # Simulate work
        mutex2.lock()
        print("Thread1 locked mutex2")
        window.update_status("Thread1 locked mutex2")
        mutex2.unlock()
        mutex1.unlock()

class Thread2(QThread):
    def run(self):
        mutex2.lock()
        print("Thread2 locked mutex2")
        window.update_status("Thread2 locked mutex2")
        time.sleep(0.1)  # Simulate work
        mutex1.lock()
        print("Thread2 locked mutex1")
        window.update_status("Thread2 locked mutex1")
        mutex1.unlock()
        mutex2.unlock()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Deadlock Demo")
        self.setGeometry(100, 100, 400, 200)

        # Layout and widgets
        layout = QVBoxLayout()
        self.status_label = QLabel("Click the button to start threads", self)
        self.status_label.setAlignment(Qt.AlignCenter)
        self.button = QPushButton("Start Threads", self)
        self.button.clicked.connect(self.start_threads)
        
        self.another_button = QPushButton('click me too')
        self.another_button.clicked.connect(self.on_another_btn_clicked)
        
        layout.addWidget(self.status_label)
        layout.addWidget(self.button)
        layout.addWidget(self.another_button)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Thread instances
        self.thread1 = None
        self.thread2 = None

    def update_status(self, text):
        self.status_label.setText(text)
        QApplication.processEvents()  # Ensure GUI updates

    def start_threads(self):
        self.button.setEnabled(False)  # Prevent multiple clicks
        self.status_label.setText("Starting threads...")
        
        # Create and start threads
        self.thread1 = Thread1()
        self.thread2 = Thread2()
        self.thread1.start()
        self.thread2.start()
        
    def on_another_btn_clicked(self):
        print('another button clicked')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())