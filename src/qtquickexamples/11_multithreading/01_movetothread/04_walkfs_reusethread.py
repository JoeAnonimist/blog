import os
import sys

from PySide6.QtCore import QObject, QThread, Signal, Slot, Property, QMutex, QMutexLocker
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, QmlElement


QML_IMPORT_NAME = 'examples.workerthread'
QML_IMPORT_MAJOR_VERSION = 1

class Worker(QObject):
    
    result_ready = Signal()
    progress = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.interruption_requested = False
        self.mutex = QMutex()
        
    @Slot()
    def do_work(self):
        
        self.interruption_requested = False
        
        path = os.path.abspath('.').split(os.path.sep)[0] + os.path.sep
        for root, _, _ in os.walk(path):
            with QMutexLocker(self.mutex):
                if self.interruption_requested:
                    self.progress.emit('Canceled')
                    self.result_ready.emit()
                    return
            self.progress.emit(os.path.basename(root))
        self.result_ready.emit()
        
    @Slot()
    def stop(self):
        with QMutexLocker(self.mutex):
            self.interruption_requested = True
        
    @Slot()
    def reset(self):
        with QMutexLocker(self.mutex):
            self.interruption_requested = False
        
        
@QmlElement
class Controller(QObject):
    
    operate = Signal()
    progress = Signal(str)
    result_ready = Signal()
    
    worker = None
    
    def __init__(self, parent=None):
        
        super().__init__(parent)
        QGuiApplication.instance().aboutToQuit.connect(self.cleanup)
    
        self.worker_thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.worker_thread)
        
        self.worker_thread.finished.connect(self.worker.deleteLater)
        self.operate.connect(self.worker.do_work)
        self.worker.result_ready.connect(self.result_ready)
        
        self.worker.progress.connect(self.progress)
        
        self.worker_thread.start()
    
    @Slot()
    def reset_worker(self):
        self.worker.reset()
        
    @Slot()
    def stop_worker(self):
        self.worker.stop()

    @Slot()
    def cleanup(self):
        print("Cleaning up...")
        try:
            self.worker_thread.requestInterruption()
            self.worker_thread.quit()
            self.worker_thread.wait()
        except Exception as e:
            print(e)


if __name__ == '__main__':

    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('04_walkfs_reusethread.qml')

    sys.exit(app.exec())