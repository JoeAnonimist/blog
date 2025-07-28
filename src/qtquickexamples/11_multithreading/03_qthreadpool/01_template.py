import sys

from PySide6.QtCore import QObject, QRunnable, Signal, Slot, QThreadPool
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


class Signals(QObject):
    progress = Signal(str)
    error = Signal(str)


class Runnable(QRunnable):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.signals = Signals()

    def run(self):
        self.signals.progress.emit('Progress emitted')
        print('Hello World')
        self.signals.deleteLater()


class Controller(QObject):
    
    progress = Signal(str)
    error = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        
    @Slot()
    def run_task(self):
        
        runnable = Runnable()

        runnable.signals.progress.connect(self.progress)
        runnable.signals.error.connect(self.on_error)

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
    
    engine.load('01_template.qml')

    sys.exit(app.exec())