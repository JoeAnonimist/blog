import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, 
    QWidget, QPushButton, QVBoxLayout, QLineEdit)
from PySide6.QtSql import QSqlDatabase, QSqlQuery


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText('Enter user name')
        self.email_edit = QLineEdit()
        self.email_edit.setPlaceholderText('Enter e-mail')

        self.button = QPushButton('Add user')
        self.button.clicked.connect(self.on_button_clicked)
        
        layout.addWidget(self.name_edit)
        layout.addWidget(self.email_edit)
        layout.addWidget(self.button)
        
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('finance_demo.sqlite')
        
        result = self.db.open()
        if result:
            print('Connected!')
        else:
            self.button.setDisabled(True)
            print('Failed to connect to the database')
    
    @Slot()
    def on_button_clicked(self, checked):
        
        query = QSqlQuery()
        query.prepare('''
            Insert Into Users (username, email)
            Values (:name, :email)
            ''')
        query.addBindValue(self.name_edit.text())
        query.addBindValue(self.email_edit.text())
        print(query.lastQuery())
        result = query.exec()
        
        print('last query ', query.lastQuery())
        
        if result:
            print('User added successfully')
        else:
            print(f'Error: {query.lastError().text()}')
    

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()
    
    sys.exit(app.exec())
