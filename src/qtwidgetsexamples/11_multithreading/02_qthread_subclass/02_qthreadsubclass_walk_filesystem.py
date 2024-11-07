import os
import sys

from PySide6.QtCore import QThread, Slot, Signal, Qt
from PySide6.QtWidgets import (QApplication, QPushButton,
    QLabel, QWidget, QVBoxLayout)


class WorkerThread(QThread):
    
    progress = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
    def run(self):
        print('Running in: ', QThread.currentThread().objectName())
        print('event loop level: ', QThread.currentThread().loopLevel())
        path = os.path.abspath('.').split(os.path.sep)[0] + os.path.sep
        for root, _, _ in os.walk(path):
            if QThread.currentThread().isInterruptionRequested():
                print('Interrupt')
                return
            self.progress.emit(os.path.basename(root))


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.start_button = QPushButton('Start background thread')
        self.start_button.clicked.connect(self.on_start_button_clicked)
        
        self.cancel_button = QPushButton('Cancel')
        self.cancel_button.clicked.connect(self.on_cancel_button_clicked)
        self.cancel_button.setDisabled(True)
        
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout.addWidget(self.start_button)
        layout.addWidget(self.cancel_button)
        layout.addWidget(self.label)
    
    @Slot()
    def on_start_button_clicked(self):
        print('Main thread loop level', QThread.currentThread().loopLevel())
        self.worker_thread = WorkerThread()
        self.worker_thread.setObjectName('Worker thread')

        self.worker_thread.started.connect(self.on_started)
        self.worker_thread.progress.connect(self.on_progress)
        
        self.start_button.setDisabled(True)
        self.cancel_button.setEnabled(True)
        
        self.worker_thread.start()
        
    @Slot()
    def on_cancel_button_clicked(self):
        print('cancel')
        self.start_button.setEnabled(True)
        self.cancel_button.setDisabled(True)
        
        if hasattr(self, 'worker_thread'):
            self.worker_thread.requestInterruption()
            self.worker_thread.wait()
    
    @Slot()
    def on_started(self):
        print('thread started')
        
    @Slot()
    def on_progress(self, msg):
        self.label.setText(msg)
        
    # Make sure the thread is destroyed
    # when the main window is closed.
    
    def closeEvent(self, event):        
        try:
            self.worker_thread.requestInterruption()
            self.worker_thread.wait()
        except Exception as e:
            print(e) 


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()

    sys.exit(app.exec())

