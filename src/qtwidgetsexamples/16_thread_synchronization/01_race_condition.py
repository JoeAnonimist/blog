import sys

from PySide6.QtCore import (QObject, QThread,
    Slot, Signal, Qt)
from PySide6.QtWidgets import (QApplication,
    QPushButton, QLabel, QWidget, QVBoxLayout)


class SharedResource(QObject):
    
    def __init__(self, parent=None):
        
        super().__init__(parent)
        self.counter = 0
        
        file_name = 'temp_file.txt'
        with open(file_name, 'w+') as f:
            for _ in range(100):
                f.write('Some text\n')


class Worker(QObject):
    
    finished = Signal()
    
    def __init__(self, shared_resource, parent=None):
        super().__init__(parent)
        self.shared_resource = shared_resource
        
    @Slot()
    def process(self):

        for _ in range(200):
            local_var = self.shared_resource.counter
            with open('temp_file.txt', 'r') as f:
                f.read()
            local_var += 1
            self.shared_resource.counter = local_var
        print(QThread.currentThread().objectName(),
            'Counter value: ', self.shared_resource.counter)
        
        self.finished.emit()


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        button = QPushButton('Start background threads')
        button.clicked.connect(self.on_button_clicked)
        
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout.addWidget(button)
        layout.addWidget(self.label)
        
        self.shared_resource = SharedResource()
    
    @Slot()
    def on_button_clicked(self):
        
        print('Counter value: ', self.shared_resource.counter)
        self.shared_resource.counter = 0
        self.workers = []
        
        for i in range(5):
            
            background_thread = QThread(self)
            background_thread.setObjectName(f'Thread {i}')

            worker_obj = Worker(self.shared_resource)
            self.workers.append(worker_obj)
            worker_obj.moveToThread(background_thread)
            
            worker_obj.finished.connect(self.on_finished)
    
            background_thread.started.connect(worker_obj.process)
            worker_obj.finished.connect(background_thread.quit)
            worker_obj.finished.connect(worker_obj.deleteLater)
            background_thread.finished.connect(background_thread.deleteLater)
            
            background_thread.start()
    
    @Slot()
    def on_finished(self):
        self.label.setText('Final counter value: ' +
            str(self.shared_resource.counter) +
            ' of 1000 expected.')


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
