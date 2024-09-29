# The QComboBox widget is a combined button and popup list.

from PySide6.QtWidgets import (QApplication, 
    QWidget, QVBoxLayout, QComboBox, QLabel)
import sys


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1 - Create the combo box
        
        self.combo_box = QComboBox()
        
        # 2 - Add items to it
        
        self.combo_box.addItem('Linux')
        self.combo_box.addItem('Windows')
        self.combo_box.addItem('Mac')
        self.combo_box.addItem('Android')
        
        # Set setEditable to False if you
        # want to limit text to your predefined values.
        
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
        
    def on_current_text_changed(self, text):
        self.label_text_changed.setText(text)

    #     Also handle QComboBox.textActivated
    def on_text_activated(self, text):
        self.label_text_activated.setText(text)


if __name__ == '__main__':

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())