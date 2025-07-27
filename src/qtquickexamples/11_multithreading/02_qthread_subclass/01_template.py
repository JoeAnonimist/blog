import sys

from PySide6.QtCore import QObject, QThread, Signal, Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, QmlElement


QML_IMPORT_NAME = 'examples.qthreadsubclass'
QML_IMPORT_MAJOR_VERSION = 1

@QmlElement
class WorkerThread(QThread):
    
    result_ready = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        print('Init in', QThread.currentThread().objectName(),
            ', Loop level', QThread.currentThread().loopLevel())
        
    def run(self):
        
        print('Running in', QThread.currentThread().objectName(),
            ', Loop level', QThread.currentThread().loopLevel())

        result = 'Hello World'
        print(result)
        self.result_ready.emit(result)
        
    @Slot()
    def d(self):
        super().deleteLater()


if __name__ == '__main__':

    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('01_template.qml')

    sys.exit(app.exec())