import sys
import csv

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
from PySide6.QtWidgets import (QApplication,
    QWidget, QTableView, QVBoxLayout)
from PySide6.QtTest import QAbstractItemModelTester


# 1. Create a QAbstractTableModel subclass.
#    We read the data from a csv file using Python's csv.reader
#    Each row in a reader object is a list making self.csv_data
#    a two-dimensional list suitable for use
#    with QAbstractTableModel.

class CsvModel(QAbstractTableModel):
    
    def __init__(self, source, parent=None):
        
        super().__init__(parent)
        
        self.csv_data = []
        with open(source) as csv_file:
            reader = csv.reader(csv_file)
            self.header = next(reader)
            for row in reader:
                self.csv_data.append(row)

    # 2. Implement the rowCount() and columnCount() methods

    def rowCount(self, parent=QModelIndex()):
        return len(self.csv_data)

    def columnCount(self, parent=QModelIndex()):
        return 4
    
    # 3. Implement the data() method
    
    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return self.csv_data[index.row()][index.column()]
        
    # QTableView can have a header
    # but implementing headerData() is still optional.

    def headerData(self, section, orientation, role):
        if orientation == Qt.Orientation.Horizontal:
            if role == Qt.ItemDataRole.DisplayRole:
                return self.header[section]

class Window(QWidget):
    
    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 4. Use the model:
        #    Create a model instance, create a view instance
        #    and and use view.setModel() to connect them.

        model = CsvModel('data.csv')
        QAbstractItemModelTester(model)
        
        view = QTableView()
        view.setModel(model)
        view.resizeColumnsToContents()
        layout.addWidget(view)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())

