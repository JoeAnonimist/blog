import sys

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt, QMetaType
from PySide6.QtWidgets import (QApplication, QSlider,
    QWidget, QTableView, QVBoxLayout, QItemEditorFactory,
    QStyledItemDelegate, QItemEditorCreatorBase)
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

    def rowCount(self, parent=QModelIndex()):
        return len(self.csv_data)
    
    def columnCount(self, parent=QModelIndex()):
        return len(self.header)
    
    def data(self, index, role):
        
        value = self.csv_data[index.row()][index.column()]

        if role == Qt.ItemDataRole.DisplayRole:
            return value
        if role == Qt.ItemDataRole.EditRole:
            if index.column() == 2:
                return value == 1
            else:
                return value
    
    def setData(self, index, value, role):
        
        if role == Qt.ItemDataRole.EditRole:
            if index.column() == 2:
                value = 1 if value else 0
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

class SliderCreator(QItemEditorCreatorBase):
    
    def __init__(self, min_width):
        super().__init__()
        self.min_width = min_width
    
    def createWidget(self, parent):
        
        editor = QSlider(parent)
        editor.setAutoFillBackground(True)
        
        editor.setMinimum(-100)
        editor.setMaximum(100)
        
        editor.setOrientation(Qt.Orientation.Horizontal)
        editor.setMinimumWidth(self.min_width)
        
        # If we don't implement valuePropertyName()
        # the widget's user property is used
        # (in this case 'value')
        print(editor.metaObject().userProperty().name())
        
        return editor


class Window(QWidget):
    
    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        model = CsvModel()
        QAbstractItemModelTester(model)
        
        factory = QItemEditorFactory()
        min_width = 100
        factory.registerEditor(
            QMetaType.Type.Int, SliderCreator(min_width))
        
        delegate = QStyledItemDelegate()
        delegate.setItemEditorFactory(factory)
        
        view = QTableView()
        view.setModel(model)
        
        view.setItemDelegateForColumn(1, delegate)
        
        view.resizeColumnsToContents()
        view.setColumnWidth(1, min_width + 10)
        
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

