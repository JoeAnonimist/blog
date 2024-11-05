import sys
import psutil

from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import (QApplication, QWidget,
    QVBoxLayout, QListWidget, QListWidgetItem, QLabel)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.list_widget = QListWidget()
        
        for process in psutil.process_iter(attrs=['pid', 'name', 'exe']):
            try:
                item = QListWidgetItem(f'{process.pid}: {process.name()}')
                item.setData(Qt.ItemDataRole.UserRole, process.exe())
                self.list_widget.addItem(item)
            except Exception as e:
                print(e)

        self.label = QLabel()
        
        layout.addWidget(self.list_widget)
        layout.addWidget(self.label)

        self.list_widget.currentItemChanged.connect(
            self.on_current_item_changed)

    @Slot()
    def on_current_item_changed(self, current, previous):
        self.label.setText(current.data(Qt.ItemDataRole.UserRole))


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
