import sys

from PySide6.QtCore import (QAbstractTableModel, QModelIndex,
    Qt, QMetaType, Property)
from PySide6.QtWidgets import (QApplication, 
    QRadioButton, QWidget, QTableView, QVBoxLayout, 
    QItemEditorFactory, QHBoxLayout, QStyledItemDelegate,
    QItemEditorCreatorBase)
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


class SwitchWidget(QWidget):
    
    def __init__(self, parent=None):
        
        super().__init__(parent)
        
        self._value = False
        
        self.true_radio = QRadioButton('Yes')
        self.false_radio = QRadioButton('No')
        self.true_radio.toggled.connect(self.on_toggled)
        
        layout = QHBoxLayout()
        layout.addWidget(self.true_radio)
        layout.addWidget(self.false_radio)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        self.setMinimumHeight(self.sizeHint().height())
        
    def on_toggled(self, checked):
        self.setValue(checked)
        
    def getValue(self):
        return self._value
    
    def setValue(self, value):
        if value != self._value:
            self._value = value
        if value:
            self.true_radio.setChecked(True)
        else:
            self.false_radio.setChecked(True)
        
    value = Property(bool, getValue, setValue, user=True)    


class SwitchCreator(QItemEditorCreatorBase):
    
    def createWidget(self, parent):
        
        editor = SwitchWidget(parent)

        # If we don't implement valuePropertyName()
        # the widget's user property is used (in this case 'value')
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
        factory.registerEditor(
            QMetaType.Type.Bool, SwitchCreator())
        
        delegate = QStyledItemDelegate()
        delegate.setItemEditorFactory(factory)
        
        view = QTableView()
        view.setModel(model)
        
        view.setItemDelegateForColumn(3, delegate)
        
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

