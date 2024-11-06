import sys

from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, QmlElement

# 1. Set the global variables

QML_IMPORT_NAME = 'examples.logger'
QML_IMPORT_MAJOR_VERSION = 1

# 2. Decorate the class with @QmlElement
#     and subclass QObject

@QmlElement
class Logger(QObject):
    
    # 3. Any signal declared here
    #    is available to Qml.
    
    messageLogged = Signal()
    
    @Slot(str)
    def log(self, message):
        print(message)
        self.messageLogged.emit()


if __name__ == '__main__':

    app = QGuiApplication(sys.argv)
    
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('02_signal.qml')

    result = app.exec()
    del engine
    
    sys.exit(result)