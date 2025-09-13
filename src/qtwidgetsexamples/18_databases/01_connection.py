import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, 
    QWidget, QPushButton, QVBoxLayout)
from PySide6.QtSql import QSqlDatabase


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)

        button = QPushButton('Print database info')
        button.clicked.connect(self.on_button_clicked)
        layout.addWidget(button)
        
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('finance_demo.sqlite')
        
        if self.db.open():
            print('Connected!')
        else:
            print('Failed to connect to the database')
    
    @Slot()
    def on_button_clicked(self, checked):
        print('Name: ', self.db.databaseName())
        print('Driver: ', self.db.driverName())
        print('Tables: ')
        for table in self.db.tables():
            print(f'\t{table}')
        

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()
    
    sys.exit(app.exec())
