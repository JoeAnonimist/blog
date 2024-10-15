import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


if __name__ == '__main__':
    
    # 1. Create a QGuiApplication instance

    app = QGuiApplication(sys.argv)
    
    # 2. Create a QQMlApplicationEngine instance and connect
    #    its quit signal with QGuiApplication.quit()
    
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    
    # 3. Load the Qml file and start the event loop
    
    engine.load('01_hello_world.qml')

    sys.exit(app.exec())