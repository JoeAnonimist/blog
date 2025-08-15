
import sys
import csv

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt, QMetaType
from PySide6.QtGui import QBrush
from PySide6.QtWidgets import (QApplication, QPushButton,
QWidget, QTableView, QVBoxLayout, QItemEditorCreatorBase, QItemEditorFactory)


class CsvModel(QAbstractTableModel):
    def __init__(self, source, parent=None):
        super().__init__(parent)
        self.csv_data = []
        with open(source) as csv_file:
            reader = csv.reader(csv_file)
            self.header = next(reader)
            for row in reader:
                row[1] = int(row[1])
                self.csv_data.append(
                    [row[0], int(row[1]), bool(int(row[2]))])

    def rowCount(self, parent=QModelIndex()):
        return len(self.csv_data)
    
    def columnCount(self, parent=QModelIndex()):
        return len(self.header)

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if index.column() == 2:
                if self.csv_data[index.row()][index.column()] == 0:
                    return 'Yes'
                else:
                    return 'No'
            else:
                return self.csv_data[index.row()][index.column()]
        if role == Qt.ItemDataRole.EditRole:
            return self.csv_data[index.row()][index.column()]
        if role == Qt.ItemDataRole.BackgroundRole:
            if index.column() == 2:
                if self.csv_data[index.row()][index.column()] == 0:
                    brush = QBrush(Qt.GlobalColor.green)
                    return brush
                else:
                    brush = QBrush(Qt.GlobalColor.red)
                    return brush
        if role == Qt.ItemDataRole.TextAlignmentRole:
            if index.column() == 2:
                return Qt.AlignmentFlag.AlignCenter
    
    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:
            if self.csv_data[index.row()][index.column()] != value:
                self.csv_data[index.row()][index.column()] = value
                self.dataChanged.emit(index, index)
                print(self.csv_data)
                return True
            return False
        return False

    def flags(self, index):
        if index.column() == 0:
            flags = Qt.ItemFlags.ItemIsSelectable
        else:
            flags = Qt.ItemFlags.ItemIsSelectable | \
            Qt.ItemFlags.ItemIsEnabled | \
            Qt.ItemFlags.ItemIsEditable
        return flags
    
    def headerData(self, section, orientation, role):
        if orientation == Qt.Orientation.Horizontal:
            if role == Qt.ItemDataRole.DisplayRole:
                return self.header[section]


class BoolEditorCreator(QItemEditorCreatorBase):

    def createWidget(self, parent):
        self.button = QPushButton(parent)
        self.button.setCheckable(True)
        self.button.clicked.connect(self.on_clicked)
        return self.button

    def valuePropertyName(self):
        return b'checked'
    
    def on_clicked(self, checked):
        if checked:
            self.button.setText('YES')
        else:
            self.button.setText('NO')


class Window(QWidget):

    def __init__(self):
        
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        model = CsvModel('01_data.csv')
        view = QTableView()
        view.setModel(model)
        view.resizeColumnsToContents()
        factory = QItemEditorFactory()
        factory.registerEditor(QMetaType.Type.Bool, BoolEditorCreator())
        delegate = view.itemDelegate()
        delegate.setItemEditorFactory(factory)
        layout.addWidget(view)
        model.dataChanged.connect(self.on_data_changed)
        
    def on_data_changed(self, topLeft, bottomRight, roles):
        print(f'Model changed, r: {topLeft.row()}, c: {topLeft.column()}')
        data = topLeft.model().data(topLeft, Qt.ItemDataRole.DisplayRole)
        print(f'Data: {data} in row: {topLeft.model().csv_data[topLeft.row()]}')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    
    main_window = Window()
    main_window.show()
    
    sys.exit(app.exec())

