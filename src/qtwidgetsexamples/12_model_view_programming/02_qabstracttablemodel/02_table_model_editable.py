import sys
import csv

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
from PySide6.QtWidgets import (QApplication,
    QWidget, QTableView, QVBoxLayout)
from PySide6.QtTest import QAbstractItemModelTester


# 1. Create a QAbstractTableModel subclass
#    same as in the read-only subclass example.

class CsvModel(QAbstractTableModel):
    
    def __init__(self, source, parent=None):
        
        super().__init__(parent)
        
        self.csv_data = []
        with open(source) as csv_file:
            reader = csv.reader(csv_file)
            self.header = next(reader)
            for row in reader:
                self.csv_data.append(row)

    # 2. Implement rowCount(), columnCount() and data()

    def rowCount(self, parent=QModelIndex()):
        return len(self.csv_data)
    
    def columnCount(self, parent=QModelIndex()):
        return 4
    
    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return self.csv_data[index.row()][index.column()]

    # 3. Implement setData() and flags()
    
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
        
        # 4. Use the model
        #    Create the model, create the view
        #    and assign the model to the view.

        model = CsvModel('data.csv')
        QAbstractItemModelTester(model)
        view = QTableView()
        view.setModel(model)
        view.resizeColumnsToContents()
        layout.addWidget(view)
        
        model.dataChanged.connect(self.on_data_changed)
        
    def on_data_changed(self, topLeft, bottomRight, roles):
        print(f'Model changed, r: {topLeft.row()}, c: {topLeft.column()}')
        data = topLeft.model().data(topLeft, Qt.ItemDataRole.DisplayRole)
        print(f'Data: {data}')


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())

