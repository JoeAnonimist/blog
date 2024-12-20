# The QTableWidget class provides an
# item-based table view with a default model.
#
# Simply put, it's a table.

import sys
from random import randint

from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout,
    QTableWidget, QTableWidgetItem, QHeaderView, QLabel)


class Window(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        # 1 - Create the table widget passing row and column
        #     count to the constructor.
        #     This table widget has three rows and four columns
        self.table_widget = QTableWidget(3, 4)

        # Fit columns to table width
        self.table_widget.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch)

        # 2 - Use QTableWidgetItem instances
        #     to manipulate table cells

        # Fill the cells with some data
        for r in range(self.table_widget.rowCount()):
            for c in range(self.table_widget.columnCount()):
                value = randint(0, 100)
                item = QTableWidgetItem()
                item.setData(Qt.ItemDataRole.DisplayRole, value)
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.table_widget.setItem(r, c, item)

        self.table_widget.currentItemChanged.connect(
            self.on_current_item_changed)

        self.table_widget.itemChanged.connect(self.on_item_changed)

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.table_widget)
        layout.addWidget(self.label)

    # 3 - Handle table widget signals
    #     table selection changes:
    @Slot()
    def on_current_item_changed(self, current, previous):
        # You have references to current and previously selected
        # table cells. previous can be None!
        self.label.setText(f'Selected cell value: {current.text()}')

    #     item value changes:
    @Slot()
    def on_item_changed(self, item):
        self.label.setText(f'Cell value has changed: {item.text()}')


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
