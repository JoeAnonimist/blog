import os
import sys

from PySide6.QtCore import QThread, Signal, Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, QmlElement


QML_IMPORT_NAME = 'examples.qthreadsubclass'
QML_IMPORT_MAJOR_VERSION = 1

@QmlElement
class WorkerThread(QThread):
    
    progress = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        print('Init it', QThread.currentThread().objectName())
        
    def run(self):
        
        print('Running in: ',
            QThread.currentThread().objectName())
        print('event loop level: ',
            QThread.currentThread().loopLevel())

        path = os.path.abspath('.').split(os.path.sep)[0] + os.path.sep
        for root, _, _ in os.walk(path):
            if QThread.currentThread().isInterruptionRequested():
                return
            self.progress.emit(os.path.basename(root))
            
    @Slot()
    def cleanup(self):
        super().deleteLater()
        
    @Slot()
    def safelyRequestInterruption(self):
        self.requestInterruption()
        self.wait()
        print(self.objectName())


if __name__ == '__main__':

    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('02_walk_filesystem.qml')

    sys.exit(app.exec())