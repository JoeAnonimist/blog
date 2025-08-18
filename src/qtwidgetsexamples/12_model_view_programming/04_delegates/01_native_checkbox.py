import sys
import csv
from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt, QMetaType
from PySide6.QtWidgets import (QApplication, QWidget, QTableView, QVBoxLayout,
                               QItemEditorFactory, QItemEditorCreatorBase,
                               QSpinBox, QPushButton, QStyledItemDelegate, QMessageBox)

class CsvModel(QAbstractTableModel):

    def __init__(self, source, parent=None):
        
        super().__init__(parent)
        
        self.csv_data = []
        with open(source) as csv_file:
            reader = csv.reader(csv_file)
            self.header = next(reader)
            for row in reader:
                self.csv_data.append(
                    [row[0], int(row[1]), bool(int(row[2]))])

    def rowCount(self, parent=QModelIndex()):
        return len(self.csv_data)
    
    def columnCount(self, parent=QModelIndex()):
        return len(self.header)
    
    def data(self, index, role):
        value = self.csv_data[index.row()][index.column()]
        if role == Qt.ItemDataRole.DisplayRole:
            if not isinstance(value, bool):
                return value
        if role == Qt.ItemDataRole.EditRole:
            return value
        if role == Qt.ItemDataRole.CheckStateRole and isinstance(value, bool):
            return Qt.CheckState.Checked if value else Qt.CheckState.Unchecked
        if role == Qt.ItemDataRole.TextAlignmentRole and index.column() == 2:
            return Qt.AlignmentFlag.AlignCenter
        return None

    def setData(self, index, value, role):
        print(Qt.CheckState(value), Qt.Checked == (Qt.CheckState(value)), Qt.CheckState.Checked == (Qt.CheckState(value)))
        if role == Qt.ItemDataRole.EditRole:
            if self.csv_data[index.row()][index.column()] != value:
                self.csv_data[index.row()][index.column()] = value
                self.dataChanged.emit(index, index)
                return True
            return False
        if role == Qt.ItemDataRole.CheckStateRole:
            checked = Qt.CheckState(value) == Qt.CheckState.Checked
            self.csv_data[index.row()][index.column()] = checked
            return True
        return False
    
    def flags(self, index):
        flags = Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled
        if index.column() == 1:
            flags |= Qt.ItemFlag.ItemIsEditable
        if index.column() == 2:
            flags |= Qt.ItemFlag.ItemIsUserCheckable
        return flags

    def headerData(self, section, orientation, role):
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return self.header[section]
        return None


class Window(QWidget):
    def __init__(self, csv_file='01_data.csv'):
        super().__init__()
        layout = QVBoxLayout(self)
        
        self.model = CsvModel(csv_file)
        self.view = QTableView()
        self.view.setModel(self.model)
        self.view.resizeColumnsToContents()
        
        layout.addWidget(self.view)
        
        self.model.dataChanged.connect(self.on_data_changed)
    
    def on_data_changed(self, topLeft, bottomRight, roles):
        print(f'Model changed, r: {topLeft.row()}, c: {topLeft.column()}')
        if Qt.ItemDataRole.CheckStateRole in roles and topLeft.column() == 2:
            data = topLeft.model().data(topLeft, Qt.ItemDataRole.CheckStateRole)
            print(f'CheckState: {"Checked" if data == Qt.CheckState.Checked else "Unchecked"}')
        else:
            data = topLeft.model().data(topLeft, Qt.ItemDataRole.EditRole)
            print(f'Data: {data}')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window('01_data.csv')
    main_window.show()
    sys.exit(app.exec())