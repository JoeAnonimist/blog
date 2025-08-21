import sys

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
from PySide6.QtGui import QColor, QBrush, QFont
from PySide6.QtWidgets import (QApplication,
    QWidget, QTableView, QVBoxLayout)
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
        
        self.plus_brush = QBrush(QColor("#d9fdd3"))
        self.minus_brush = QBrush(QColor("#fce4e4"))

    def rowCount(self, parent=QModelIndex()):
        return len(self.csv_data)
    
    def columnCount(self, parent=QModelIndex()):
        return len(self.header) - 1
    
    def data(self, index, role):
        
        value = self.csv_data[index.row()][index.column()]

        if role == Qt.ItemDataRole.DisplayRole:
            if index.column() == 2:
                return 'YES' if value == 1 else 'NO'
            return value
        if role == Qt.ItemDataRole.EditRole:
            if index.column() == 2:
                return value == 1
            else:
                return value
            
        if role == Qt.ItemDataRole.CheckStateRole:
            if index.column() == 0:
                if self.csv_data[index.row()][3]:
                    return Qt.CheckState.Checked
                else:
                    return Qt.CheckState.Unchecked

        if role == Qt.ItemDataRole.BackgroundRole:
            if index.column() in(1, 2):
                if value > 0:
                    return self.plus_brush
                else:
                    return self.minus_brush

        if role == Qt.ItemDataRole.FontRole:
            if index.column() in (1, 2):
                font = QFont()
                if value <= 0:
                    font.setItalic(True)
                return font
                
        if role == Qt.ItemDataRole.TextAlignmentRole:
            alignment = Qt.AlignmentFlag.AlignVCenter
            if index.column() in (1, 2):
                if value <= 0:
                    alignment |= Qt.AlignmentFlag.AlignRight 
                else:
                    alignment |= Qt.AlignmentFlag.AlignCenter
            return alignment
    
    def setData(self, index, value, role):
        
        if role == Qt.ItemDataRole.EditRole:
            if index.column() == 2:
                value = 1 if value else 0
            if self.csv_data[index.row()][index.column()] != value:
                self.csv_data[index.row()][index.column()] = value
                self.dataChanged.emit(index, index)
                return True
            return False
        
        if role == Qt.ItemDataRole.CheckStateRole:
            if index.column() == 0:
                if value:
                    self.csv_data[index.row()][self.columnCount()] = True
                else:
                    self.csv_data[index.row()][self.columnCount()] = False
                self.dataChanged.emit(index, index)
                return True
            return False
        
        return False
    
    def flags(self, index):
        flags = Qt.ItemFlags.ItemIsSelectable | \
            Qt.ItemFlags.ItemIsEnabled | \
            Qt.ItemFlags.ItemIsEditable
        if index.column() == 0:
            flags |= Qt.ItemFlags.ItemIsUserCheckable
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
        view = QTableView()
        view.setModel(model)
        view.resizeColumnsToContents()
        layout.addWidget(view)
        
        model.dataChanged.connect(self.on_data_changed)
        
    def on_data_changed(self, topLeft, bottomRight, roles):
        for row in topLeft.model().csv_data:
            print(row)

if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())

