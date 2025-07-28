import os
import sys

from PySide6.QtCore import QObject, QRunnable, Signal, Slot, QThreadPool, QThread
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


class Signals(QObject):
    progress = Signal(str)
    error = Signal(str)


class Runnable(QRunnable):
    
    def __init__(self):
        super().__init__()
        self.signals = Signals()
        self.do_work = True
    
    def run(self):
        path = os.path.abspath('.').split(os.path.sep)[0] + os.path.sep
        for root, _, _ in os.walk(path):
            if not self.do_work:
                return
            self.signals.progress.emit(os.path.basename(root))
    
    @Slot()
    def on_cancel_emitted(self):
        self.do_work = False


class Controller(QObject):
    
    progress = Signal(str)
    error = Signal(str)
    cancel_runnable = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        
    @Slot()
    def run_task(self):
        
        runnable = Runnable()

        runnable.signals.progress.connect(self.progress)
        runnable.signals.error.connect(self.on_error)
        self.cancel_runnable.connect(runnable.on_cancel_emitted)

        QThreadPool.globalInstance().start(runnable)
        
    @Slot()
    def on_error(self, message):
        print(message)


if __name__ == '__main__':

    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    
    controller = Controller()
    engine.setInitialProperties({'controller': controller})
    
    engine.load('02_walk_filesystem.qml')

    sys.exit(app.exec())