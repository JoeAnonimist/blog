import sys

from PySide6.QtCore import QObject, Slot
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
    engine.load('01_columnlayout.qml')
    
    root = engine.rootObjects()[0]
    
    button1 = root.findChild(QObject, 'button1') 
    button2 = root.findChild(QObject, 'button2')
    button3 = root.findChild(QObject, 'button3')
    
    logger = Logger()
    
    button1.clicked.connect(lambda: logger.log('Button 1 clicked'))
    button2.clicked.connect(lambda: logger.log('Button 2 clicked'))
    button3.clicked.connect(lambda: logger.log('Button 3 clicked'))

    result = app.exec()
    del engine
    
    sys.exit(result)