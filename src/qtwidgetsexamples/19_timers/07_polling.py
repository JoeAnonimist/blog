import sys
import psutil
from PySide6.QtCore import QObject, QTimer, QThread, Signal, Slot
from PySide6.QtWidgets import (QApplication,
    QWidget, QPushButton, QProgressBar, QVBoxLayout)


class Worker(QObject):
    
    result_ready = Signal(int)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.interval = 500
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.poll)
        print(QThread.currentThread().objectName())
        
    @Slot(bool)
    def do_work(self, switch):
        print(QThread.currentThread().objectName())
        if switch and not self.timer.isActive():
            self.timer.start(self.interval)
        else:
            self.timer.stop()
        
        
    @Slot()
    def poll(self):
        self.result_ready.emit(int(psutil.cpu_percent(interval=None)))


class Window(QWidget):
    
    operate = Signal(bool)
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.start_button = QPushButton('Start timer')
        self.start_button.clicked.connect(self.on_start_button_clicked)
        layout.addWidget(self.start_button)
        
        self.stop_button = QPushButton('Stop timer')
        self.stop_button.clicked.connect(self.on_stop_button_clicked)
        self.stop_button.setEnabled(False)
        layout.addWidget(self.stop_button)
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        layout.addWidget(self.progress_bar)
        
        self.worker_thread = QThread()
        self.worker_thread.setObjectName('Worker thread')
        self.worker_obj = Worker()
        self.worker_obj.moveToThread(self.worker_thread)
        
        self.worker_thread.finished.connect(self.worker_obj.deleteLater)
        self.operate.connect(self.worker_obj.do_work)
        self.worker_obj.result_ready.connect(self.handle_results)
        
        self.worker_thread.start()
    
    @Slot()
    def on_start_button_clicked(self):
        self.start_button.setDisabled(True)
        self.stop_button.setEnabled(True)
        self.operate.emit(True)
        
    @Slot()
    def on_stop_button_clicked(self):
        self.start_button.setEnabled(True)
        self.stop_button.setDisabled(True)
        self.operate.emit(False)

    @Slot(int)
    def handle_results(self, value):
        self.progress_bar.setValue(value)
        
    def closeEvent(self, event):    
        self.operate.emit(False)    
        try:
            self.worker_thread.quit()
            self.worker_thread.wait()
        except Exception as e:
            print(e)
        super().closeEvent(event)
      

if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
