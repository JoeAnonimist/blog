import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from PySide6.QtCore import QObject, Slot


class Logger(QObject):
    
    @Slot(str)
    def log(self, message):
        print(message)



if __name__ == '__main__':

    app = QGuiApplication(sys.argv)
    
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('04_rootelement_findchild.qml')
    
    # 2. Use the engine to find the button
    
    root = engine.rootObjects()[0]
    button = root.findChild(QObject, 'button')
    
    # 3. Create a Logger() instance
    #    and connect buttons clicked signal 
    #    to the Logger.log slot
    
    logger = Logger()
    
    button.clicked.connect(
        lambda: logger.log('You clicked me!'))

    result = app.exec()
    del engine
    
    sys.exit(result)