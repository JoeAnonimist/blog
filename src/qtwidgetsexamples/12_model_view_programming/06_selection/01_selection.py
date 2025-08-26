import sys
from random import randint

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
from PySide6.QtWidgets import (QApplication, QWidget,
    QTableView, QVBoxLayout, QHBoxLayout, QLabel)
from PySide6.QtTest import QAbstractItemModelTester


class RandomModel(QAbstractTableModel):
    
    def __init__(self, parent=None):
        
        super().__init__(parent)
        
        self.random_data = []
        for _ in range(6):
            row = []
            for _ in range(6):
                row.append(randint(0, 100))
            self.random_data.append(row)


    def rowCount(self, parent=QModelIndex()):
        return 6

    def columnCount(self, parent=QModelIndex()):
        return 6
    
    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None
        if role == Qt.ItemDataRole.DisplayRole:
            return self.random_data[index.row()][index.column()]
        if role == Qt.ItemDataRole.TextAlignmentRole:
            return Qt.AlignmentFlag.AlignCenter

    def headerData(self, section, orientation, role):
        if orientation == Qt.Orientation.Horizontal:
            if role == Qt.ItemDataRole.DisplayRole:
                return 'C' + str(section)
        if orientation == Qt.Orientation.Vertical:
            if role == Qt.ItemDataRole.DisplayRole:
                return 'R' + str(section)

class Window(QWidget):
    
    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.model = RandomModel()
        QAbstractItemModelTester(self.model)
        
        self.view = QTableView()
        self.view.setModel(self.model)
        
        self.current_item = QLabel('Current: None')
        self.selection_sum = QLabel('Selection sum: 0')
        self.cumulative_sum = 0
        
        horizontal_layout = QHBoxLayout()
        horizontal_layout.addWidget(self.current_item)
        horizontal_layout.addWidget(self.selection_sum)        

        layout.addWidget(self.view)
        layout.addLayout(horizontal_layout)
        
        selection_model = self.view.selectionModel()
        selection_model.currentChanged.connect(
            self.on_current_changed)
        selection_model.selectionChanged.connect(
            self.on_selection_changed)
        
    def on_current_changed(self, current, previous):
        self.current_item.setText(
            'Current item: ' + 
            str(current.model().data(current)))
        
    def on_selection_changed(self, selected, deselected):

        for index in selected.indexes():
            value = self.model.data(index)
            self.selection_sum += value
        for index in deselected.indexes():
            value = self.model.data(index)
            self.selection_sum -= value            
        self.selection_sum.setText(str(self.selection_sum))


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())

