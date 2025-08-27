import sys

from PySide6.QtCore import Qt, QEvent, QKeyCombination
from PySide6.QtGui import QKeySequence
from PySide6.QtWidgets import (QApplication, 
    QWidget, QLabel, QVBoxLayout)

class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        self.resize(300, 200)
        self.setAcceptDrops(True)
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.label = QLabel('Hello, events!')
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)
        
        self.installEventFilter(self)

    def eventFilter(self, watched, event):
        if watched == self:
            if event.type() == QEvent.Type.KeyPress:
                print('Filter for key press')
                return False
        return QWidget.eventFilter(self, watched, event)

    
    def event(self, event):
        if event.type() == QEvent.Type.KeyPress:
            print('Intercepted key pressed event')
            # return True
        if event.type() in (QEvent.Type.Show, QEvent.Type.Hide):
            print('Intercepted show/hide event')
            #return True

        return QWidget.event(self, event)
    
    # Specialized event handlers
    
    def keyPressEvent(self, event):

        modifiers = Qt.KeyboardModifier(event.modifiers())
        key = Qt.Key(event.key())
    
        combo = QKeyCombination(modifiers, key)
        key_seq = QKeySequence(combo)
        key_str = key_seq.toString(QKeySequence.NativeText)
        
        print(key_str)
        self.label.setText(key_str)

        QWidget.keyPressEvent(self, event)

    def dragEnterEvent(self, event):
        event.acceptProposedAction()
        QWidget.dragEnterEvent(self, event)
    
    def dropEvent(self, event):
        event.acceptProposedAction()
        try:
            print(event.mimeData().urls()[0].toLocalFile())
        except Exception as e:
            print(e)
        QWidget.dropEvent(self, event)
        
    def hideEvent(self, event):
        print('Hidden')
        QWidget.hideEvent(self, event)
        
    def showEvent(self, event):
        print('Shown')
        QWidget.showEvent(self, event)
      

if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
