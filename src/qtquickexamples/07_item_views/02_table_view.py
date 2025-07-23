import sys

from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


def set_up_model():
    
    database = QSqlDatabase.addDatabase('QSQLITE')
    database.setDatabaseName(':memory:')
    database.open()
    
    query = QSqlQuery()
    query.exec('''
    Create Table users (
    id Integer Primary Key,
    fname Text Not Null,
    lname Text Not Null,
    age Integer Not Null)
    ''')

    query.exec('''
    Insert Into users (fname, lname, age)
    Values
    ('Alice', 'Carol', 32),
    ('Bob', 'Rock', 28),
    ('Chuck', 'Moore', 23)
    ''')

    model = QSqlQueryModel()
    model.setQuery('Select * From users')
    model.setHeaderData(0, Qt.Horizontal, 'Id')
    model.setHeaderData(1, Qt.Horizontal, 'First Name')
    model.setHeaderData(2, Qt.Horizontal, 'Last Name')
    model.setHeaderData(3, Qt.Horizontal, 'Age')
    
    return model


if __name__ == '__main__':
    
    app = QGuiApplication(sys.argv)
    
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    
    model = set_up_model()

    engine.setInitialProperties({'sqlmodel': model})
    engine.load('02_table_view.qml')
    
    result = app.exec()
    del engine
    
    sys.exit(result)