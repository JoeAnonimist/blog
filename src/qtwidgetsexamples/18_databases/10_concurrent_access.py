import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QLineEdit, QTableView, QMessageBox
)
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PySide6.QtCore import QThread, Signal, Slot


def initialize_database():
    db = QSqlDatabase.addDatabase("QSQLITE", "init_conn")
    db.setDatabaseName("example.db")
    if not db.open():
        raise Exception("Could not open database.")

    query = QSqlQuery(db)
    query.exec("""
        CREATE TABLE IF NOT EXISTS Users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)
    db.close()
    QSqlDatabase.removeDatabase("init_conn")


class ReaderThread(QThread):
    result_ready = Signal(list)

    def run(self):
        db = QSqlDatabase.addDatabase("QSQLITE", "readConn")
        db.setDatabaseName("example.db")
        if not db.open():
            self.result_ready.emit([])
            return

        query = QSqlQuery(db)
        result = []
        if query.exec("SELECT user_id, username, email FROM Users"):
            while query.next():
                result.append((query.value(0), query.value(1), query.value(2)))

        db.close()
        QSqlDatabase.removeDatabase("readConn")
        self.result_ready.emit(result)


class WriterThread(QThread):
    write_complete = Signal(str)

    def __init__(self, username, email):
        super().__init__()
        self.username = username
        self.email = email

    def run(self):
        db = QSqlDatabase.addDatabase("QSQLITE", "writeConn")
        db.setDatabaseName("example.db")
        if not db.open():
            self.write_complete.emit("DB connection failed.")
            return

        query = QSqlQuery(db)
        query.prepare("INSERT INTO Users (username, email) VALUES (?, ?)")
        query.addBindValue(self.username)
        query.addBindValue(self.email)

        if query.exec():
            self.write_complete.emit("User added.")
        else:
            self.write_complete.emit(f"Error: {query.lastError().text()}")

        db.close()
        QSqlDatabase.removeDatabase("writeConn")


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Users DB (Multithreaded)")
        initialize_database()

        layout = QVBoxLayout(self)
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")

        self.add_btn = QPushButton("Add User")
        self.refresh_btn = QPushButton("Refresh")

        self.table = QTableView()
        self.model = QSqlTableModel()
        self.model.setTable("Users")
        self.model.select()
        self.table.setModel(self.model)

        layout.addWidget(self.username_input)
        layout.addWidget(self.email_input)
        layout.addWidget(self.add_btn)
        layout.addWidget(self.refresh_btn)
        layout.addWidget(self.table)

        self.add_btn.clicked.connect(self.add_user)
        self.refresh_btn.clicked.connect(self.refresh_users)

    def add_user(self):
        name = self.username_input.text().strip()
        email = self.email_input.text().strip()
        if not name or not email:
            QMessageBox.warning(self, "Input Error", "Both fields are required.")
            return

        self.writer = WriterThread(name, email)
        self.writer.write_complete.connect(self.on_write_done)
        self.writer.start()

    @Slot(str)
    def on_write_done(self, msg):
        QMessageBox.information(self, "Insert Result", msg)
        self.model.select()  # Refresh view

    def refresh_users(self):
        self.reader = ReaderThread()
        self.reader.result_ready.connect(self.on_read_done)
        self.reader.start()

    @Slot(list)
    def on_read_done(self, data):
        print("Read from DB:")
        for row in data:
            print(row)
        self.model.select()  # Refresh view


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(500, 400)
    window.show()
    sys.exit(app.exec())
