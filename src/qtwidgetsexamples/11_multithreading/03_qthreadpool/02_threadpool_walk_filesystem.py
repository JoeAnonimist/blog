import os
import sys

from PySide6.QtCore import (QObject, QRunnable, QThread,
    QThreadPool, Slot, Signal, Qt)
from PySide6.QtWidgets import (QApplication,
    QPushButton, QLabel, QWidget, QVBoxLayout)


class Signals(QObject):
    progress = Signal(str)
    error = Signal(str)

class Runnable(QRunnable):
    
    signals = Signals()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.do_work = True
        QThread.currentThread().setObjectName('Worker thread')
        
    def run(self):
        path = os.path.abspath('.').split(os.path.sep)[0] + os.path.sep
        for root, _, _ in os.walk(path):
            if not self.do_work:
                return
            self.signals.progress.emit(os.path.basename(root))
            
    def on_cancel_emitted(self):
        print(QThread.currentThread().objectName())
        print(QThread.currentThread().loopLevel())
        self.do_work = False


class Window(QWidget):
    
    cancel_runnable = Signal()
    
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
        
        runnable = Runnable()
        runnable.signals.progress.connect(self.label.setText)
        runnable.signals.error.connect(self.on_error)
        self.cancel_runnable.connect(runnable.on_cancel_emitted)
        QThreadPool.globalInstance().start(runnable)
        
        self.start_button.setDisabled(True)
        self.cancel_button.setEnabled(True)
        
    @Slot()
    def on_cancel_button_clicked(self):
        QApplication.instance().beep()
        print('in cancel button click')
        self.cancel_runnable.emit()
        self.start_button.setEnabled(True)
        self.cancel_button.setDisabled(True)
        
    
    @Slot()
    def on_error(self, message):
        print(message)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
