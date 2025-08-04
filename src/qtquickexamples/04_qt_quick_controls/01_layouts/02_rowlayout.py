import sys

from PySide6.QtCore import QObject, QTimer, Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


class Logger(QObject):
    
    @Slot(str)
    def log(self, message):
        print(message)


if __name__ == '__main__':

    app = QGuiApplication(sys.argv)
    
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    
    timer = QTimer()
    timer.setInterval(1000)
    
    engine.setInitialProperties({'timer': timer})
    
    engine.load('02_rowlayout.qml')
    
    result = app.exec()
    del engine
    
    sys.exit(result)