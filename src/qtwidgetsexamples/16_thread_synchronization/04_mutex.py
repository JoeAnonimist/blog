import sys
from PySide6.QtCore import (QObject, Slot, Signal, QThread,
    QEventLoop, QTimer, QMutex)
from PySide6.QtWidgets import (QApplication, 
    QWidget, QPushButton, QVBoxLayout, QLabel)


class BankAccount(QObject):
    
    def __init__(self, balance, parent=None):
        super().__init__(parent)
        self.balance = balance
        self.mutex = QMutex()
    
    @Slot(result=int)
    def get_balance(self):
        return self.balance
    
    def withdraw(self, amount):
        self.mutex.lock()
        print('---withdraw start---',
            QThread.currentThread().objectName())
        balance = self.balance
        QThread.msleep(1)
        #print(end='')
        #loop = QEventLoop()
        #QTimer.singleShot(1000, loop.quit)
        if balance >= amount:
            balance -= amount
            self.balance = balance
        print('---withdraw end---',
            QThread.currentThread().objectName(), self.balance)
        self.mutex.unlock()
            
            
class Worker(QObject):
    
    finished = Signal()

    def __init__(self, bank_account, amount, parent=None):
        super().__init__(parent)
        self.bank_account = bank_account
        self.amount = amount

    def process(self):
        self.bank_account.withdraw(self.amount)
        self.finished.emit()


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        self.thread_count = 5
        self.amount = 100

        self.label = QLabel("Click to start", self)
        self.button = QPushButton("Start Threads", self)
        self.button.clicked.connect(self.start_threads)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.workers = []

    def start_threads(self):

        self.button.setEnabled(False)

        self.bank_account = BankAccount(self.thread_count * self.amount)
        self.bank_account_thread = QThread()
        self.bank_account_thread.setObjectName('Bank account thread')
        self.bank_account.moveToThread(self.bank_account_thread)
        self.bank_account_thread.start()
        
        self.completed = 0

        self.workers.clear()

        for i in range(self.thread_count):
            background_thread = QThread(self)
            background_thread.setObjectName(f'Thread {i}')

            worker_obj = Worker(self.bank_account, self.amount)
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
            print('Expected: 0, Got:', self.bank_account.balance)
            self.label.setText(f"Final counter: {self.bank_account.balance}")
            self.bank_account_thread.quit()
            self.bank_account_thread.wait()
            self.button.setEnabled(True)
            print('=====================')


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()
    
    sys.exit(app.exec())
