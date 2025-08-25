import csv
import sys

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
from PySide6.QtTest import QAbstractItemModelTester
from PySide6.QtWidgets import (QApplication, QWidget,
    QTableView, QVBoxLayout, QPushButton)


class CsvModel(QAbstractTableModel):
    
    def __init__(self, source, parent=None):
        
        super().__init__(parent)
        
        self.csv_data = []
        with open(source) as csv_file:
            reader = csv.reader(csv_file)
            self.header = next(reader)
            for row in reader:
                self.csv_data.append(row)
                
    def rowCount(self, parent=QModelIndex()):
        return len(self.csv_data)
    
    def columnCount(self, parent=QModelIndex()):
        return 4
    
    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return self.csv_data[index.row()][index.column()]
        elif role == Qt.ItemDataRole.EditRole:
            return self.csv_data[index.row()][index.column()]

    # Editable models implement setData() and flags()
    
    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:
            if self.csv_data[index.row()][index.column()] != value:
                self.csv_data[index.row()][index.column()] = value
                self.dataChanged.emit(index, index)
                return True
            return False
        return False
    
    def flags(self, index):
        flags = Qt.ItemFlags.ItemIsSelectable | \
            Qt.ItemFlags.ItemIsEnabled | \
            Qt.ItemFlags.ItemIsEditable
        return flags
    
    def insertRows(self, row, count, parent=QModelIndex()):
        if 0 <= row <= self.rowCount():
            self.beginInsertRows(parent, row, row)
            self.csv_data.insert(row, ['', '', '', ''])
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

    # QTableView can have a header

    def headerData(self, section, orientation, role):
        if orientation == Qt.Orientation.Horizontal:
            if role == Qt.ItemDataRole.DisplayRole:
                return self.header[section]


class Window(QWidget):
    
    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.model = CsvModel('data.csv')
        QAbstractItemModelTester(self.model)
        self.view = QTableView()
        self.view.setModel(self.model)
        self.model.rowsInserted.connect(self.on_rows_inserted)
        self.view.resizeColumnsToContents()

        self.insert_button = QPushButton('Insert new')
        self.insert_button.clicked.connect(self.on_insert)
        
        self.append_button = QPushButton('Append new')
        self.append_button.clicked.connect(self.on_append)
        
        self.remove_button = QPushButton('Remove current')
        self.remove_button.clicked.connect(self.on_remove)
        
        layout.addWidget(self.view)
        layout.addWidget(self.insert_button)
        layout.addWidget(self.append_button)
        layout.addWidget(self.remove_button)
        
        self.model.dataChanged.connect(self.on_data_changed)
        
    def on_insert(self):
        row = self.view.selectionModel().currentIndex().row()
        self.model.insertRows(row, 1)
        
    def on_append(self):
        print('in on append')
        row = self.model.rowCount()
        self.model.insertRows(row, 1)
        index = self.model.index(row, 0)
        self.view.scrollTo(index)
    
    def on_remove(self):
        index = self.view.currentIndex()
        self.model.removeRows(index.row(), 1)
        
    def on_rows_inserted(self, parent, first, last):
        index = self.model.index(first, 0)
        if index.isValid():
            self.view.setCurrentIndex(index)
        
    def on_data_changed(self, topLeft, bottomRight, roles):
        print(f'Model changed, r: {topLeft.row()}, c: {topLeft.column()}')
        data = topLeft.model().data(topLeft, Qt.ItemDataRole.DisplayRole)
        print(f'Data: {data}')
           

if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())

