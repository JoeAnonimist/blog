import sys

from PySide6.QtCore import (QObject, QRunnable, 
    QThreadPool, Slot, Signal, Qt)
from PySide6.QtWidgets import (QApplication,
    QPushButton, QLabel, QWidget, QVBoxLayout)


class Signals(QObject):
    progress = Signal(str)
    error = Signal(str)

# 1. Create a QRunnable subclass
#    and implement its run() method.

class Runnable(QRunnable):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.signals = Signals()
    
    # The run method will be executed
    # in the worker thread.
    
    def run(self):
        self.signals.progress.emit('Progress emitted')
        print('Hello World')
        self.signals.deleteLater()


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
    
    # When the button is clicked:
    
    @Slot()
    def on_button_clicked(self):
        
        # 2. Create a Runnable object
        
        runnable = Runnable()

        runnable.signals.progress.connect(self.label.setText)
        runnable.signals.error.connect(self.on_error)
        
        # 3. Access the QThreadPool global instance
        #    and run the task. 

        QThreadPool.globalInstance().start(runnable)
    
    @Slot()
    def on_error(self, message):
        print(message)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())

