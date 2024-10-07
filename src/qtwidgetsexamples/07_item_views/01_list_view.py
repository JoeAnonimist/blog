# QListView presents items stored in a model.
# ie. it uses the QT model/view architecture
# Models contain data and views display it
# so one view can be used to display multiple models and vv.
# It is similar to QListWidget but should be more flexible

import os
import sys

from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import (QApplication,
    QWidget, QVBoxLayout, QListView)


# We need model classes now
class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1 - Create the view
        
        list_view = QListView()
        
        # 2 - Create and populate the model
        
        self.model = QStandardItemModel()
        self.populate_model()
        
        # 3 - Connect the model and the view
        
        list_view.setModel(self.model)
        
        layout.addWidget(list_view)
        
    def populate_model(self):
        # This incantation returns the contents
        # of your home directory as a list:
        files = os.listdir(os.path.expanduser('~'))
        
        for f in files:
            item = QStandardItem(f)
            self.model.appendRow(item)


if __name__ == '__main__':

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
