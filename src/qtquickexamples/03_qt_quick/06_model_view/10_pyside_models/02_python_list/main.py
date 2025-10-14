import sys
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


if __name__ == '__main__':

    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()
    
    list_model = ['Item 1', 'Item 2', 'Item 3', 'Item 4']
    engine.setInitialProperties({'listModel': list_model})
    
    engine.load('Main.qml')

    sys.exit(app.exec())