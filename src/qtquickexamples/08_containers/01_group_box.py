import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


if __name__ == '__main__':

    app = QGuiApplication(sys.argv)
    
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    
    engine.load('01_group_box.qml')
    # engine.load('01_group_box_stacklayout.qml')
    
    sys.exit(app.exec())