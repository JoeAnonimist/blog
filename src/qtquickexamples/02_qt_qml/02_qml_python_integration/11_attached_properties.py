import sys

from PySide6.QtCore import QObject, Signal, Property
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, QmlElement, QmlAnonymous, QmlAttached


QML_IMPORT_NAME = 'examples.logger'
QML_IMPORT_MAJOR_VERSION = 1

@QmlAnonymous
class LogDetails(QObject):

    severityChanged = Signal(int)
    filenameChanged = Signal(str)
    
    def getSeverity(self):
        return self.severity_value
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.severity_value = 0
        self.fname_value = ''
    
    def setSeverity(self, value):
        if value != self.severity_value:
            print('in severity')
            self.severity_value = value
            self.severityChanged.emit(value)
    
    def getFilename(self):
        return self.fname_value
    
    def setFilename(self, value):
        if value != self.fname_value:
            self.fname_value = value
            self.filenameChanged.emit(value)
    
    severity = Property(int, fget=getSeverity,
        fset=setSeverity, notify=severityChanged)
    
    filename = Property(str, fget=getFilename, 
        fset=setFilename, notify=filenameChanged) 


@QmlElement
@QmlAttached(LogDetails)
class Logger(QObject):
    
    messageChanged = Signal(str)
    msg_value = ''
    
    def getMessage(self):
        return self.msg_value
    
    def setMessage(self, value):
        if value != self.msg_value:
            self.messageChanged.emit(value)
            self.msg_value = value
            
    message = Property(str, fget=getMessage,
        fset=setMessage, notify=messageChanged)
    
    @staticmethod
    def qmlAttachedProperties(self, obj):
        print("qmlAttachedProperties called for", obj)
        return LogDetails(obj)

if __name__ == '__main__':

    app = QGuiApplication(sys.argv)
    
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('11_attached_properties.qml')

    result = app.exec()
    del engine
    
    sys.exit(result)