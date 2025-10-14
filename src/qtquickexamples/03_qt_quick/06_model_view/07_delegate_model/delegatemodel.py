import sys

from PySide6.QtCore import QDir
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QFileSystemModel, QApplication


if __name__ == '__main__':

    app = QApplication(sys.argv)
    
    engine = QQmlApplicationEngine()
    
    model = QFileSystemModel()
    
    root_path = QDir.homePath()
    model.setRootPath(QDir.homePath())
    
    root_index = model.index(root_path)
    
    engine.setInitialProperties(
        {'fsModel': model, 'rootIndex': root_index})
    
    engine.load('delegatemodel.qml')

    sys.exit(app.exec())