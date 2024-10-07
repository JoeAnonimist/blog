# The QTreeView class provides a default model/view 
# implementation of a tree view.
# For the model I'm using QFileSystemModel
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
        
        # 2 - Create the model
        
        model = QFileSystemModel()
        
        # 3 - Set the mode as the tree view's model
        
        tree_view.setModel(model)
        
        # 4 - This line sets the tree view root
        #     In this case I set it to my home directory
        #     Any changes to files and directories within root
        #     will be reflected in the model.
        
        tree_view.setRootIndex(
            model.setRootPath(QDir.home().path()))
        
        layout.addWidget(tree_view)
        
        # It's a start of a rudimentary file manager
        # in a few lines of code!


if __name__ == '__main__':

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
