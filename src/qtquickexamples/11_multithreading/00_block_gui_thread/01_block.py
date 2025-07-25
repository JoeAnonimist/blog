import os
import sys

from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, QmlElement


QML_IMPORT_NAME = 'examples.longRunningTask'
QML_IMPORT_MAJOR_VERSION = 1

@QmlElement
class Task(QObject):
    
    progress = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
    
    @Slot()
    def do_work(self):
        path = os.path.abspath('.').split(os.path.sep)[0] + os.path.sep
        name = 'bogus'
        for root, _, files in os.walk(path):
            self.progress.emit(root)
            if name in files:
                print(os.path.join(root, name))


if __name__ == '__main__':

    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('01_block.qml')

    sys.exit(app.exec())