import sys

from PySide6.QtCore import QtMsgType, qInstallMessageHandler
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


def qt_message_handler(mode, context, message):
    if mode == QtMsgType.QtInfoMsg:
        mode = 'Info'
    elif mode == QtMsgType.QtWarningMsg:
        mode = 'Warning'
    elif mode == QtMsgType.QtCriticalMsg:
        mode = 'Critical'
    elif mode == QtMsgType.QtFatalMsg:
        mode = 'Fatal'
        print(f"{mode}: {message} ({context.file}:{context.line})", file=sys.stderr)
        sys.exit(1)
    else:
        mode = 'Debug'
    print(f"{mode}: {message} ({context.file}:{context.line})", file=sys.stderr)

if __name__ == '__main__':

    qInstallMessageHandler(qt_message_handler)

    app = QGuiApplication(sys.argv)
    
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('04_split_view.qml')

    sys.exit(app.exec())