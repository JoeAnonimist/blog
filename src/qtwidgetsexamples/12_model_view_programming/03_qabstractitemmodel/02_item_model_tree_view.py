import json
import sys

from PySide6.QtCore import (QAbstractItemModel,
    QModelIndex, Qt)
from PySide6.QtTest import QAbstractItemModelTester
from PySide6.QtWidgets import (QApplication, QWidget,
    QTreeView, QVBoxLayout)


class TreeItem:

    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.children = []


class JsonModel(QAbstractItemModel):

    def __init__(self, source, parent=None):

        super().__init__(parent)

        self.root_item = TreeItem(['', '', ''], None)
        with open(source) as json_file:
            data = json.load(json_file)
            for json_item in data:
                tree_item = TreeItem(
                    [json_item['id'],
                     json_item['firstname'],
                     json_item['lastname']],
                    self.root_item)
                self.root_item.children.append(tree_item)
                if 'subordinates' in json_item:
                    self.create_tree(json_item, tree_item)

    def create_tree(self, json_item, tree_item):
        for child_json_item in json_item['subordinates']:
            child_item = TreeItem(
                [child_json_item['id'],
                 child_json_item['firstname'],
                 child_json_item['lastname']],
                tree_item)
            tree_item.children.append(child_item)
            if 'subordinates' in child_json_item:
                self.create_tree(child_json_item, child_item)

    def rowCount(self, parent=QModelIndex()):

        if parent.isValid():
            parent_item = parent.internalPointer()
            return len(parent_item.children)
        else:
            return len(self.root_item.children)

    def columnCount(self, parent=QModelIndex()):
        return 1

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            item = index.internalPointer()
            return f'{item.data[1]} {item.data[2]}'

    def index(self, row, column, parent=QModelIndex()):

        if not self.hasIndex(row, column, parent):
            return QModelIndex()

        if not parent.isValid():
            parent_item = self.root_item
        else:
            parent_item = parent.internalPointer()

        childItem = parent_item.children[row]
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
            grandparent_item = parent_item.parent
            row = grandparent_item.children.index(parent_item)
            return self.createIndex(row, 0, parent_item)


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
