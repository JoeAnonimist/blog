import sys
from PySide6.QtCore import Slot, QMetaType
from PySide6.QtWidgets import (QApplication, 
    QWidget, QComboBox, QVBoxLayout, QTableView)
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlField


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.tables = QComboBox()
        self.tables.addItems(['Accounts', 'Categories',
            'Transactions', 'Users'])
        self.tables.currentIndexChanged.connect(self.on_index_changed)
        
        layout.addWidget(self.tables)
        
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('finance_demo.sqlite')
        
        result = self.db.open()
        if result:
            print('Connected!')
        else:
            print('Failed to connect to the database')
        
        self.table_model = QSqlTableModel()
        self.table_model.setTable('Accounts')
        self.table_model.select()
        
        self.table_view = QTableView()        
        self.table_view.setModel(self.table_model)
        layout.addWidget(self.table_view)

    @Slot()
    def on_index_changed(self, index):
        
        table_name = self.tables.currentText()
        self.table_model.setTable(table_name)
        self.table_model.select()
    

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()
    
    sys.exit(app.exec())
