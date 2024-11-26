# https://doc.qt.io/qt-6/qthread.html

import sys

from PySide6.QtCore import (QObject, QThread,
    Slot, Signal, Qt)
from PySide6.QtWidgets import (QApplication,
    QPushButton, QLabel, QWidget, QVBoxLayout)


# 1. Create the worker class

class Worker(QObject):
    
    result_ready = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
    @Slot()
    def do_work(self, parameter):
        print(parameter)
        self.result_ready.emit(parameter)


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
        
        # 2. Create the thread object
        
        self.worker_thread = QThread()
        
        # 3. Create the worker and move it to the thread
        
        self.worker = Worker()
        self.worker.moveToThread(self.worker_thread)
        
        # 4. Connect the signals and the slots
        
        self.worker_thread.finished.connect(
            self.worker.deleteLater)
        self.operate.connect(self.worker.do_work)
        self.worker.result_ready.connect(self.handle_results)
        
        # 5. Start the thread

        self.worker_thread.start()
    
    # 6. On the button click emit the operate signal
    
    @Slot()
    def on_button_clicked(self):
        
        self.operate.emit('Hello World')
    
    @Slot()
    def handle_results(self):
        self.label.setText('Worker finished')
    
    # 7. Quit the thread when the main window is closed
    
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
