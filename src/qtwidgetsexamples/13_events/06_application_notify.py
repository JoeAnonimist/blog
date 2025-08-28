import sys

from PySide6.QtCore import QEvent
from PySide6.QtWidgets import (QApplication, QWidget, 
    QPushButton, QVBoxLayout)


# Future direction: This function will not be called
# for objects that live outside the main thread in Qt 7.
# Applications that need that functionality
# should find other solutions for their event
# inspection needs in the meantime. The change may be extended
# to the main thread, causing this function to be deprecated.

# Warning: If you override this function, you must ensure
# all threads that process events stop doing so
# before your application object begins destruction.
# This includes threads started by other libraries
# that you may be using, but does not apply to Qt's own threads.

class MyCustomApplication(QApplication):
    
    def notify(self, receiver, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            print('Filter mouse press for: ', receiver.objectName())
            if isinstance(receiver, QPushButton):
                if not receiver.isEnabled():
                    receiver.clicked.emit()
                    return True
        return super().notify(receiver, event)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        self.setObjectName('Main Window')
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        button1 = QPushButton('Button 1')
        button1.setObjectName('button1')
        button1.clicked.connect(self.on_button_clicked)
        
        button2 = QPushButton('Button 2')
        button2.setObjectName('button2')
        button2.clicked.connect(self.on_button_clicked)
        button2.setDisabled(True)
        
        button3 = QPushButton('Button 3')
        button3.setObjectName('button3')
        button3.clicked.connect(self.on_button_clicked)
        
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addStretch()
        
    def on_button_clicked(self):
        print('Button clicked: ', self.sender().objectName())
      

if __name__ == '__main__':

    app = MyCustomApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
