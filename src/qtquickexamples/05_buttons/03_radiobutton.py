import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


if __name__ == '__main__':

    app = QGuiApplication(sys.argv)
    
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('03_radiobutton.qml')
    
    result = app.exec()
    del engine
    
    sys.exit(result)