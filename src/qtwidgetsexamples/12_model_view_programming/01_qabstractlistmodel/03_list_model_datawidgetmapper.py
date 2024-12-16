import sys
import csv

from PySide6.QtCore import QAbstractListModel, Qt
from PySide6.QtWidgets import (QApplication,
    QWidget, QListView, QLineEdit, QPushButton,
    QHBoxLayout, QVBoxLayout, QDataWidgetMapper)
from PySide6.QtTest import QAbstractItemModelTester


# 1. Create the model class

class CsvModel(QAbstractListModel):
    
    def __init__(self, source, parent=None):
        
        super().__init__(parent)
        
        self.csv_data = []
        with open(source) as csv_file:
            reader = csv.reader(csv_file)
            self.header = ', '.join(next(reader))
            for row in reader:
                self.csv_data.append(', '.join(row))
                
    def rowCount(self, parent):
        return len(self.csv_data)
    
    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return self.csv_data[index.row()]
        elif role == Qt.ItemDataRole.EditRole:
            return self.csv_data[index.row()]

    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:
            if self.csv_data[index.row()] != value:
                self.csv_data[index.row()] = value
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
                return self.header

class Window(QWidget):
    
    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.model = CsvModel('data.csv')
        QAbstractItemModelTester(self.model)
        
        self.view = QListView()
        self.view.setModel(self.model)
        self.view.selectionModel().currentChanged.connect(
            self.on_current_changed)
        
        # 2. Create the widgets for displaying
        #    and editing the data
        
        self.lineedit = QLineEdit()
        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.on_submit)
        
        # 3. Create the mapper object and set its model
        
        self.mapper = QDataWidgetMapper()
        self.mapper.setModel(self.model)
        
        # 4. Add the mappings

        self.mapper.addMapping(self.lineedit, 0)
        
        self.mapper.setSubmitPolicy(
            QDataWidgetMapper.SubmitPolicy.ManualSubmit)
        self.mapper.toFirst()
        
        horizontal_layout = QHBoxLayout()
        horizontal_layout.addWidget(self.lineedit)
        horizontal_layout.addWidget(self.submit_button)
        
        layout.addWidget(self.view)
        layout.addLayout(horizontal_layout)
    
    # 5. Synchronize 
    
    def on_current_changed(self, current, previous):
        self.mapper.setCurrentIndex(current.row())
        
    def on_submit(self):
        self.mapper.submit()


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())

