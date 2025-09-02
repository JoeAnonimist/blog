import sys
from PySide6.QtCore import Slot, Qt, SIGNAL
from PySide6.QtWidgets import (QApplication, QWidget, 
    QHBoxLayout, QVBoxLayout, QLabel, QPushButton)


class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.resize(300, 200)
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.checkbox_1 = QPushButton('Checkbox 1: 0 receivers')
        self.checkbox_1.setCheckable(True)
        
        self.label = QLabel()
        
        layout.addWidget(self.checkbox_1)
        layout.addWidget(self.label)

        h_layout = QHBoxLayout()
        self.button_connect = QPushButton('Connect signals')
        self.button_disconnect = QPushButton('Disconnect signals')
        
        self.button_connect.clicked.connect(self.on_connect_button_clicked)
        self.button_disconnect.clicked.connect(self.on_disconnect_button_clicked)
        
        h_layout.addWidget(self.button_connect)
        h_layout.addWidget(self.button_disconnect)
        layout.addLayout(h_layout)

    def on_connect_button_clicked(self):
        
        self.checkbox_1.clicked.connect(self.on_state_changed)
        
        self.update_checkbox_texts()

    def on_disconnect_button_clicked(self):

        self.checkbox_1.clicked.disconnect(self.on_state_changed)

        self.update_checkbox_texts()
        
    @Slot(bool)
    def on_state_changed(self, checked):
        sender_name = self.sender().objectName()
        self.label.setText(f'{sender_name} {checked}')
        
    def update_checkbox_texts(self):

        self.checkbox_1.setText('Checkbox 1: ' +
            str(self.receiver_count(self.checkbox_1)) + ' receivers')
        
    def receiver_count(self, checkbox):
        return checkbox.receivers(SIGNAL('clicked(bool)'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())