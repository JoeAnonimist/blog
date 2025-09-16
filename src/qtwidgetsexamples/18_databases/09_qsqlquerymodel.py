import sys
from PySide6.QtWidgets import (QApplication, 
    QWidget, QVBoxLayout, QTableView)
from PySide6.QtSql import (QSqlDatabase, QSqlQueryModel)


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
            
        query = '''
        SELECT 
            a.account_id, a.account_name, u.username AS owner,
            COALESCE(c.category_name, 'N/A') AS category_name,
            COUNT(t.transaction_id) AS transaction_count,
            COALESCE(SUM(t.amount), 0) AS total_amount,
            COALESCE(AVG(t.amount), 0) AS avg_transaction,
            COALESCE((
                SELECT SUM(t2.amount)
                FROM Transactions t2
                WHERE t2.account_id = a.account_id
                    AND t2.transaction_date LIKE '2025-09%'
            ), 0) AS net_balance
        FROM 
            Accounts a
            INNER JOIN Users u ON a.user_id = u.user_id
            LEFT JOIN Transactions t ON a.account_id = t.account_id 
                AND t.transaction_date LIKE '2025-09%'
            LEFT JOIN Categories c ON t.category_id = c.category_id
        GROUP BY 
            a.account_id, a.account_name, u.username, c.category_name
        UNION ALL
        SELECT 
            a.account_id, a.account_name, u.username AS owner,
            'Total' AS category_name,
            COUNT(t.transaction_id) AS transaction_count,
            COALESCE(SUM(t.amount), 0) AS total_amount,
            COALESCE(AVG(t.amount), 0) AS avg_transaction,
            COALESCE(SUM(t.amount), 0) AS net_balance
        FROM 
            Accounts a
            INNER JOIN Users u ON a.user_id = u.user_id
            LEFT JOIN Transactions t ON a.account_id = t.account_id 
                AND t.transaction_date LIKE '2025-09%'
        GROUP BY 
            a.account_id, a.account_name, u.username
        UNION ALL
        SELECT 
            NULL AS account_id, 'Grand Total' AS account_name,
            NULL AS owner, NULL AS category_name,
            COUNT(t.transaction_id) AS transaction_count,
            COALESCE(SUM(t.amount), 0) AS total_amount,
            COALESCE(AVG(t.amount), 0) AS avg_transaction,
            COALESCE(SUM(t.amount), 0) AS net_balance
        FROM 
            Transactions t
        WHERE 
            t.transaction_date LIKE '2025-09%'
        ORDER BY 
            account_id, category_name      
        '''
        
        self.table_model = QSqlQueryModel()
        self.table_model.setQuery(query)
        
        if self.table_model.query().lastError().isValid():
            print(f"Query error: {self.table_model.query().lastError().text()}")
        
        print(self.table_model.rowCount())
        print(self.table_model.columnCount())
        
        self.table_view = QTableView()        
        self.table_view.setModel(self.table_model)
        
        layout.addWidget(self.table_view)


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()
    
    sys.exit(app.exec())
