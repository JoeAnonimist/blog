import sys
from PySide6.QtCore import (QObject, Signal,
    QThread, QMutex, QMutexLocker, QWaitCondition)
from PySide6.QtWidgets import (QApplication, QWidget,
    QPushButton, QVBoxLayout, QLabel)


class BankAccount(QObject):
    
    def __init__(self, parent=None):
        
        super().__init__(parent)
        self.balance = 0
        self.mutex = QMutex()
        self.condition = QWaitCondition()

    def deposit(self, amount):
        
        locker = QMutexLocker(self.mutex)
        self.balance += amount
        print(f'[Deposit] Balance updated: {self.balance}')
        self.condition.wakeAll()

    def withdraw(self, amount):
        
        locker = QMutexLocker(self.mutex)
        
        thread_name = QThread.currentThread().objectName()
        while self.balance < amount:
            print(f'[Withdraw] No money. Waiting... | Thread: {thread_name}')
            self.condition.wait(self.mutex)

        self.balance -= amount
        print(f'[Withdraw] Done. Remaining: {self.balance} | Thread: {thread_name}')


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

        self.label = QLabel()
        self.start_button = QPushButton('Start Withdrawals', self)
        self.deposit_button = QPushButton('Deposit Funds', self)
        self.start_button.clicked.connect(self.start_threads)
        self.deposit_button.clicked.connect(self.deposit_money)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.start_button)
        layout.addWidget(self.deposit_button)

        self.workers = []
        self.bank_account = BankAccount()
        self.completed = 0

    def start_threads(self):
        
        self.start_button.setEnabled(False)
        self.completed = 0

        for i in range(self.thread_count):
            thread = QThread(self)
            thread.setObjectName(f'Thread {i}')
            worker = Worker(self.bank_account, self.amount)
            worker.moveToThread(thread)

            thread.started.connect(worker.process)
            worker.finished.connect(self.on_worker_done)
            worker.finished.connect(thread.quit)
            worker.finished.connect(worker.deleteLater)
            thread.finished.connect(thread.deleteLater)

            thread.start()
            self.workers.append(worker)

    def deposit_money(self):
        
        deposit = self.amount * self.thread_count
        print(f'[Main] Depositing {deposit}')
        self.bank_account.deposit(deposit)
        self.label.setText(
            f'Remaining balance: {self.bank_account.balance}')

    def on_worker_done(self):
        print(self.sender())
        self.completed += 1
        if self.completed == self.thread_count:
            print(f'Remaining balance: {self.bank_account.balance}')
            self.label.setText(
                f'Remaining balance: {self.bank_account.balance}')
            self.start_button.setEnabled(True)


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    
    main_window = Window()
    main_window.show()
    
    sys.exit(app.exec())
