# The QTreeView class provides an  
# implementation of a tree view.
# For the model we are using QFileSystemModel
# provided by Qt so no need for subclassing.

import sys

from PySide6.QtCore import QDir
from PySide6.QtWidgets import QFileSystemModel
from PySide6.QtWidgets import (QApplication,
    QWidget, QVBoxLayout, QTreeView)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1 - Create the tree view
        
        tree_view = QTreeView()
        
        # 2 - Create the model and set its root path 
        #     to the user's home directory.
        
        model = QFileSystemModel()
        model.setRootPath(QDir.home().path())
        
        # 3 - Set the tree view's model
        
        tree_view.setModel(model)
        
        # 4 - This line sets the tree view root index,
        #     to the index of the user's home directory. 
        #     Any changes to files and directories within root
        #     will be reflected in the model.
        
        tree_view.setRootIndex(model.index(QDir.home().path()))
        
        layout.addWidget(tree_view)
        
        # It's a start of a rudimentary file manager
        # in a few lines of code!


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
