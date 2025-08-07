from PySide6.QtCore import QObject
from PySide6.QtQml import QmlElement, QmlUncreatable


QML_IMPORT_NAME = 'examples.logger.logtargets'
QML_IMPORT_MAJOR_VERSION = 1


@QmlElement
@QmlUncreatable('Base class')
class LogTarget(QObject):
    def write(self, severity, message, filename):
        pass
    
@QmlElement
class FileLogTarget(LogTarget):
    def write(self, severity, message, filename):
        print('Logging to a file: ', 'Severity: ',
              severity, message, filename)
        
@QmlElement
class ConsoleLogTarget(LogTarget):
    def write(self, severity, message, filename):
        print('Logging to console: ', 'Severity: ',
              severity, message, filename)
        
@QmlElement
class PopupLogTarget(LogTarget):
    def write(self, severity, message, filename):
        print('Message box: ', 'Severity: ',
              severity, message, filename)