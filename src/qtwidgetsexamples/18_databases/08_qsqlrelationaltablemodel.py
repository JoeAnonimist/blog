import sys
from PySide6.QtWidgets import (QApplication, 
    QWidget, QVBoxLayout, QTableView)
from PySide6.QtSql import (QSqlDatabase, 
    QSqlRelationalTableModel, QSqlRelation, QSqlRelationalDelegate)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('finance_demo.sqlite')
        
        result = self.db.open()
        if result:
            print('Connected!')
        else:
            print('Failed to connect to the database')
        
        self.table_model = QSqlRelationalTableModel()
        self.table_model.setTable('Transactions')
        
        self.table_model.setRelation(1,
            QSqlRelation('Accounts', 'account_id', 'account_name'))        
        self.table_model.setRelation(2,
            QSqlRelation('Categories', 'category_id', 'category_name'))
        
        self.table_model.select()
        
        self.table_view = QTableView()        
        self.table_view.setModel(self.table_model)
        
        # Provide comboboxes
        delegate = QSqlRelationalDelegate(self.table_view)
        self.table_view.setItemDelegate(delegate)
        
        layout.addWidget(self.table_view)


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()
    
    sys.exit(app.exec())
