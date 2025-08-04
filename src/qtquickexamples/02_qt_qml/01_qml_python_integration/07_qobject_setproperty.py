import sys

from PySide6.QtCore import QObject, Property, Slot, QUrl, qInstallMessageHandler
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

class Logger(QObject):

    fname_value = ''
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.default_handler = qInstallMessageHandler(None)
    
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
        
    def msg_handler(self, msg_type, context, message):
        self.fname_value = QUrl(context.file).fileName()
        if self.default_handler and context.category != 'ignoreme':
            self.default_handler(msg_type, context, message)

if __name__ == '__main__':
    
    logger = Logger()
    
    qInstallMessageHandler(logger.msg_handler)

    app = QGuiApplication(sys.argv)
    
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    
    engine.load(QUrl.fromLocalFile('07_qobject_setproperty.qml'))

    root = engine.rootObjects()[0]
    button = root.findChild(QObject, 'button')
    button.setProperty('logger', logger)

    result = app.exec()
    del engine
    
    sys.exit(result)