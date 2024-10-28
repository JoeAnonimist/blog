# QListView presents items stored in a model.
# ie. it uses the QT model/view architecture
# Models contain data and views display it
# so one model can be used with multiple views.
# It is similar to QListWidget but should be more flexible

import os
import sys

from PySide6.QtCore import QDir
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import (QApplication,
    QWidget, QVBoxLayout, QListView)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1 - Create the view
        
        list_view = QListView()
        
        # 2 - Create and populate the model
        
        self.model = QStandardItemModel()
        
        files = QDir.home().entryList()
        for f in files:
            item = QStandardItem(f)
            self.model.appendRow(item)
        
        # 3 - Connect the model and the view
        
        list_view.setModel(self.model)
        
        layout.addWidget(list_view)


if __name__ == '__main__':

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
