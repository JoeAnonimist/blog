import sys

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt, QSortFilterProxyModel
from PySide6.QtWidgets import (QApplication, QWidget,
    QLineEdit, QTableView, QVBoxLayout)
from PySide6.QtTest import QAbstractItemModelTester


class CsvModel(QAbstractTableModel):
    
    def __init__(self, parent=None):
        
        super().__init__(parent)
        
        self.header = ['Indicator', 'Description']
        self.csv_data = [
            ['GDP', 'Measures total economic output'],
            ['CPI', 'Tracks consumer price changes'],
            ['Jobs', 'Employment level indicator'],
            ['Confidence', 'Consumer sentiment index'],
            ['Industry', 'Manufacturing activity gauge'],
            ['Retail', 'Consumer spending on goods'],
            ['Unemployment', 'Percentage of jobless workforce'],
            ['Inflation', 'Rate of price increase'],
            ['PPI', 'Producer price index'],
            ['Trade Balance', 'Export minus import value']
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
            return value
    
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

    def headerData(self, section, orientation, role):
        if orientation == Qt.Orientation.Horizontal:
            if role == Qt.ItemDataRole.DisplayRole:
                return self.header[section]


class Window(QWidget):
    
    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        model = CsvModel()
        QAbstractItemModelTester(model)
        
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSortCaseSensitivity(
            Qt.CaseSensitivity.CaseInsensitive)
        self.proxy_model.setSourceModel(model)
        
        view = QTableView()
        view.setModel(self.proxy_model)
        
        view.setSortingEnabled(True)
        
        view.resizeColumnsToContents()
        layout.addWidget(view)
        
        filter_edit = QLineEdit()
        
        self.proxy_model.setFilterKeyColumn(1)
        self.proxy_model.setFilterCaseSensitivity(
            Qt.CaseSensitivity.CaseInsensitive)
        
        filter_edit.textChanged.connect(self.on_text_changed)
        layout.addWidget(filter_edit)
        
    def on_text_changed(self, text):
        self.proxy_model.setFilterRegularExpression(text)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())

