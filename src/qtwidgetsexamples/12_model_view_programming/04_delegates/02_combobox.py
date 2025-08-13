import sys
import csv

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import (QApplication,
    QWidget, QTableView, QVBoxLayout, QStyledItemDelegate, QComboBox)


class CsvModel(QAbstractTableModel):
    
    def __init__(self, source, parent=None):
        
        super().__init__(parent)
        
        self.csv_data = []
        with open(source) as csv_file:
            reader = csv.reader(csv_file)
            self.header = next(reader)
            for row in reader:
                row[1] = int(row[1])
                self.csv_data.append(row)

    def rowCount(self, parent=QModelIndex()):
        return len(self.csv_data)
    
    def columnCount(self, parent=QModelIndex()):
        return len(self.header)
    
    def data(self, index, role):
        
        if role == Qt.ItemDataRole.DisplayRole:
            if index.column() == 1:
                return Qt.AnchorPoint(self.csv_data[index.row()][1]).name
            else:
                return self.csv_data[index.row()][index.column()]
        
        if role == Qt.ItemDataRole.EditRole:
            return self.csv_data[index.row()][index.column()]

    def setData(self, index, value, role):
        
        if role == Qt.ItemDataRole.EditRole:
            if self.csv_data[index.row()][index.column()] != value:
                self.csv_data[index.row()][index.column()] = value
                self.dataChanged.emit(index, index)
    
                for row in self.csv_data:
                    print(row)
                return True
        return False

    def flags(self, index):
        flags = Qt.ItemFlags.ItemIsSelectable | \
            Qt.ItemFlags.ItemIsEnabled | \
            Qt.ItemFlags.ItemIsEditable
        return flags

    def headerData(self, section, orientation, role):
        if orientation == Qt.Orientation.Horizontal:
            if role == Qt.ItemDataRole.DisplayRole:
                return self.header[section]


class ComboBoxDelegate(QStyledItemDelegate):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        data = [(point.name, point.value) for point in Qt.AnchorPoint]
        self.combobox_model = QStandardItemModel()
        
        for name, value in data:
            name_item = QStandardItem(name)
            name_item.setData(name, Qt.ItemDataRole.UserRole)
            value_item = QStandardItem(value)
            value_item.setData(value, Qt.ItemDataRole.UserRole)
            self.combobox_model.appendRow([name_item, value_item])        
        
    def createEditor(self, parent, option, index):
        
        editor = QComboBox(parent)
        editor.setFrame(False)
        
        editor.setModel(self.combobox_model)
        editor.setModelColumn(0)
        
        return editor
    
    def setEditorData(self, editor, index):

        current_value = index.model().data(
            index, Qt.ItemDataRole.EditRole)

        for row in range(self.combobox_model.rowCount()):
            item = self.combobox_model.item(row, 0)
            if item.data(Qt.ItemDataRole.UserRole) == current_value:
                editor.setCurrentIndex(row)
                break

        
    def setModelData(self, editor, model, index):
        item = self.combobox_model.item(editor.currentIndex(), 1)
        value = item.data(Qt.ItemDataRole.UserRole)
        model.setData(index, value, Qt.ItemDataRole.EditRole)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        model = CsvModel('02_data.csv')
        
        view = QTableView()
        view.setModel(model)
        view.resizeColumnsToContents()
        
        delegate = ComboBoxDelegate()
        view.setItemDelegateForColumn(1, delegate)
        
        layout.addWidget(view)
        
        #model.dataChanged.connect(self.on_data_changed)
        
    def on_data_changed(self, topLeft, bottomRight, roles):
        print(f'Model changed, r: {topLeft.row()}, c: {topLeft.column()}')
        data = topLeft.model().data(topLeft, Qt.ItemDataRole.DisplayRole)
        print(f'Data: {data} in row: {topLeft.model().csv_data[topLeft.row()]}')



if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())

