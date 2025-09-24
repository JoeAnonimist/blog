import sys
from PySide6.QtWidgets import (QApplication, QWidget,
    QVBoxLayout, QPushButton, QLineEdit, QTableView)
from PySide6.QtSql import (QSqlDatabase, QSqlQuery,
    QSqlTableModel)
from PySide6.QtCore import QThread, Signal, Slot


class BaseThread(QThread):
    done = Signal(str)

    def __init__(self, query_fn):
        super().__init__()
        self.query_fn = query_fn

    def _open_db(self, prefix):
        conn_name = f'{prefix}_{id(self)}'
        db = QSqlDatabase.addDatabase('QSQLITE', conn_name)
        db.setDatabaseName('finance_demo.sqlite')
        return db, conn_name

    def run(self):
        db, conn_name = self._open_db(self.__class__.__name__.lower())
        if not db.open():
            self.done.emit('DB connection failed.')
            db = None
            return

        query = QSqlQuery(db)
        msg = self.query_fn(query)
        query = None  # explicit cleanup
        del query
        db = None
        del db
        self.done.emit(msg)


class WriterThread(BaseThread):
    def __init__(self, username, email):
        def insert_user(query):
            query.prepare('INSERT INTO Users (username, email) VALUES (?, ?)')
            query.addBindValue(username)
            query.addBindValue(email)
            return 'User added.' if query.exec() else f'Error: {query.lastError().text()}'

        super().__init__(insert_user)


class DeleterThread(BaseThread):
    def __init__(self, user_id):
        def delete_user(query):
            query.prepare('DELETE FROM Users WHERE user_id = ?')
            query.addBindValue(user_id)
            return 'User deleted.' if query.exec() else f'Error: {query.lastError().text()}'

        super().__init__(delete_user)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText('Username')
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText('Email')

        self.add_btn = QPushButton('Add User')
        self.delete_btn = QPushButton('Delete Selected')

        db = QSqlDatabase.addDatabase('QSQLITE', 'main_conn')
        db.setDatabaseName('finance_demo.sqlite')
        if not db.open():
            print(f'DB Error: {db.lastError().text()}')
            return

        self.table = QTableView()
        self.table.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.model = QSqlTableModel(self, db)
        self.model.setTable('Users')
        self.model.select()
        self.table.setModel(self.model)

        layout.addWidget(self.username_input)
        layout.addWidget(self.email_input)
        layout.addWidget(self.add_btn)
        layout.addWidget(self.delete_btn)
        layout.addWidget(self.table)

        self.add_btn.clicked.connect(self.add_user)
        self.delete_btn.clicked.connect(self.delete_user)

    def add_user(self):
        name = self.username_input.text().strip()
        email = self.email_input.text().strip()
        if not name or not email:
            print('Input Error: Both fields are required.')
            return

        self.writer = WriterThread(name, email)
        self.writer.done.connect(self.on_action_done)
        self.writer.finished.connect(self.writer.deleteLater)
        self.writer.start()

    def delete_user(self):
        selected = self.table.selectionModel().selectedRows()
        if not selected:
            print('No row selected.')
            return

        row = selected[0].row()
        user_id = self.model.data(self.model.index(row, 0))  # assumes user_id is column 0
        if user_id is None:
            print('Invalid user ID.')
            return

        self.deleter = DeleterThread(user_id)
        self.deleter.done.connect(self.on_action_done)
        self.deleter.finished.connect(self.deleter.deleteLater)
        self.deleter.start()

    @Slot(str)
    def on_action_done(self, msg):
        print(msg)
        self.model.select()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.resize(500, 300)
    window.show()

    sys.exit(app.exec())
