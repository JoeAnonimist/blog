# The QToolBox class provides a column of tabbed widget items

import sys

from PySide6.QtWidgets import (QApplication,
    QWidget, QVBoxLayout, QToolBox, QPushButton, QLabel)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1 - Create the toolbox
        
        toolbox = QToolBox()
        
        # 2 - Create the widgets (buttons in this case)
        
        linux_button = QPushButton('Linux')
        windows_button = QPushButton('Windows')
        mac_button = QPushButton('Mac')
        
        # 3 - Add widgets to the toolbox
        
        toolbox.addItem(linux_button, 'Lin')
        toolbox.addItem(windows_button, 'Win')
        toolbox.addItem(mac_button, 'Mac')
        
        linux_button.clicked.connect(self.on_clicked)
        windows_button.clicked.connect(self.on_clicked)
        mac_button.clicked.connect(self.on_clicked)
        
        self.label = QLabel()
        
        # QToolBox is kinda weird looking widget
        # I don't think I like it.
        
        layout.addWidget(toolbox)
        layout.addWidget(self.label)
        
    def on_clicked(self):
        self.label.setText(self.sender().text() + ' clicked!')


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
