import sys

from PySide6.QtGui import QGuiApplication, QFontDatabase
from PySide6.QtQml import QQmlApplicationEngine


if __name__ == '__main__':

    app = QGuiApplication(sys.argv)
    
    for family in QFontDatabase.families():
        print(family)
    
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    
    engine.load('show_text.qml')

    sys.exit(app.exec())