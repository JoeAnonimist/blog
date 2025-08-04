import sys

from PySide6.QtGui import QGuiApplication, QTextCursor
from PySide6.QtCore import QObject, Slot
from PySide6.QtQml import QQmlApplicationEngine, QmlElement
from PySide6.QtQuick import QQuickTextDocument


QML_IMPORT_NAME = 'examples.charcounter'
QML_IMPORT_MAJOR_VERSION = 1


@QmlElement
class CharCounter(QObject):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
    @Slot(QQuickTextDocument, int, result=list)
    def cursor_position(self, textDocument, cursorPosition):

        cursor = QTextCursor(textDocument.textDocument())
        cursor.setPosition(cursorPosition)
        return (cursor.blockNumber(), cursor.columnNumber())
    
    @Slot(QQuickTextDocument, result=int)
    def char_count(self, textDocument):
        return len(textDocument.textDocument().toPlainText())


if __name__ == '__main__':

    app = QGuiApplication(sys.argv)
    
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('04_tool_bar.qml')

    sys.exit(app.exec())