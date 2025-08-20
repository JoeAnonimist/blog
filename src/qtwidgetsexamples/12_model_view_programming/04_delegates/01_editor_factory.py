import sys
import csv

from PySide6.QtCore import (QAbstractTableModel,
    QModelIndex, Qt, QMetaType)
from PySide6.QtWidgets import (QApplication, QWidget,
    QTableView, QVBoxLayout, QItemEditorFactory,
    QItemEditorCreatorBase, QCheckBox)


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
            return value
        if role == Qt.ItemDataRole.EditRole:
            print(value)
            return value

    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:
            if self.csv_data[index.row()][index.column()] != value:
                self.csv_data[index.row()][index.column()] = value
                self.dataChanged.emit(index, index)
                return True
            return False
        return False
    
    def flags(self, index):
        flags = Qt.ItemFlags.ItemIsSelectable
        if index.column() != 0:
            flags = flags | Qt.ItemFlags.ItemIsEnabled | \
                            Qt.ItemFlags.ItemIsEditable 
        return flags

    def headerData(self, section, orientation, role):
        if orientation == Qt.Orientation.Horizontal:
            if role == Qt.ItemDataRole.DisplayRole:
                return self.header[section]

class BoolEditorCreator(QItemEditorCreatorBase):
        
    def createWidget(self, parent):
        editor = QCheckBox(parent)
        editor.setAutoFillBackground(True)
        return editor
    
    def valuePropertyName(self):
        return b'checked'


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
        factory.registerEditor(QMetaType(QMetaType.Type.Bool).id(), BoolEditorCreator())
        
        delegate = view.itemDelegate()
        delegate.setItemEditorFactory(factory)
        
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

