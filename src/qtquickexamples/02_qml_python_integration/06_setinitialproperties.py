import sys

from PySide6.QtCore import QObject, Property, Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

# 1. Create a QObject subclass

class Logger(QObject):
    
    
    fname_value = ''
    
    @Property(str)
    def filename(self):
        return self.fname_value
    
    @filename.setter
    def filename(self, value):
        if value != self.fname_value:
            self.fname_value = value
    
    @Slot(str)
    def log(self, message):
        print(self.filename, ':', message)    

if __name__ == '__main__':

    app = QGuiApplication(sys.argv)
    
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    
    # 3. Create a Logger object
    
    logger = Logger()
    
    # 4. Use QQMlApplicationEngine.setInitialProperties()
    #    to set the QML ApplicationWindow.logger property.
    #    The setInitialProperties argument is a dictionary.
    
    engine.setInitialProperties({'logger': logger})
    
    engine.load('06_setinitialproperties.qml')

    result = app.exec()
    del engine
    
    sys.exit(result)