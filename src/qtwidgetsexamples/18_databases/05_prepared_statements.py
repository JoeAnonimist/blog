import sys
from PySide6.QtCore import QDate, Slot, Qt
from PySide6.QtWidgets import (QApplication, 
    QWidget, QVBoxLayout, QTableWidget, 
    QPushButton, QTableWidgetItem)
from PySide6.QtSql import QSqlDatabase, QSqlQuery


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.resize(620, 200)
        
        self.transactions = [
            (1, 2, -250.00, '2025-09-21', 'Online shopping'),
            (2, 1, 300.00, '2025-09-22', 'Interest deposit'),
            (3, 3, -2000.00, '2025-09-23', 'Real estate investment'),
            (1, 4, -100.00, '2025-09-24', 'Transfer to savings')
        ]
        
        self.query_string = 'Select * From Transactions'
        
        self.transaction_table = QTableWidget()
        layout.addWidget(self.transaction_table)
        
        self.button = QPushButton('Add transactions')
        self.button.clicked.connect(self.add_records)
        layout.addWidget(self.button)
        
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('finance_demo.sqlite')
        
        result = self.db.open()
        if result:
            print('Connected!')
            self.load_transactions()
            self.set_column_widths()
        else:
            print('Failed to connect to the database')
            
    @Slot()
    def add_records(self):
        
        self.button.setDisabled(True)
        
        query_string = ''' 
            INSERT INTO Transactions
                (account_id,
                category_id,
                amount,
                transaction_date,
                description)
            VALUES 
                (:account_id,
                :category_id,
                :amount,
                :transaction_date,
                :description)
        '''
        query = QSqlQuery()
        query.prepare(query_string)
        
        for t in self.transactions:
            query.bindValue(':account_id', t[0])
            query.bindValue(':category_id', t[1])
            query.bindValue(':amount', t[2])
            query.bindValue(':transaction_date', t[3])
            query.bindValue(':description', t[4])
            result = query.exec()
        
            if not result:
                print(query.lastError().text())
            else:
                print(f'Inserted transaction: {t[4]}')
                
        self.load_transactions()
    
    def load_transactions(self):
        
        query = QSqlQuery()
        result = query.exec(self.query_string)
        
        if result:
            
            self.transaction_table.blockSignals(True)
            
            self.transaction_table.clear()
            self.transaction_table.setRowCount(0)
            
            record = query.record()
            column_count = record.count()
            self.transaction_table.setColumnCount(column_count)
            
            self.columns = [record.fieldName(i) for i in range(column_count)]
            self.transaction_table.setHorizontalHeaderLabels(self.columns)

            row = 0

            while query.next():
                self.transaction_table.insertRow(row)
                record = query.record()
                for column in range(record.count()):
                    if column == 4:
                        value = QDate.fromString(query.value(column), 'yyyy-MM-dd')
                    else:
                        value = query.value(column)
                    item = QTableWidgetItem()
                    item.setData(Qt.ItemDataRole.DisplayRole, value)
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                    self.transaction_table.setItem(row, column, item)
                    print(f'{record.value(column)}\t', end='')
                print()
                row += 1
                
            self.transaction_table.blockSignals(False)
        else:
            print(query.lastError().text())

    def set_column_widths(self):
        for c in range(4):
            self.transaction_table.setColumnWidth(c, 80)
        self.transaction_table.setColumnWidth(5, 160)
        self.transaction_table.resizeRowsToContents()
    

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()
    
    sys.exit(app.exec())
