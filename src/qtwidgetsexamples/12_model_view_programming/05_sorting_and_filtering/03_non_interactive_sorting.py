import sys

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt, QItemSelectionModel
from PySide6.QtWidgets import (QApplication, QWidget,
    QTableView, QVBoxLayout, QPushButton)
from PySide6.QtTest import QAbstractItemModelTester


class CsvModel(QAbstractTableModel):
    
    def __init__(self, parent=None):
        
        super().__init__(parent)
        
        self.header = ['Indicator', 'Value (%)', 
            'Aggregate', 'Include in report']
        self.csv_data = [
            ['GDP', 3, 1, True],
            ['CPI', 6, 1, True],
            ['Jobs', 5, 0, True],
            ['Confidence', 75, 0, True],
            ['Industry', 92, 0, True],
            ['Retail', 4, 1, True],
        ]

    def rowCount(self, parent=QModelIndex()):
        return len(self.csv_data)
    
    def columnCount(self, parent=QModelIndex()):
        return len(self.header)
    
    def data(self, index, role):
        
        value = self.csv_data[index.row()][index.column()]

        if role == Qt.ItemDataRole.DisplayRole:
            return value
        if role == Qt.ItemDataRole.EditRole:
            if index.column() == 2:
                return value == 1
            else:
                return value
    
    def setData(self, index, value, role):
        
        if role == Qt.ItemDataRole.EditRole:
            if index.column() == 2:
                value = 1 if value else 0
            if self.csv_data[index.row()][index.column()] != value:
                self.csv_data[index.row()][index.column()] = value
                self.dataChanged.emit(index, index)
                if index.column() == 0:
                    self.sort(0)
                return True
            return False
        return False

    def sort(self, column, order=Qt.SortOrder.AscendingOrder):
        
        self.layoutAboutToBeChanged.emit()
        self.csv_data.sort(
            key=lambda row: row[0].lower(),
            reverse=(order == Qt.SortOrder.DescendingOrder)
        )
        self.layoutChanged.emit()
        
        for row in self.csv_data:
            print(row)
        print('----------------------------')
    
    def flags(self, index):
        flags = Qt.ItemFlags.ItemIsSelectable | \
            Qt.ItemFlags.ItemIsEnabled | \
            Qt.ItemFlags.ItemIsEditable
        return flags
    
    def insertRows(self, row, count, parent=QModelIndex()):
        if 0 <= row <= self.rowCount():
            self.beginInsertRows(parent, row, row)
            self.csv_data.insert(row, ['', 0, 0, True])
            self.endInsertRows()
            return True
        else:
            return False
        
    def removeRows(self, row, count, parent=QModelIndex()):
        if 0 <= row < len(self.csv_data):
            self.beginRemoveRows(parent, row, row)
            self.csv_data[row:row + 1] = []
            self.endRemoveRows()
            return True
        else:
            return False

    def headerData(self, section, orientation, role):
        if orientation == Qt.Orientation.Horizontal:
            if role == Qt.ItemDataRole.DisplayRole:
                return self.header[section]


class Window(QWidget):
    
    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.model = CsvModel()
        self.model.sort(0, Qt.SortOrder.AscendingOrder)
        QAbstractItemModelTester(self.model)
        
        self.view = QTableView()
        self.view.setModel(self.model)

        self.view.resizeColumnsToContents()
        layout.addWidget(self.view)
        
        self.insert_button = QPushButton('Insert new')
        self.insert_button.clicked.connect(self.on_insert)
        
        self.append_button = QPushButton('Append new')
        self.append_button.clicked.connect(self.on_append)
        
        self.remove_button = QPushButton('Remove current')
        self.remove_button.clicked.connect(self.on_remove)
        
        layout.addWidget(self.insert_button)
        layout.addWidget(self.append_button)
        layout.addWidget(self.remove_button)
        
    def on_insert(self):
        row = self.view.selectionModel().currentIndex().row()
        self.model.insertRows(row, 1)
        
    def on_append(self):
        row = self.model.rowCount()
        self.model.insertRows(row, 1)
        index = self.model.index(row, 0)
        self.view.scrollTo(index)
        #self.view.selectionModel().select(index, QItemSelectionModel.SelectionFlag.ClearAndSelect | QItemSelectionModel.SelectionFlag.Rows)
    
    def on_remove(self):
        index = self.view.currentIndex()
        self.model.removeRows(index.row(), 1)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())

