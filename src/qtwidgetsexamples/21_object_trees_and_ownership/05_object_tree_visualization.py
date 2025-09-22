import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QWidget,
    QGroupBox, QCheckBox, QLabel, QPushButton, QVBoxLayout,
    QDialog, QTreeWidget, QTreeWidgetItem)


class ObjectTreeDialog(QDialog):
    
    def __init__(self, root):

        super().__init__()
        
        self.root = root
        
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.tree = QTreeWidget()
        self.tree.setColumnCount(2)
        self.tree.setHeaderLabels(['Class', 'Object name'])
        layout.addWidget(self.tree)
        
        root_class = self.root.__class__.__name__
        root_name = self.root.objectName()
        self.root_item = QTreeWidgetItem(
            self.tree, [root_class, root_name],
            QTreeWidgetItem.ItemType.Type)
        
        self.populate_tree(self.root, self.root_item)
        
    def populate_tree(self, widget, tree_item):
        
        for child_widget in widget.children():
            widget_class = child_widget.__class__.__name__
            widget_name = child_widget.objectName()
            child_item = QTreeWidgetItem(
                tree_item, [widget_class, widget_name],
                QTreeWidgetItem.ItemType.Type)
            self.populate_tree(child_widget, child_item)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        self.setObjectName('Main Window')
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.groupbox = QGroupBox()
        gb_layout = QVBoxLayout()
        self.groupbox.setLayout(gb_layout)
        layout.addWidget(self.groupbox)
        
        self.checkbox = QCheckBox('checkbox')
        self.checkbox.setObjectName('checkbox')
        gb_layout.addWidget(self.checkbox)
        
        self.label = QLabel('label')
        self.label.setObjectName('label')
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        gb_layout.addWidget(self.label)
        
        self.button = QPushButton('button')
        self.button.setObjectName('button')
        gb_layout.addWidget(self.button)
        
        self.show_button = QPushButton('Show object tree')
        self.show_button.clicked.connect(self.show_tree)
        layout.addWidget(self.show_button)
        
    def show_tree(self):
        self.dumpObjectTree()
        self.dialog = ObjectTreeDialog(root=self)
        self.dialog.show()


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()
    
    sys.exit(app.exec())
