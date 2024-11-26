# https://doc.qt.io/qt-6/qthread.html

import os
import sys

from PySide6.QtCore import (QObject, QThread,
    Slot, Signal, QMutex, QMutexLocker, Qt)
from PySide6.QtWidgets import (QApplication,
    QPushButton, QLabel, QWidget, QVBoxLayout)


# 1. Create the worker class

class Worker(QObject):
    
    result_ready = Signal()
    progress = Signal(str)
    stop_signal = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.interruption_requested = False
        self.mutex = QMutex()
        
    @Slot()
    def do_work(self):
        
        self.interruption_requested = False
        
        path = os.path.abspath('.').split(os.path.sep)[0] + os.path.sep
        for root, _, _ in os.walk(path):
            with QMutexLocker(self.mutex):
                if self.interruption_requested:
                    self.progress.emit('Canceled')
                    self.result_ready.emit()
                    return
            self.progress.emit(os.path.basename(root))
        self.result_ready.emit()
        
    @Slot()
    def stop(self):
        with QMutexLocker(self.mutex):
            self.interruption_requested = True
        
    @Slot()
    def reset(self):
        with QMutexLocker(self.mutex):
            self.interruption_requested = False


class Controller(QWidget):
    
    operate = Signal()
    
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
        
        # 2. Create the thread
        
        self.worker_thread = QThread()
        
        # 3. Create the worker and move it to the thread
        
        self.worker = Worker()
        self.worker.moveToThread(self.worker_thread)
        
        # 4. Connect the signals with the slots
        
        self.worker_thread.finished.connect(self.worker.deleteLater)
        self.operate.connect(self.worker.do_work)
        self.worker.result_ready.connect(self.handle_results)
        
        self.worker.progress.connect(self.label.setText)
        
        # 5. Start the thread

        self.worker_thread.start()
    
    # 6. On the start button click emit the operate signal
    
    @Slot()
    def on_start_button_clicked(self):
        
        self.start_button.setDisabled(True)
        self.cancel_button.setEnabled(True)
        
        self.worker.reset()
        self.operate.emit()
    
    # 7. On the cancel button click stop the worker
    
    @Slot()
    def on_cancel_button_clicked(self):
        
        self.start_button.setEnabled(True)
        self.cancel_button.setDisabled(True)
        self.worker.stop()

    @Slot()
    def handle_results(self):
        self.label.setText('Worker finished')
    
    # 8. Quit the thread when the main window is closed
    
    def closeEvent(self, event):        
        try:
            self.worker.stop()
            self.worker_thread.quit()
            self.worker_thread.wait()
        except Exception as e:
            print(e) 
        event.accept()


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Controller()
    main_window.show()

    sys.exit(app.exec())

