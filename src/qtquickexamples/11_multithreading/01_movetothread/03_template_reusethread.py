import sys

from PySide6.QtCore import QObject, QThread, Signal, Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, QmlElement


QML_IMPORT_NAME = 'examples.workerthread'
QML_IMPORT_MAJOR_VERSION = 1

class Worker(QObject):
    
    result_ready = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
    
    @Slot()
    def do_work(self, parameter):
        print(parameter)
        self.result_ready.emit(parameter)
        
        
@QmlElement
class Controller(QObject):
    
    operate = Signal(str)
    result_ready = Signal(str)
    
    def __init__(self, parent=None):
        
        super().__init__(parent)
        QGuiApplication.instance().aboutToQuit.connect(self.cleanup)
    
        self.worker_thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.worker_thread)
        
        self.worker_thread.finished.connect(self.worker.deleteLater)
        self.operate.connect(self.worker.do_work)
        self.worker.result_ready.connect(self.result_ready)
        
        self.worker_thread.start()
        
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
    engine.load('03_template_reusethread.qml')

    sys.exit(app.exec())