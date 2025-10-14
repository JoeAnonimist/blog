import csv
from PySide6.QtCore import QAbstractListModel, QModelIndex, Qt


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
        flags = Qt.ItemFlag.ItemIsSelectable | \
            Qt.ItemFlag.ItemIsEnabled | \
            Qt.ItemFlag.ItemIsEditable
        return flags
    
    def insertRows(self, row, count, parent=QModelIndex()):
        if 0 <= row <= self.rowCount():
            self.beginInsertRows(parent, row, row + count - 1)
            self.csv_data[row:row] = ['<insert row data>'] * count
            self.endInsertRows()
            return True
        else:
            return False
    
    def removeRows(self, row, count, parent=QModelIndex()):
        if 0 <= row < len(self.csv_data) and count > 0:
            end = row + count - 1
            if end >= len(self.csv_data):
                end = len(self.csv_data) - 1
            self.beginRemoveRows(parent, row, end)
            del self.csv_data[row:row + count]
            self.endRemoveRows()
            return True
        return False

    def headerData(self, section, orientation, role):
        if orientation == Qt.Orientation.Horizontal:
            if role == Qt.ItemDataRole.DisplayRole:
                return self.header
