import sys

from PySide6.QtCore import QObject, QTimer
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


if __name__ == '__main__':

    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)

    # 2. Create a timer and set the root object
    #    timer property value to it.

    timer = QTimer()
    timer.start(1000)

    # it appears that you need to set properties
    # before loading the Qml file.
    
    engine.setInitialProperties({'timer': timer})
    engine.load('02_setinitialproperties.qml')
    
    root = engine.rootObjects()[0]
    label = root.findChild(QObject, 'label')

    result = app.exec()
    del engine
    
    sys.exit(result)