import os
import sys

from PySide6.QtCore import QObject, QThread, Signal, Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, QmlElement


QML_IMPORT_NAME = 'examples.workerthread'
QML_IMPORT_MAJOR_VERSION = 1

class Worker(QObject):
    
    finished = Signal()
    progress = Signal(str)
    error = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
    
    @Slot()
    def process(self):
        path = os.path.abspath('.').split(os.path.sep)[0] + os.path.sep
        for root, _, _ in os.walk(path):
            if QThread.currentThread().isInterruptionRequested():
                return
            self.progress.emit(os.path.basename(root))
        self.finished.emit()


@QmlElement
class Controller(QObject):
    
    finished = Signal()
    progress = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        QGuiApplication.instance().aboutToQuit.connect(self.cleanup)
    
    @Slot()
    def start_working(self):
        
        self.background_thread = QThread()
        self.worker_obj = Worker()
        self.worker_obj.moveToThread(self.background_thread)
        
        self.worker_obj.finished.connect(self.finished)
        self.worker_obj.error.connect(self.on_error)
        
        self.background_thread.started.connect(self.worker_obj.process)
        self.worker_obj.finished.connect(self.background_thread.quit)
        self.worker_obj.finished.connect(self.worker_obj.deleteLater)
        self.background_thread.finished.connect(self.background_thread.deleteLater)
        
        self.worker_obj.progress.connect(self.progress)
        
        self.background_thread.start()
        
    @Slot()
    def stop_working(self):
        
        if hasattr(self, 'background_thread'):
            self.background_thread.requestInterruption()
            self.background_thread.quit()
            self.background_thread.wait()
        
    @Slot()
    def on_error(self, message):
        print(message)
        
    @Slot()
    def cleanup(self):
        print("Cleaning up...")
        try:
            self.background_thread.requestInterruption()
            self.background_thread.quit()
            self.background_thread.wait()
        except Exception as e:
            print(e) 


if __name__ == '__main__':

    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('02_walk_filesystem.qml')

    sys.exit(app.exec())