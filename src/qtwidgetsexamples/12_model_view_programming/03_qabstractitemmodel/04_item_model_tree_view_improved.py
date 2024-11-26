import json
import sys

from PySide6.QtCore import (QAbstractItemModel,
    QModelIndex, Qt)
from PySide6.QtTest import QAbstractItemModelTester
from PySide6.QtWidgets import (QApplication, QWidget,
    QTreeView, QVBoxLayout)


class TreeItem:

    def __init__(self, data, parent=None):
        
        self.item_data = data
        self.parent = parent
        self.children = []

        if parent:
            self.parent.append_child(self)
            
    def append_child(self, item):
        self.children.append(item)
        
    def child(self, row):
        return self.children[row]
    
    def child_count(self):
        return len(self.children)
    
    def column_count(self):
        return len(self.item_data)
    
    def data(self, column):
        try:
            return self.item_data[column]
        except IndexError:
            return None
        
    def row(self):
        if self.parent:
            return self.parent.children.index(self)
        else:
            return 0
            
    @classmethod
    def create_top_level_items(cls, source):
        
        root_item = TreeItem(['', '', '', ''], None)
        
        with open(source) as json_file:
            data = json.load(json_file)
            for json_object in data:
                tree_item = TreeItem.create_tree_item(
                    json_object, root_item)
                if 'subordinates' in json_object:
                    TreeItem.create_tree(json_object, tree_item)
                    
        return root_item
    
    @staticmethod
    def create_tree(json_object, parent):
        for child_json_object in json_object['subordinates']:
            child = TreeItem.create_tree_item(
                child_json_object, parent)
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
        
        if role == Qt.ItemDataRole.DisplayRole:
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
        
    def headerData(self, section, orientation, role):
        if orientation == Qt.Orientation.Horizontal:
            if role == Qt.ItemDataRole.DisplayRole:
                return self.header[section]


class Window(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        model = JsonModel('data.json')
        QAbstractItemModelTester(model)
        view = QTreeView()
        view.setModel(model)
        layout.addWidget(view)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
