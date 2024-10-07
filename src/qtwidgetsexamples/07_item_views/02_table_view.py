# The QTableView class provides a default model/view 
# implementation of a table view.
# Just as with QListView you need to provide the model yourself

import os
from random import randint
import sys

from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex
from PySide6.QtWidgets import (QApplication,
    QWidget, QVBoxLayout, QTableView, QHeaderView)


# 1 - So, create the model, in this case 
#     a QAbstractTableModel subclass. You must
#     implement rowCount(), columnCount() and data()
class RandomTableModel(QAbstractTableModel):
    
    def __init__(self):
        
        super().__init__()
        
        self.row_count = 3
        self.column_count = 5
        
        self.table = [[randint(0, 100) 
            for _ in range(self.column_count)] 
                for _ in range(self.row_count)]
                
    def rowCount(self, parent=QModelIndex()):
        return self.row_count
        
    def columnCount(self, parent=QModelIndex()):
        return self.column_count
        
    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        
        # This is where you actually provide the data
        
        if role == Qt.ItemDataRole.DisplayRole:
            i = index.row()
            j = index.column()
            return self.table[i][j]
        # I did not expect to have to set cell 
        # alignment in the model but hey.
        # Here's the available roles:
        # https://doc.qt.io/qt-6/qt.html#ItemDataRole-enum
        elif role == Qt.ItemDataRole.TextAlignmentRole:
            return Qt.AlignmentFlag.AlignCenter


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 2 - Create the table view
        
        table_view = QTableView()
        
        # 3 - Create the model instance and set it
        #     as the table view model.
        
        model = RandomTableModel()
        table_view.setModel(model)
        
        # Make the columns and rows fit the table view
        # size so there's no scrollbars
        
        table_view.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch)
            
        table_view.verticalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch)
        
        layout.addWidget(table_view)


if __name__ == '__main__':

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
