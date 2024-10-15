import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, QmlElement

from PySide6.QtCore import QObject, Slot


# 1. Create a class that can be imported into Qml

QML_IMPORT_NAME = 'examples.logger'
QML_IMPORT_MAJOR_VERSION = 1


@QmlElement
class Logger(QObject):
    
    @Slot(str)
    def log(self, message):
        print(message)


if __name__ == '__main__':

    app = QGuiApplication(sys.argv)
    
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('03_qmlelement.qml')

    result = app.exec()
    del engine
    
    sys.exit(result)