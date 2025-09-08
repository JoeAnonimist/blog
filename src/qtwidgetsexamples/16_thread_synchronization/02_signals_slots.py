import sys
from PySide6.QtWidgets import (QApplication, QWidget,
    QVBoxLayout, QPushButton, QLabel)
from PySide6.QtCore import QObject, QThread, QTimer, Signal, Slot


class Balance(QObject):
    
    value_changed = Signal(int)
    
    def __init__(self):
        super().__init__()
        self.amount = 0

    @Slot(result=int)
    def get(self):
        return self.amount

    @Slot(int)
    def deposit(self, amount):
        self.do_some_work()
        self.amount = amount
        self.value_changed.emit(self.amount)
        
    @Slot()
    def report(self):
        self.value_changed.emit(self.amount)

    def do_some_work(self):
        total = 0
        print('Doing work')




class Worker(QObject):
    
    finished = Signal()

    def __init__(self, balance, amount, parent=None):
        super().__init__(parent)
        self.balance = balance
        self.amount = amount

    def process(self):
        local_var = self.balance.get()
        local_var += self.amount
        self.balance.deposit(local_var)
        print(QThread.currentThread().objectName())
        self.finished.emit()


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        self.thread_count = 5
        self.amount = 1000
        
        self.setWindowTitle("Race Condition Demo")

        self.label = QLabel("Click to start", self)
        self.button = QPushButton("Start Threads", self)
        self.button.clicked.connect(self.start_threads)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.workers = []

    def start_threads(self):

        self.button.setEnabled(False)

        self.balance = Balance()
        self.balance_thread = QThread()
        self.balance.moveToThread(self.balance_thread)
        self.balance.value_changed.connect(self.on_value_changed)
        self.balance_thread.start()

        self.completed = 0

        self.workers.clear()

        for i in range(self.thread_count):
            background_thread = QThread(self)
            background_thread.setObjectName(f'Thread {i}')

            worker_obj = Worker(self.balance, self.amount)
            self.workers.append(worker_obj)
            worker_obj.moveToThread(background_thread)
            
            worker_obj.finished.connect(self.on_worker_done)
    
            background_thread.started.connect(worker_obj.process)
            worker_obj.finished.connect(background_thread.quit)
            worker_obj.finished.connect(worker_obj.deleteLater)
            background_thread.finished.connect(background_thread.deleteLater)
            
            background_thread.start()

    def on_worker_done(self):
        
        self.completed += 1

        if self.completed == self.thread_count:
            QTimer.singleShot(0, self.balance.report)
            
    @Slot(int)
    def on_value_changed(self, value):
        
        if self.completed == self.thread_count:
            print('\nExpected: ', self.thread_count * self.amount)
            print('Got:', value)
            self.label.setText(f"Final counter: {value}")
            self.button.setEnabled(True)
            self.balance_thread.quit()
            self.balance_thread.wait()


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    
    win = Window()
    win.show()
    
    sys.exit(app.exec())

