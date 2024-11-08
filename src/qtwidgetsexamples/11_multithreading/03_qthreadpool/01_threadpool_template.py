# DeadPool

import sys

from PySide6.QtCore import (QObject, QRunnable, 
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
        
    def run(self):
        self.signals.progress.emit('Progress emitted')
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
        runnable = Runnable()
        runnable.signals.progress.connect(self.label.setText)
        runnable.signals.error.connect(self.on_error)
        QThreadPool.globalInstance().start(runnable)
    
    @Slot()
    def on_error(self, message):
        print(message)


if __name__ == '__main__':

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())

