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
    
    # 3. Define the signal, the getter and the setter
    
    filenameChanged = Signal(str)
    
    fname_value = '<no name>'
    
    def getFilename(self):
        return self.fname_value
    
    def setFilename(self, value):
        if value != self.fname_value:
            self.fname_value = value
            self.filenameChanged.emit(value)
    
    # 4. Declare the property
    #    notify=... is necessary if the signal name
    #    does not follow convention.   
    filename = Property(str, fget=getFilename, 
        fset=setFilename, notify=filenameChanged)    

if __name__ == '__main__':

    app = QGuiApplication(sys.argv)
    
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('03_property.qml')

    result = app.exec()
    del engine
    
    sys.exit(result)