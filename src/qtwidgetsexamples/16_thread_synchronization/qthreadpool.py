import sys
from PySide6.QtCore import QObject, Slot, Signal, QThread, QTimer, QRunnable, QThreadPool
from PySide6.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QLabel)


class BankAccount(QObject):
    
    def __init__(self, balance, parent=None):
        super().__init__(parent)
        self.balance = balance
    
    @Slot(int)
    def withdraw(self, amount):
        print('---withdraw start---', QThread.currentThread().objectName())
        balance = self.balance
        QThread.msleep(1)
        if balance >= amount:
            balance -= amount
            self.balance = balance
        print('---withdraw end---', QThread.currentThread().objectName(), self.balance)
    
    @Slot(result=int)
    def get_balance(self):
        return self.balance


class WorkerSignals(QObject):
    finished = Signal()


class Worker(QRunnable):
    
    def __init__(self, bank_account, amount, index):
        super().__init__()
        self.bank_account = bank_account
        self.amount = amount
        self.index = index
        self.signals = WorkerSignals()
        self.setAutoDelete(True)

    @Slot()
    def run(self):
        QThread.currentThread().setObjectName(f'Thread {self.index}')
        self.bank_account.withdraw(self.amount)
        self.signals.finished.emit()


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

        pool = QThreadPool.globalInstance()

        for i in range(self.thread_count):
            worker_obj = Worker(self.bank_account, self.amount, i)
            self.workers.append(worker_obj)
            worker_obj.signals.finished.connect(self.on_worker_done)
            pool.start(worker_obj)
            
    def on_worker_done(self):
        self.completed += 1

        if self.completed == self.thread_count:
            print('Expected: 0, Got:', self.bank_account.get_balance())
            self.label.setText(f"Final counter: {self.bank_account.get_balance()}")
            self.bank_account_thread.quit()
            self.bank_account_thread.wait()
            self.button.setEnabled(True)
            print('=====================')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())