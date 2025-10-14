import sys
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from csvmodel import CsvModel


if __name__ == '__main__':

    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()
    
    csv_model = CsvModel('data.csv')
    engine.setInitialProperties({'csvModel': csv_model})
    
    engine.load('Main.qml')

    sys.exit(app.exec())