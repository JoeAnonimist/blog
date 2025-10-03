import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


if __name__ == '__main__':

    app = QGuiApplication(sys.argv)
    
    engine = QQmlApplicationEngine()
    engine.load('xml_list_model.qml')

    sys.exit(app.exec())