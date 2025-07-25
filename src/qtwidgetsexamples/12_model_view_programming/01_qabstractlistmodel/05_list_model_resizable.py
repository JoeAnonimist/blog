import sys
import csv

from PySide6.QtCore import QAbstractListModel, QModelIndex, Qt
from PySide6.QtWidgets import (QApplication,
    QWidget, QListView, QLineEdit, QPushButton,
    QHBoxLayout, QVBoxLayout, QDataWidgetMapper)
from PySide6.QtTest import QAbstractItemModelTester


class CsvModel(QAbstractListModel):
    
    def __init__(self, source, parent=None):
        
        super().__init__(parent)
        
        self.csv_data = []
        with open(source) as csv_file:
            reader = csv.reader(csv_file)
            self.header = ', '.join(next(reader))
            for row in reader:
                self.csv_data.append(', '.join(row))
                
    def rowCount(self, parent=QModelIndex()):
        return len(self.csv_data)
    
    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole \
        or role == Qt.ItemDataRole.EditRole:
            return self.csv_data[index.row()]
    
    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:
            if self.csv_data[index.row()] != value:
                self.csv_data[index.row()] = value
                self.dataChanged.emit(index, index)
                return True
        else:
            return False
    
    def flags(self, index):
        flags = Qt.ItemFlags.ItemIsSelectable | \
            Qt.ItemFlags.ItemIsEnabled | \
            Qt.ItemFlags.ItemIsEditable
        return flags
    
    def insertRows(self, row, count, parent=QModelIndex()):
        if 0 <= row <= self.rowCount():
            self.beginInsertRows(parent, row, row)
            self.csv_data.insert(row, '')
            self.endInsertRows()
            return True
        else:
            return False

    def removeRows(self, row, count, parent=QModelIndex()):
        if 0 <= row < len(self.csv_data):
            self.beginRemoveRows(parent, row, row + 1)
            self.csv_data[row:row + 1] = []
            self.endRemoveRows()
            return True
        else:
            return False

    # QListView does not have a header
    # so this is never executed!

    def headerData(self, section, orientation, role):
        if orientation == Qt.Orientation.Horizontal:
            if role == Qt.ItemDataRole.DisplayRole:
                return self.header

class Window(QWidget):
    
    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.model = CsvModel('data.csv')
        QAbstractItemModelTester(self.model)
        self.model.rowsInserted.connect(self.on_rows_inserted)
        
        self.view = QListView()
        self.view.setModel(self.model)
        self.view.selectionModel().currentChanged.connect(
            self.on_current_changed)
        
        self.lineedit = QLineEdit()

        self.mapper = QDataWidgetMapper()
        self.mapper.setModel(self.model)
        self.mapper.setSubmitPolicy(
            QDataWidgetMapper.SubmitPolicy.ManualSubmit)
        self.mapper.addMapping(self.lineedit, 0)
        self.mapper.toFirst()
        
        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.on_submit)
        
        self.insert_button = QPushButton('Insert new')
        self.insert_button.clicked.connect(self.on_insert)
        
        self.append_button = QPushButton('Append new')
        self.append_button.clicked.connect(self.on_append)
        
        self.remove_button = QPushButton('Remove current')
        self.remove_button.clicked.connect(self.on_remove)

        input_layout = QVBoxLayout()
        input_layout.addWidget(self.lineedit)
        input_layout.addWidget(self.submit_button)

        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(self.insert_button)
        buttons_layout.addWidget(self.append_button)
        buttons_layout.addWidget(self.remove_button)

        controls_layout = QHBoxLayout()
        controls_layout.addLayout(input_layout)
        controls_layout.addLayout(buttons_layout)

        layout.addWidget(self.view)
        layout.addLayout(controls_layout)
        
    def on_current_changed(self, current, previous):
        self.mapper.setCurrentIndex(current.row())
        
    def on_submit(self):
        self.mapper.submit()
        
    def on_insert(self):
        row = self.view.selectionModel().currentIndex().row()
        if self.model.insertRows(row, 1):
            self.mapper.setCurrentIndex(row)
        
    def on_append(self):
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


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
