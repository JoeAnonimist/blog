import sys
import csv

from PySide6.QtCore import QAbstractListModel, Qt
from PySide6.QtWidgets import (QApplication,
    QWidget, QListView, QVBoxLayout)
from PySide6.QtTest import QAbstractItemModelTester


# 1. Create a QAbstractListModel subclass
#    and make the data available to it.

class CsvModel(QAbstractListModel):
    
    def __init__(self, source, parent=None):
        
        super().__init__(parent)
        
        self.csv_data = []
        with open(source) as csv_file:
            reader = csv.reader(csv_file)
            self.header = ', '.join(next(reader))
            for row in reader:
                self.csv_data.append(', '.join(row))
    
    # 2. Implement the rowCount() and the data() methods
    
    def rowCount(self, parent):
        return len(self.csv_data)
    
    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return self.csv_data[index.row()]
    
    # 3. Implement the setData() method
    
    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:
            if self.csv_data[index.row()] != value:
                self.csv_data[index.row()] = value
                self.dataChanged.emit(index, index)
                return True
            return False
        return False
    
    # 4. Implement the flags() method
    
    def flags(self, index):
        flags = Qt.ItemFlags.ItemIsSelectable | \
            Qt.ItemFlags.ItemIsEnabled | \
            Qt.ItemFlags.ItemIsEditable
        return flags
        
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

        model = CsvModel('data.csv')
        QAbstractItemModelTester(model)
        view = QListView()
        view.setModel(model)
        layout.addWidget(view)
        
        model.dataChanged.connect(self.on_data_changed)
    
    # Handle the dataChanged signals
    
    def on_data_changed(self, toplLeft, bottomRight, roles):
        print('Model changed, row:', toplLeft.row())


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())

