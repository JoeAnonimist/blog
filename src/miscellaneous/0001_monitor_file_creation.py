import sys

from PySide6.QtCore import QDir
from PySide6.QtWidgets import (QApplication,
    QWidget, QLabel, QVBoxLayout, QFileSystemModel)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setWindowTitle('Monitoring current directory')
        self.setLayout(layout)

        self.label = QLabel('Monitoring file creation')
        layout.addWidget(self.label)
        
        # 1 - Create a QFileSystemModel object.
        #     Set the directory to be monitored
        #     and the filter to monitor files only.
        
        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.currentPath())
        self.model.setFilter(QDir.Filter.Files)
        
        # 3 - Connect QFileSystemModel.rowsInsewrted
        #     with the slot.
        
        self.model.rowsInserted.connect(self.on_rows_inserted)
    
    # 2 - Create the slot
    
    def on_rows_inserted(self, parent, first, last):
        filenames = ''
        for row in range(first, last + 1):
            index = self.model.index(row, 0, parent)
            filenames = filenames + index.data() + '\n'
        self.label.setText(filenames)


if __name__ == '__main__':

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
