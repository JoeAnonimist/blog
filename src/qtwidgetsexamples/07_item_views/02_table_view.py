# The QTableView class provides a default model/view 
# implementation of a table view.
# Just as with QListView you need to provide the model yourself

import os
from random import randint
import sqlite3
import sys

from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex
from PySide6.QtWidgets import (QApplication,
    QWidget, QVBoxLayout, QTableView, QHeaderView)
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1 - Set up the model data
        
        self.database = QSqlDatabase.addDatabase('QSQLITE')
        self.database.setDatabaseName(':memory:')
        self.database.open()
        self.set_up_model()
        
        # 2 - Create the table view
        
        table_view = QTableView()
        
        # 3 - Create the model instance and set it
        #     as the table view model.
        
        self.model = QSqlQueryModel()
        self.model.setQuery('Select * From users')
        self.model.setHeaderData(0, Qt.Horizontal, 'Id')
        self.model.setHeaderData(1, Qt.Horizontal, 'fname')
        self.model.setHeaderData(2, Qt.Horizontal, 'lname')
        self.model.setHeaderData(3, Qt.Horizontal, 'age')
        table_view.setModel(self.model)
        
        # Make the columns and rows fit the table view
        # size so there's no scrollbars
        
        table_view.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch)
            
        table_view.verticalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch)
        
        layout.addWidget(table_view)
        
    def set_up_model(self):
        
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

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
