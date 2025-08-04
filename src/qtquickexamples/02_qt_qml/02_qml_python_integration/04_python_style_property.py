import sys

from PySide6.QtCore import QObject, Slot, Signal, Property
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, QmlElement

# 1. Set the global variables

QML_IMPORT_NAME = 'examples.logger'
QML_IMPORT_MAJOR_VERSION = 1

# 2. Decorate the class with @QmlElement
#     and subclass QObject

@QmlElement
class Logger(QObject):
    
    filenameChanged = Signal(str)
    fname_value = '<no name>'
    
    @Property(str, notify=filenameChanged)
    def filename(self):
        return self.fname_value
    
    @filename.setter
    def filename(self, value):
        if value != self.fname_value:
            self.fname_value = value
            self.filenameChanged.emit(value)

if __name__ == '__main__':

    app = QGuiApplication(sys.argv)
    
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('04_python_style_property.qml')

    result = app.exec()
    del engine
    
    sys.exit(result)