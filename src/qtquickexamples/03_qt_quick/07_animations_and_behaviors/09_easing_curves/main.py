import sys
from PySide6.QtCore import QEasingCurve
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


if __name__ == '__main__':

    app = QGuiApplication(sys.argv)

    easingTypes = [t.name for t in QEasingCurve.Type]

    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.setInitialProperties({'easingTypes': easingTypes})
    engine.load('Main.qml')

    sys.exit(app.exec())
