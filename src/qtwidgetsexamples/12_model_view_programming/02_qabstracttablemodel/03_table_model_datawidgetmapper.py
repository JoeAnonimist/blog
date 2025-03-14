import sys
import csv

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
from PySide6.QtWidgets import (QApplication, QWidget,
    QTableView, QVBoxLayout, QFormLayout, QDataWidgetMapper,
    QLineEdit, QPushButton)
from PySide6.QtTest import QAbstractItemModelTester


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
        self.view.selectionModel().currentChanged.connect(
            self.on_current_changed)
        self.view.resizeColumnsToContents()
        
        self.fname_edit = QLineEdit()
        self.lname_edit = QLineEdit()
        self.prof_edit = QLineEdit()
        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.on_submit)
        
        self.mapper = QDataWidgetMapper()
        self.mapper.setModel(self.model)
        self.mapper.setSubmitPolicy(
            QDataWidgetMapper.SubmitPolicy.ManualSubmit)
        
        self.mapper.addMapping(self.fname_edit, 1)
        self.mapper.addMapping(self.lname_edit, 2)
        self.mapper.addMapping(self.prof_edit, 3)
        self.mapper.toFirst()
        
        form_layout = QFormLayout()
        form_layout.addWidget(self.fname_edit)
        form_layout.addWidget(self.lname_edit)
        form_layout.addWidget(self.prof_edit)
        form_layout.addWidget(self.submit_button)
        
        layout.addWidget(self.view)
        layout.addLayout(form_layout)
        
        self.model.dataChanged.connect(self.on_data_changed)
        
    def on_submit(self):
        self.mapper.submit()
        
    def on_current_changed(self, current, previous):
        self.mapper.setCurrentIndex(current.row())
        
    def on_data_changed(self, topLeft, bottomRight, roles):
        print(f'Model changed, r: {topLeft.row()}, c: {topLeft.column()}')
        data = topLeft.model().data(topLeft, Qt.ItemDataRole.DisplayRole)
        print(f'Data: {data}')
           

if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())

