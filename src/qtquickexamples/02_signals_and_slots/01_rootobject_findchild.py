import sys

from PySide6.QtCore import QObject, QTimer
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


if __name__ == '__main__':

    app = QGuiApplication(sys.argv)
    
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('01_rootobjects_findchild.qml')
    
    # 2. Find the Label element
    
    root = engine.rootObjects()[0]
    label = root.findChild(QObject, 'label')
    
    # 3. Create a timer and connect
    #    the timer signal to the label slot
    
    timer = QTimer()
    timer.timeout.connect(label.updateText)
    timer.start(1000)

    result = app.exec()
    del engine
    
    sys.exit(result)