import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, 
    QWidget, QPushButton, QComboBox, QVBoxLayout)
from PySide6.QtSql import QSqlDatabase, QSqlQuery


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.query_string = 'Select * From Categories'
        
        self.tables = QComboBox()
        self.tables.addItems(['Accounts', 'Categories',
            'Transactions', 'Users'])
        self.tables.currentIndexChanged.connect(self.on_index_changed)

        self.button = QPushButton('Execute query')
        self.button.clicked.connect(self.on_button_clicked)
        
        layout.addWidget(self.tables)
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
        result = query.exec(self.query_string)
        
        if result:
            while query.next():
                record = query.record()
                for i in range(record.count()):
                    print(f'{query.value(i)}\t', end='')
                print()
        else:
            print(query.lastError().text())
            
    @Slot()
    def on_index_changed(self, index):
        table_name = self.tables.currentText()
        self.query_string = f'Select * From {table_name}'
        print(f'Current query: {self.query_string}')
    

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()
    
    sys.exit(app.exec())
