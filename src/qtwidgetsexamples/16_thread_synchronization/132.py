import sys
from PySide6.QtCore import QObject, QRunnable, QThreadPool, QCoreApplication, QTimer, Signal, Slot
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel


class BankAccount(QObject):
    def __init__(self, balance, parent=None):
        super().__init__(parent)
        self.balance = balance

    @Slot(result=int)
    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        print('---withdraw start---', QCoreApplication.instance().thread().objectName())
        balance = self.balance
        QTimer.singleShot(1, lambda: None)  # simulate delay (no sleep in main thread)
        if balance >= amount:
            balance -= amount
            self.balance = balance
        print('---withdraw end---', QCoreApplication.instance().thread().objectName(), self.balance)


class Worker(QRunnable):
    def __init__(self, bank_account, amount, on_done):
        super().__init__()
        self.bank_account = bank_account
        self.amount = amount
        self.on_done = on_done

    def run(self):
        self.bank_account.withdraw(self.amount)
        QTimer.singleShot(0, self.on_done)  # post back to main thread safely


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

        self.thread_pool = QThreadPool()
        self.bank_account = None
        self.completed = 0

    def start_threads(self):
        self.button.setEnabled(False)
        self.completed = 0

        self.bank_account = BankAccount(self.thread_count * self.amount)

        for _ in range(self.thread_count):
            worker = Worker(self.bank_account, self.amount, self.on_worker_done)
            self.thread_pool.start(worker)

    def on_worker_done(self):
        self.completed += 1

        if self.completed == self.thread_count:
            print('Expected: 0, Got:', self.bank_account.balance)
            self.label.setText(f"Final counter: {self.bank_account.balance}")
            self.button.setEnabled(True)
            print('=====================')
            self.button.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
