# https://mayaposch.wordpress.com/2011/11/01/how-to-really-truly-use-qthreads-the-full-explanation/
# SImilar to the above article but with a QThread subclass

import sys

from PySide6.QtCore import (QObject, QThread,
    Slot, Signal, Qt)
from PySide6.QtWidgets import (QApplication,
    QPushButton, QLabel, QWidget, QVBoxLayout)


class WorkerThread(QThread):
    
    working = Signal()
    error = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
    def run(self):
        self.working.emit()
        print('Hello World')


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        button = QPushButton('Start background thread')
        button.clicked.connect(self.on_button_clicked)
        
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout.addWidget(button)
        layout.addWidget(self.label)
    
    @Slot()
    def on_button_clicked(self):
        
        self.worker_thread = WorkerThread()
        
        self.worker_thread.finished.connect(self.on_finished)
        
        self.worker_thread.error.connect(self.on_error)
        self.worker_thread.started.connect(self.on_started)
        self.worker_thread.working.connect(self.on_working)
        
        self.worker_thread.start()
    
    @Slot()
    def on_started(self):
        print('thread started')
        
    @Slot()
    def on_working(self):
        print('working')
    
    @Slot()
    def on_finished(self):
        self.label.setText('Worker finished')
    
    @Slot()
    def on_error(self, message):
        print(message)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()

    sys.exit(app.exec())

