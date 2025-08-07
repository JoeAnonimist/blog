import sys

from PySide6.QtCore import QObject, Slot, Signal, Property
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, QmlElement, ListProperty

from logtarget import LogTarget

QML_IMPORT_NAME = 'examples.logger'
QML_IMPORT_MAJOR_VERSION = 1

@QmlElement
class Logger(QObject):
    
    filenameChanged = Signal(str)
    severityChanged = Signal(int)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.severity_value = 0
        self.fname_value = '<no name>'
        self.log_targets = []
    
    def getFilename(self):
        return self.fname_value
    
    def setFilename(self, value):
        if value != self.fname_value:
            self.fname_value = value
            self.filenameChanged.emit(value)

    filename = Property(str, fget=getFilename, 
        fset=setFilename, notify=filenameChanged)
    
    def getSeverity(self):
        return self.severity_value
    
    def setSeverity(self, value):
        if value != self.severity_value:
            self.severity_value = value
            self.severityChanged.emit(value)
            
    severity = Property(int, fget=getSeverity,
        fset=setSeverity, notify=severityChanged)
    
    def target(self, n):
        return self.log_targets[n]
    
    def targetCount(self):
        return len(self.log_targets)
    
    def appendTarget(self, target):
        self.log_targets.append(target)
    
    targets = ListProperty(LogTarget, appendTarget, final=True)
    
    @Slot(int, str, str)
    def log(self, severity, message, filename):
        for target in self.log_targets:
            target.write(severity, message, filename)

if __name__ == '__main__':

    app = QGuiApplication(sys.argv)
    
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('list_properties.qml')

    result = app.exec()
    del engine
    
    sys.exit(result)