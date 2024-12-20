# The QTableView class provides a default model/view 
# implementation of a table view.
# Just as with QListView you need to provide the model yourself

import sys

from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PySide6.QtWidgets import (QApplication,
    QWidget, QVBoxLayout, QTableView, QHeaderView)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1 - Create the table view
        
        table_view = QTableView()
        
        # 2 - Create the model instance
        
        # Set up the model data for the example
        
        database = QSqlDatabase.addDatabase('QSQLITE')
        database.setDatabaseName(':memory:')
        database.open()
        self.set_up_data()
        
        self.model = QSqlQueryModel()
        self.model.setQuery('Select * From users')
        self.model.setHeaderData(0, Qt.Horizontal, 'Id')
        self.model.setHeaderData(1, Qt.Horizontal, 'First Name')
        self.model.setHeaderData(2, Qt.Horizontal, 'Last Name')
        self.model.setHeaderData(3, Qt.Horizontal, 'Age')
        
        # 3 - Set it as the table view model.
        
        table_view.setModel(self.model)
        
        # Make the columns and rows fit the table view
        # size so there's no scrollbars
        
        table_view.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch)
            
        table_view.verticalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch)
        
        layout.addWidget(table_view)
        
    def set_up_data(self):
        
        # Create a table and fill it with some data
        
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


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
