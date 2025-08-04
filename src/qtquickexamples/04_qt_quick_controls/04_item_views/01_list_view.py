import sys

from PySide6.QtCore import QDir
from PySide6.QtGui import QGuiApplication, QStandardItemModel, QStandardItem
from PySide6.QtQml import QQmlApplicationEngine


if __name__ == '__main__':
    
    fsmodel = QStandardItemModel()
    
    files = QDir.home().entryList()
    for f in files:
        item = QStandardItem(f)
        fsmodel.appendRow(item)

    app = QGuiApplication(sys.argv)
    
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)

    engine.setInitialProperties({'fsmodel': fsmodel})
    engine.load('01_list_view.qml')
    
    result = app.exec()
    del engine
    
    sys.exit(result)