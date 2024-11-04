# The QComboBox widget is a combined button and popup list.

import sys

from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import (QApplication,
    QWidget, QVBoxLayout, QComboBox, QLabel)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1 - Create the combo box
        
        self.combo_box = QComboBox()
        
        # 2 - Add items to it
        
        self.combo_box.addItems(
            ['Linux', 'Windows', 'Mac', 'Android'])
        
        # Set setEditable to False if you
        # want to limit text to your predefined values.
        # False is the default value
        
        self.combo_box.setEditable(True)
        
        self.label_text_changed = QLabel()
        self.label_text_activated = QLabel()
        
        layout.addWidget(self.combo_box)
        layout.addWidget(self.label_text_changed)
        layout.addWidget(self.label_text_activated)
        
        self.combo_box.currentTextChanged.connect(
            self.on_current_text_changed)
            
        self.combo_box.textActivated.connect(
            self.on_text_activated)
    
    # 3 - Handle QComboBox.currentTextChanged signals
    
    @Slot()
    def on_current_text_changed(self, text):
        self.label_text_changed.setText(text)
        self.print_current()

    #     Also handle QComboBox.textActivated
    
    @Slot()
    def on_text_activated(self, text):
        self.label_text_activated.setText(text)
        self.print_current()
        
    def print_current(self):
        print(self.combo_box.currentData(Qt.DisplayRole))
        print(self.combo_box.currentIndex())
        print(self.combo_box.currentText())


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
