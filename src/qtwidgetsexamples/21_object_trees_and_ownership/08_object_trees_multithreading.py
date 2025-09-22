import sys
from PySide6.QtCore import (
    QObject, QThread, Slot, Signal, QTimer,
    QMetaObject, Qt)
from PySide6.QtWidgets import (QApplication,
    QPushButton, QLabel, QWidget, QVBoxLayout)


class MyObject(QObject):
    
    finished = Signal()
    error = Signal(str)
    
    def __init__(self, name, parent=None):
        super().__init__(parent)
        self.name = name
        self.setObjectName(name)
        self.destroyed.connect(MyObject.on_destroyed)

    def __del__(self):
        print(f'Deleted: {self.name}')

    @Slot()
    @staticmethod
    def on_destroyed(obj):
        print(f'Destroyed: {obj.objectName()}')
        
    @Slot()
    def process(self):
        print(f'Processing in thread: {self.name}')
        # Simulate work
        QTimer.singleShot(1000, self.finished.emit)


class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.button = QPushButton('Start background thread')
        self.button.clicked.connect(self.on_button_clicked)
        
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        
        self.background_thread = None
        
    @Slot()
    def on_button_clicked(self):
        
        if self.background_thread:
            if not self.background_thread.isFinished():
                return
        
        self.parent_obj = MyObject('parent')
        
        child1 = MyObject('child 1')
        child1.setParent(self.parent_obj)
        
        child2 = MyObject('child 2')
        child2.setParent(child1)
        
        child3 = MyObject('child 3')
        child3.setParent(self.parent_obj)
        
        print('Object tree in main thread:')
        self.parent_obj.dumpObjectTree()
        
        self.background_thread = QThread()
        self.parent_obj.moveToThread(self.background_thread)
        
        print('Object tree in background thread:')
        self.parent_obj.dumpObjectTree()
        
        self.parent_obj.destroyed.connect(self.clean_up)
        self.background_thread.finished.connect(
            self.background_thread.deleteLater)
        self.background_thread.finished.connect(
            lambda: self.label.setText('Worker finished'))
        
        QMetaObject.invokeMethod(self.parent_obj, 'process', Qt.QueuedConnection)
        
        self.background_thread.start()
        self.button.setEnabled(False)
        self.label.setText('Thread started...')

        QTimer.singleShot(3000, self.parent_obj.deleteLater)
        
    @Slot()
    def clean_up(self):
        try:
            if self.background_thread:
                self.background_thread.quit()
                self.background_thread.wait()
                self.background_thread = None  # Null ref to prevent access errors
        except RuntimeError:  # If already deleted
            pass
        self.button.setEnabled(True)
        self.label.setText('Cleanup done')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())