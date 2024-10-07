# The QTreeWidget class provides a standard tree widget.

import sys

from PySide6.QtWidgets import (QApplication,
    QWidget, QVBoxLayout, QTreeWidget,
    QTreeWidgetItem, QLabel)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1 - Create the tree widget
        
        self.tree_widget = QTreeWidget()
        
        # 2 - Create the tree widget items and add them 
        #     to the tree widget
        #
        # QTreeWidgetItem.ItemType.Type value is 0
        # You can use 0 instead of the enum value
        # but there's no guarantee it will stay 0 in the future.
        #
        # apes parent is self.tree_widget which means 
        # apes is the root item
        #
        # ['Apes'] is the item text. It's a list with one element.
        # That's because a tree widget has one column by default.
        apes = QTreeWidgetItem(self.tree_widget, ['Apes'],
            QTreeWidgetItem.ItemType.Type)
        
        # Add other items to the tree. The pattern is the same
        # as for the root item: (parent, text, type)
        # There are several other QTreeWidgetItem 
        # constructors as well.
        gibbons = QTreeWidgetItem(apes, ['Gibbons'], 0)
        hominidae = QTreeWidgetItem(apes, ['Hominidae'], 0)
        ponginae = QTreeWidgetItem(hominidae, ['Orangutans'], 0)
        homininae = QTreeWidgetItem(hominidae, ['Homininae'], 0)
        gorillinae = QTreeWidgetItem(homininae, ['Gorillas'], 0)
        hominini = QTreeWidgetItem(homininae, ['Hominini'], 0)
        panina = QTreeWidgetItem(hominini, ['Chimpanzees'], 0)
        hominina = QTreeWidgetItem(hominini, ['Hominina'], 0)
        
        # Add some event handling just for show. 
        self.tree_widget.currentItemChanged.connect(
            self.on_current_item_changed)
        
        self.label = QLabel()
        
        # 3 - Add the tree widget to the layout
        
        layout.addWidget(self.tree_widget)
        layout.addWidget(self.label)

    # The label will display currently selected item text.
    def on_current_item_changed(self, current, previous):
        self.label.setText(current.text(0))


if __name__ == '__main__':

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
