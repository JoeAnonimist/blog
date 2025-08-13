import sys
import csv

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt, Property, Signal
from PySide6.QtWidgets import (QApplication,
    QWidget, QTableView, QVBoxLayout, QStyledItemDelegate,
    QSlider, QLabel, QHBoxLayout)


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
        if (role == Qt.ItemDataRole.DisplayRole or
            role == Qt.ItemDataRole.EditRole):
            return self.csv_data[index.row()][index.column()]
    
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


class Editor(QWidget):
    
    valueChanged = Signal(int)
    
    def __init__(self, parent):
        
        super().__init__(parent)
        self.setAutoFillBackground(True)
        
        self.label = QLabel()
        self.label.setFixedWidth(20)
        
        self.slider = QSlider(Qt.Orientation.Horizontal, parent)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.valueChanged.connect(self.on_value_changed)
        
        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.label)
        self.layout().addWidget(self.slider)
        self.layout().addStretch()
        
        self.layout().setContentsMargins(2, 0, 2, 0)
        
    def on_value_changed(self, value):
        print('in value changed')
        self.label.setText(str(value))
        
    def getValue(self):
        return self.slider.value()
    
    def setValue(self, value):
        if value != self.slider.value():
            self.slider.setValue(value)
            self.valueChanged.emit(value)

    value = Property(int, getValue, setValue, notify=valueChanged)


class SpinBoxDelegate(QStyledItemDelegate):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
    def createEditor(self, parent, option, index):
        editor = Editor(parent)
        print(option, option.rect)
        editor.setGeometry(option.rect)
        return editor
    
    def setEditorData(self, editor, index):
        value = index.model().data(
            index, Qt.ItemDataRole.EditRole) 
        editor.setValue(value)
        
    def setModelData(self, editor, model, index):
        value = editor.value
        model.setData(index, value, Qt.ItemDataRole.EditRole)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        model = CsvModel('03_data.csv')
        
        view = QTableView()
        view.setModel(model)
        view.resizeColumnsToContents()
        view.setColumnWidth(1, 120)
        
        delegate = SpinBoxDelegate()
        view.setItemDelegateForColumn(1, delegate)
        
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

