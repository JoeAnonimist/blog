# The QListWidget class provides an item-based
# list widget, ie. it displays a list of items.
# This is a basic example. You can also add 
# icons and checkboxes. QListView is even more flexible.

import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication,
    QWidget, QVBoxLayout, QListWidget, QLabel)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1 - Create the list widget and add items to it
        
        self.list_widget = QListWidget()
        self.list_widget.addItems(['blue', 'green', 'red'])

        self.label = QLabel()
        
        layout.addWidget(self.list_widget)
        layout.addWidget(self.label)
        
        # 3 - Connect the list widget currentItemChanged signal
        #     with the slot.
        
        self.list_widget.currentItemChanged.connect(
            self.on_current_item_changed)
    
    # 2 - Create the slot to handle item changed events
    
    @Slot()
    def on_current_item_changed(self, current, previous):
        
        color = current.text()
        self.label.setStyleSheet(
            'background-color:{};'.format(color))


if __name__ == '__main__':

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
