import sys

from PySide6.QtCore import (QObject, QSortFilterProxyModel,
    QRegularExpression, Property, Signal, Slot)
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


class FilterModel(QObject):

    model_changed = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setFilterKeyColumn(0)

    @Property(QObject, notify=model_changed)
    def model(self):
        return self.proxy_model

    @model.setter
    def model(self, source_model):
        self.proxy_model.setSourceModel(source_model)
        self.model_changed.emit()


    @Slot()
    def filter_even(self):
        self.proxy_model.setFilterRegularExpression(
            QRegularExpression("\\b-?\\d*[02468]\\b"))

    @Slot()
    def filter_odd(self):
        self.proxy_model.setFilterRegularExpression(
            QRegularExpression("\\b-?\\d*[13579]\\b"))


if __name__ == '__main__':

    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()
    filter_model = FilterModel()
    engine.setInitialProperties({'filterModel': filter_model})
    engine.load('Main.qml')

    sys.exit(app.exec())
