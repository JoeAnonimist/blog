import sys

from PySide6.QtCore import QDir
from PySide6.QtWidgets import QFileSystemModel
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


if __name__ == '__main__':
    
    app = QGuiApplication(sys.argv)
    
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    
    model = QFileSystemModel()
    model.setRootPath(QDir.home().path())
    
    print(model.roleNames())
    
    home_index = model.index(QDir.home().path())

    engine.setInitialProperties({'fsmodel': model, 'home_index': home_index})
    engine.load('03_tree_view.qml')
    
    result = app.exec()
    del engine
    
    sys.exit(result)