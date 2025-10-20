import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


if __name__ == '__main__':
    
    # 1. Create a QGuiApplication instance

    app = QGuiApplication(sys.argv)
    
    # 2. Create a QQmlApplicationEngine instance and connect
    #    its quit signal with QGuiApplication.quit()
    
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    
    # 3. Load the Qml file
    
    engine.load('01_hello_world.qml')
    
    # 4.  Start the main event loop

    sys.exit(app.exec())
