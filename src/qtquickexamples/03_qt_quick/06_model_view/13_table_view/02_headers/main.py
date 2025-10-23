import sys
from PySide6.QtGui import QGuiApplication, QStandardItemModel, QStandardItem
from PySide6.QtQml import QQmlApplicationEngine

if __name__ == '__main__':

    app = QGuiApplication(sys.argv)

    model = QStandardItemModel(3, 2)
    model.setHorizontalHeaderLabels(["Col1", "Col2"])

    model.setItem(0, 0, QStandardItem("Value 1"))
    model.setItem(0, 1, QStandardItem("Value 2"))
    model.setItem(1, 0, QStandardItem("Value 3"))
    model.setItem(1, 1, QStandardItem("Value 4"))
    model.setItem(2, 0, QStandardItem("Value 5"))
    model.setItem(2, 1, QStandardItem("Value 6"))

    engine = QQmlApplicationEngine()
    engine.setInitialProperties({"tableModel": model})
    engine.load('Main.qml')

    sys.exit(app.exec())
