import sys

from PySide6.QtCore import QObject, Slot, Signal, Property
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, QmlElement, QmlAnonymous


QML_IMPORT_NAME = 'examples.logger'
QML_IMPORT_MAJOR_VERSION = 1

# 1. Create a class to hold the grouped properties
#    and decorate it with @QmlAnonymous

@QmlAnonymous
class LogDetails(QObject):
    
    # 2. Create the properties
    
    severityChanged = Signal(int)
    filenameChanged = Signal(str)
    
    severity_value = None
    fname_value = ''
    
    def getSeverity(self):
        return self.severity_value
    
    def setSeverity(self, value):
        if value != self.severity_value:
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

# 3. Create the main Qml element class

@QmlElement
class Logger(QObject):
    
    messageChanged = Signal(str)
    msg_value = ''
    details_obj = LogDetails()
    
    def getMessage(self):
        return self.msg_value
    
    def setMessage(self, value):
        if value != self.msg_value:
            self.messageChanged.emit(value)
            self.msg_value = value
            
    message = Property(str, fget=getMessage,
        fset=setMessage, notify=messageChanged)
    
    # 4. Add a property to it with the type of LogDetails
    #    ie. the class that holds the grouped properties.
    
    def getDetails(self):
        return self.details_obj
    
    details = Property(LogDetails, fget=getDetails)

if __name__ == '__main__':

    app = QGuiApplication(sys.argv)
    
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('05_grouped_properties.qml')

    result = app.exec()
    del engine
    
    sys.exit(result)