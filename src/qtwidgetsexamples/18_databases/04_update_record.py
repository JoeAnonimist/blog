import sys
from PySide6.QtCore import QDate, Slot, Qt
from PySide6.QtWidgets import (QApplication, 
    QWidget, QPushButton, QVBoxLayout,
    QTableWidget, QTableWidgetItem)
from PySide6.QtSql import QSqlDatabase, QSqlQuery


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.resize(620, 200)
        
        self.query_string = 'Select * From Transactions'
        
        self.transaction_table = QTableWidget()
        self.transaction_table.itemChanged.connect(self.on_item_changed)
        layout.addWidget(self.transaction_table)
        
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('finance_demo.sqlite')
        
        result = self.db.open()
        if result:
            print('Connected!')
            self.load_transactions()
            self.set_column_widths()
        else:
            print('Failed to connect to the database')
            
    @Slot(QTableWidgetItem)
    def on_item_changed(self, item):
        
        row = item.row()
        column = item.column()
        column_name = self.columns[column]
        value = item.data(Qt.ItemDataRole.DisplayRole)
        print(value)
        id_item = self.transaction_table.item(row, 0)
        transaction_id = id_item.data(Qt.ItemDataRole.DisplayRole)
        
        query_string = f'Update Transactions Set {column_name} = :value Where transaction_id = :transaction_id'
        query = QSqlQuery()
        query.prepare(query_string)
        query.bindValue(':value', value)
        query.bindValue(':transaction_id', transaction_id)
        
        result = query.exec()
        
        if not result:
            print(query.lastError().text())
        else:
            print('Updated record')
            print(query.executedQuery())
    
    def load_transactions(self):
        
        query = QSqlQuery()
        result = query.exec(self.query_string)
        
        if result:
            
            self.transaction_table.blockSignals(True)
            
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
                    if column == 0:
                        item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                    self.transaction_table.setItem(row, column, item)
                    print(f'{query.value(column)}\t', end='')
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
