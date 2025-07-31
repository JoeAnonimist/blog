import sys

from PySide6.QtCore import QObject, Slot, Signal, Property
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, QmlNamedElement, QmlSingleton

QML_IMPORT_NAME = 'examples.logger'
QML_IMPORT_MAJOR_VERSION = 1

@QmlNamedElement('FileNameLogger')
@QmlSingleton
class Logger(QObject):

    filenameChanged = Signal(str)
    
    fname_value = '<no name>'
    
    def getFilename(self):
        return self.fname_value
    
    def setFilename(self, value):
        if value != self.fname_value:
            self.fname_value = value
            self.filenameChanged.emit(value)

    filename = Property(str, fget=getFilename, 
        fset=setFilename, notify=filenameChanged)    

if __name__ == '__main__':

    app = QGuiApplication(sys.argv)
    
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('08_singleton.qml')

    result = app.exec()
    del engine
    
    sys.exit(result)