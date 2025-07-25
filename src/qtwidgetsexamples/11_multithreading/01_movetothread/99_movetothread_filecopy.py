import os
import sys

from PySide6.QtCore import (QObject, QThread,
    Slot, Signal)
from PySide6.QtWidgets import (QApplication,
    QPushButton, QProgressBar, QWidget, QVBoxLayout)


class Worker(QObject):
    
    finished = Signal()
    progress = Signal(int)
    
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
        self.finished.emit()
        
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
                        try:
                            os.remove(destination_path)
                        except Exception as e:
                            print(e)
                        return
                    destination.write(chunk)
                    step += 1
                    self.progress.emit(step)
        self.finished.emit()


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.create_button = QPushButton('Create file')
        self.create_button.setObjectName('create')
        self.create_button.clicked.connect(self.on_create_button_clicked)
        
        self.copy_button = QPushButton('Copy file')
        self.copy_button.setObjectName('copy')
        self.copy_button.setDisabled(True)
        self.copy_button.clicked.connect(self.on_create_button_clicked)
        
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
        
        self.progress_bar.setValue(0)
        self.cancel_button.setEnabled(True)
        
        self.background_thread = QThread()
        self.worker_obj = Worker()
        self.worker_obj.moveToThread(self.background_thread)
        
        self.worker_obj.finished.connect(self.on_finished)
        
        if self.sender().objectName() == 'create':
            self.create_button.setDisabled(True)
            self.copy_button.setDisabled(True)
            self.background_thread.started.connect(self.worker_obj.create_large_file)
        else:
            self.create_button.setDisabled(True)
            self.copy_button.setDisabled(True)
            self.background_thread.started.connect(self.worker_obj.copy_large_file)
            
        self.worker_obj.finished.connect(self.background_thread.quit)
        self.worker_obj.finished.connect(self.worker_obj.deleteLater)
        self.background_thread.finished.connect(self.background_thread.deleteLater)
        
        self.worker_obj.progress.connect(self.progress_bar.setValue)
        
        self.background_thread.start()
        
    @Slot()
    def on_cancel_button_clicked(self):
        
        self.create_button.setEnabled(True)
        self.copy_button.setEnabled(True)
        self.cancel_button.setDisabled(True)
        
        if hasattr(self, 'background_thread'):
            if self.background_thread.isRunning():
                self.background_thread.requestInterruption()
                self.background_thread.quit()
                self.background_thread.wait()
    
    @Slot()
    def on_finished(self):
        print('Worker finished')
        self.create_button.setEnabled(True)
        self.copy_button.setEnabled(True)
        self.cancel_button.setDisabled(True)
    
    @Slot()
    def on_error(self, message):
        print(message)
        
    def closeEvent(self, event):        
        try:
            self.background_thread.requestInterruption()
            self.background_thread.quit()
            self.background_thread.wait()
        except Exception as e:
            print(e) 


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())