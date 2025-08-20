import sys

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt, QMetaType
from PySide6.QtWidgets import (QApplication, QWidget,
    QTableView, QVBoxLayout, QDial, QItemEditorFactory,
    QItemEditorCreatorBase)
from PySide6.QtTest import QAbstractItemModelTester

class CsvModel(QAbstractTableModel):
    
    def __init__(self, parent=None):
        
        super().__init__(parent)
        
        self.header = ['Indicator', 'Value'] 
        self.csv_data = [
            ['GDP (%)', 3],
            ['CPI (%)', 6],
            ['Jobs (%)', 5],
            ['Confidence', 75],
            ['Industry', 92],
            ['Retail (%)', 4],
        ]

    def rowCount(self, parent=QModelIndex()):
        return len(self.csv_data)
    
    def columnCount(self, parent=QModelIndex()):
        return len(self.header)
    
    def data(self, index, role):
        value = self.csv_data[index.row()][index.column()]
        if role == Qt.ItemDataRole.DisplayRole:
            return value
        if role == Qt.ItemDataRole.EditRole:
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
        flags = Qt.ItemFlags.ItemIsSelectable | \
            Qt.ItemFlags.ItemIsEnabled | \
            Qt.ItemFlags.ItemIsEditable
        return flags

    def headerData(self, section, orientation, role):
        if orientation == Qt.Orientation.Horizontal:
            if role == Qt.ItemDataRole.DisplayRole:
                return self.header[section]


class DialCreatorBase(QItemEditorCreatorBase):
    
    def createWidget(self, parent):
        dial = QDial(parent)
        dial.setMinimum(0)
        dial.setMaximum(100)
        return dial


class Window(QWidget):
    
    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        model = CsvModel()
        QAbstractItemModelTester(model)
        
        view = QTableView()
        view.verticalHeader().setDefaultSectionSize(60)
        view.setModel(model)
        
        delegate = view.itemDelegate()
        factory = QItemEditorFactory()
        factory.registerEditor(QMetaType.Type.Int, DialCreatorBase())
        
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
