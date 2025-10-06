import sys

from PySide6.QtCore import QDir, Qt
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QFileSystemModel


class MyFileSystemModel(QFileSystemModel):
    
    isDirRole = Qt.UserRole + 100
    
    def roleNames(self):
        roles = super().roleNames()
        roles[self.isDirRole] = b'isDir'
        return roles
    
    def data(self, index, role):
        if role == self.isDirRole:
            return self.isDir(index)
        return super().data(index, role)


if __name__ == '__main__':

    app = QGuiApplication(sys.argv)
    
    engine = QQmlApplicationEngine()
    
    model = MyFileSystemModel()
    
    root_path = QDir.homePath()
    model.setRootPath(root_path)
    
    root_index = model.index(root_path)
    
    engine.setInitialProperties(
        {'fsModel': model, 'rootIndex': root_index})
    
    engine.load('delegatemodelgroup.qml')

    sys.exit(app.exec())
