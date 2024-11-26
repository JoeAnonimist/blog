import json
import sys

from PySide6.QtCore import (QAbstractItemModel,
    QModelIndex, Qt)
from PySide6.QtTest import QAbstractItemModelTester
from PySide6.QtWidgets import (QApplication, QWidget,
    QPushButton, QTreeView, QVBoxLayout)


class TreeItem:
    
    counter = 0

    def __init__(self, data, parent=None):
        
        self.item_data = data
        self.parent = parent
        self.children = []

    def append_child(self, item):
        TreeItem.counter += 1
        self.children.append(item)
        
    def child(self, row):
        if self.child_count() > row:
            return self.children[row]
        else:
            return None
    
    def child_count(self):
        return len(self.children)
    
    def column_count(self):
        return len(self.item_data)
    
    def data(self, column):
        try:
            return self.item_data[column]
        except IndexError:
            return None
    
    def set_data(self, column, value):
        self.item_data[column] = value
        
    def row(self):
        if self.parent:
            return self.parent.children.index(self)
        else:
            return 0
        
    def insert_child(self, row):
        TreeItem.counter += 1
        print('In insert child', row)
        data = [TreeItem.counter, '', '', '']
        item = TreeItem(data, self)
        self.children.insert(row, item)
            
    def remove_child(self, row):
        self.children[row:row + 1] = []
            
    @staticmethod
    def create_top_level_items(source):
        
        root_item = TreeItem(['', '', '', ''], None)
        
        with open(source) as json_file:
            data = json.load(json_file)
            for json_object in data:
                tree_item = TreeItem.create_tree_item(
                    json_object, root_item)
                root_item.append_child(tree_item)
                if 'subordinates' in json_object:
                    TreeItem.create_tree(json_object, tree_item)
                    
        return root_item
    
    @staticmethod
    def create_tree(json_object, parent):
        for child_json_object in json_object['subordinates']:
            child = TreeItem.create_tree_item(
                child_json_object, parent)
            parent.append_child(child)
            if 'subordinates' in child_json_object:
                TreeItem.create_tree(child_json_object, child)
    
    @staticmethod
    def create_tree_item(json_object, parent):
        child = TreeItem(
                [json_object['id'],
                 json_object['firstname'],
                 json_object['lastname'],
                 json_object['profession']],
                parent)
        return child


class JsonModel(QAbstractItemModel):

    def __init__(self, source, parent=None):

        super().__init__(parent)
        self.root_item = TreeItem.create_top_level_items(source)
        self.header = ['Id', 'First Name', 'Last Name', 'Profession']

    def rowCount(self, parent=QModelIndex()):

        if parent.isValid():
            parent_item = parent.internalPointer()
            return parent_item.child_count()
        else:
            return self.root_item.child_count()

    def columnCount(self, parent=QModelIndex()):
        if parent.isValid():
            return parent.internalPointer().column_count()
        else:
            return self.root_item.column_count()

    def data(self, index, role):
        
        if role == Qt.ItemDataRole.DisplayRole \
           or role == Qt.ItemDataRole.EditRole:
            item = index.internalPointer()
            return item.data(index.column())

    def index(self, row, column, parent=QModelIndex()):

        if not self.hasIndex(row, column, parent):
            return QModelIndex()

        if not parent.isValid():
            parent_item = self.root_item
        else:
            parent_item = parent.internalPointer()

        childItem = parent_item.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QModelIndex()

    def parent(self, index):

        if not index.isValid():
            return QModelIndex()

        item = index.internalPointer()
        parent_item = item.parent

        if parent_item == self.root_item:
            return QModelIndex()
        else:
            row = parent_item.row()
            return self.createIndex(row, 0, parent_item)

    def flags(self, index):
        flags = Qt.ItemFlags.ItemIsSelectable | \
            Qt.ItemFlags.ItemIsEnabled | \
            Qt.ItemFlags.ItemIsEditable
        return flags
   
    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:
            tree_item = index.internalPointer()
            if tree_item.data(index.column()) != value:
                tree_item.set_data(index.column(), value)
                self.dataChanged.emit(index, index)
                return True
            return False
        return False

    def insertRows(self, row, count, parent=QModelIndex()):
        if 0 <= row <= self.rowCount():
            print(row, row + count - 1)
            self.beginInsertRows(parent, row, row + count - 1)
            if parent.isValid():
                parent_item = parent.internalPointer()
            else:
                parent_item = self.root_item
            parent_item.insert_child(row)
            self.endInsertRows()
            return True
        else:
            return False
        
    def removeRows(self, row, count, parent=QModelIndex()):
        self.beginRemoveRows(parent, row, row + count - 1)
        if parent.internalPointer():
            parent_item = parent.internalPointer()
        else:
            parent_item = self.root_item
        parent_item.remove_child(row)
        self.endRemoveRows()
        return True

    def headerData(self, section, orientation, role):
        if orientation == Qt.Orientation.Horizontal:
            if role == Qt.ItemDataRole.DisplayRole:
                return self.header[section]


class Window(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.model = JsonModel('data.json')
        QAbstractItemModelTester(self.model)
        self.model.dataChanged.connect(self.on_data_changed)
        
        self.view = QTreeView()
        self.view.setModel(self.model)

        self.insert_sibling_button = QPushButton(
            'Insert sibling node')
        self.insert_sibling_button.clicked.connect(self.on_insert_sibling)
        
        self.insert_child_button = QPushButton(
            'Insert child node')
        self.insert_child_button.clicked.connect(self.on_insert_child)
        
        self.remove_button = QPushButton('Remove current')
        self.remove_button.clicked.connect(self.on_remove)

        layout.addWidget(self.view)
        layout.addWidget(self.insert_sibling_button)
        layout.addWidget(self.insert_child_button)
        layout.addWidget(self.remove_button)
        
    def on_insert_sibling(self):
        print('in on insert sibling')
        row = self.view.selectionModel().currentIndex().row()
        parent = self.view.selectionModel().currentIndex().parent()
        self.model.insertRow(row + 1, parent)
    
    def on_insert_child(self):
        print('in on insert child')
        row = self.view.selectionModel().currentIndex().row()
        parent = self.view.selectionModel().currentIndex()
        print(parent)
        self.model.insertRow(row, parent)
    
    def on_remove(self):
        row = self.view.selectionModel().currentIndex().row()
        parent = self.view.selectionModel().currentIndex().parent()
        self.model.removeRow(row, parent)

    def on_data_changed(self, toplLeft, bottomRight, roles):
        print(f'Model data changed, row:{toplLeft.row()}, col: {toplLeft.column()}')
        print(toplLeft.internalPointer().item_data)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
