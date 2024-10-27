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
        # apes parent is self.tree_widget which means 
        # apes is the root item
        #
        # ['Apes'] is the item text. It's a list with one element.
        # That's because a tree widget has one column by default.
        apes = QTreeWidgetItem(self.tree_widget, ['Apes'])
        
        # Add other items to the tree. The pattern is the same
        # as for the root item: (parent, text)
        # There are several other QTreeWidgetItem 
        # constructors as well.
        gibbons = QTreeWidgetItem(apes, ['Gibbons'])
        hominidae = QTreeWidgetItem(apes, ['Hominidae'])
        ponginae = QTreeWidgetItem(hominidae, ['Orangutans'])
        homininae = QTreeWidgetItem(hominidae, ['Homininae'])
        gorillinae = QTreeWidgetItem(homininae, ['Gorillas'])
        hominini = QTreeWidgetItem(homininae, ['Hominini'])
        panina = QTreeWidgetItem(hominini, ['Chimpanzees'])
        hominina = QTreeWidgetItem(hominini, ['Hominina'])
        
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
