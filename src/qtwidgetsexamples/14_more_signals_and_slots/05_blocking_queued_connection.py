import sys

from PySide6.QtCore import (QObject, QThread,
    Slot, Signal, QEvent, Qt)
from PySide6.QtWidgets import (QApplication,
    QPushButton, QLabel, QWidget, QVBoxLayout)


class Worker(QObject):
    
    result_ready = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
    @Slot()
    def do_work(self, parameter):
        print(parameter)
        QThread.sleep(10)
        self.result_ready.emit(parameter)
        
    def event(self, event):
        if event.type() == QEvent.Type.MetaCall:
            print(f"Queued signal (MetaCallEvent) intercepted")
            print(event)
        return QObject.event(self, event)


class Controller(QWidget):
    
    operate = Signal(str)
    
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
        
        self.worker_thread = QThread()
        
        self.worker_obj = Worker()
        self.worker_obj.moveToThread(self.worker_thread)
        
        self.worker_thread.finished.connect(
            self.worker_obj.deleteLater)
        self.operate.connect(self.worker_obj.do_work,
            Qt.ConnectionType.BlockingQueuedConnection)
        self.worker_obj.result_ready.connect(self.handle_results)

        self.worker_thread.start()
    
    @Slot()
    def on_button_clicked(self):
        
        self.operate.emit('Hello World')
    
    @Slot()
    def handle_results(self):
        self.label.setText('Worker finished')
    
    def closeEvent(self, event):        
        try:
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
