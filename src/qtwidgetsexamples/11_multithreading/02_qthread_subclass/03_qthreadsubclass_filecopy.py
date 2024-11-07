import os
import sys
from enum import Enum

from PySide6.QtCore import QThread, Slot, Signal, Qt
from PySide6.QtWidgets import (QApplication, QPushButton,
    QWidget, QVBoxLayout, QProgressBar)


class FileOperation(Enum):
    CREATE = 1
    COPY = 2


class WorkerThread(QThread):
    
    progress = Signal(int)
    work_done = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.operation = None
        print('Init in', QThread.currentThread().objectName())
    
    @Slot()
    def set_operation(self, operation):
        self.operation = operation

    @Slot()
    def create_large_file(self):
        
        filename = './large_file.txt'
        # 100 MB
        total_bytes = 100 * 1024 * 1024
        # 50 + newline
        line_length = 51
        num_lines = total_bytes // line_length
        step = num_lines // 10
        
        with open(filename, 'w') as file:
            line = 'a' * line_length + '\n'
            for i in range(num_lines):
                if QThread.currentThread().isInterruptionRequested():
                    file.close()
                    os.remove(filename)
                    return
                file.write(line)
                if i % step == 0:
                    self.progress.emit(i // step)
        self.work_done.emit()
        
    @Slot()
    def copy_large_file(self):
        
        source_path = './large_file.txt'
        destination_path = './destination.txt'
        chunk_size = os.path.getsize(source_path) // 10
        
        if os.path.exists(destination_path):
            os.remove(destination_path)

        with open(source_path, 'r') as source:
            with open(destination_path, 'w') as destination:
                
                step = 0
                while (chunk := source.read(chunk_size)):
                    if QThread.currentThread().isInterruptionRequested():
                        source.close()
                        destination.close()
                        #os.remove(destination_path)
                        return
                    destination.write(chunk)
                    step += 1
                    self.progress.emit(step)
        self.work_done.emit()

    def run(self):
        print('Running in: ', QThread.currentThread().objectName())
        print('event loop level: ', QThread.currentThread().loopLevel())
        if self.operation == FileOperation.CREATE:
            self.create_large_file()
        elif self.operation == FileOperation.COPY:
            self.copy_large_file()
        else:
            print('Shouldnt be here')


class Window(QWidget):
    
    file_operation = Signal(FileOperation)
    
    def __init__(self):

        super().__init__()
        
        QThread.currentThread().setObjectName('Main thread')
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.create_button = QPushButton('Create large file')
        self.create_button.clicked.connect(self.on_create_button_clicked)
        
        self.copy_button = QPushButton('Copy the file')
        self.copy_button.clicked.connect(self.on_copy_button_clicked)
        self.copy_button.setDisabled(True)
        
        self.cancel_button = QPushButton('Cancel')
        self.cancel_button.clicked.connect(self.on_cancel_button_clicked)
        self.cancel_button.setDisabled(True)
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(10)
        
        layout.addWidget(self.create_button)
        layout.addWidget(self.copy_button)
        layout.addWidget(self.cancel_button)
        layout.addWidget(self.progress_bar)
    
    @Slot()
    def on_create_button_clicked(self):
        print('Main thread loop level', QThread.currentThread().loopLevel())
        self.worker_thread = WorkerThread()
        self.worker_thread.setObjectName('Worker thread')

        self.worker_thread.started.connect(self.on_started)
        self.worker_thread.progress.connect(self.progress_bar.setValue)
        
        self.file_operation.connect(self.worker_thread.set_operation)
        self.file_operation.emit(FileOperation.CREATE)
        self.worker_thread.work_done.connect(self.on_work_done)
        
        self.create_button.setDisabled(True)
        self.copy_button.setDisabled(True)
        self.cancel_button.setEnabled(True)
        
        self.worker_thread.start()

    @Slot()
    def on_copy_button_clicked(self):
        print('Main thread loop level', QThread.currentThread().loopLevel())
        self.worker_thread = WorkerThread()
        self.worker_thread.setObjectName('Worker thread')

        self.worker_thread.started.connect(self.on_started)
        self.worker_thread.progress.connect(self.progress_bar.setValue)
        
        self.file_operation.connect(self.worker_thread.set_operation)
        self.file_operation.emit(FileOperation.COPY)
        self.worker_thread.work_done.connect(self.on_work_done)
        
        self.create_button.setDisabled(True)
        self.copy_button.setDisabled(True)
        self.cancel_button.setEnabled(True)
        
        self.worker_thread.start()
        
    @Slot()
    def on_cancel_button_clicked(self):
        
        if hasattr(self, 'worker_thread'):
            self.worker_thread.requestInterruption()
            self.worker_thread.wait()
            
        self.create_button.setEnabled(True)
        self.copy_button.setEnabled(True)
        self.cancel_button.setDisabled(True)
    
    @Slot()
    def on_started(self):
        print('thread started')
        
    @Slot()
    def on_work_done(self):
        print('Worker finished')
        self.create_button.setEnabled(True)
        self.copy_button.setEnabled(True)
        self.cancel_button.setDisabled(True)
        
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

