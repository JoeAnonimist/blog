import sys
from PySide6.QtCore import Slot, Qt, SIGNAL, QMetaMethod
from PySide6.QtWidgets import (QApplication, QWidget, 
    QHBoxLayout, QVBoxLayout, QCheckBox, QLabel, QPushButton)


class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.resize(300, 200)
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.checkbox_1 = QCheckBox('Checkbox 1: 0 receivers')
        self.checkbox_1.setObjectName('Checkbox1')

        self.checkbox_2 = QCheckBox('Checkbox 2: 0 receivers')
        self.checkbox_2.setObjectName('Checkbox2')
        
        self.label = QLabel()
        
        layout.addWidget(self.checkbox_1)
        layout.addWidget(self.checkbox_2)
        
        layout.addWidget(self.label)

        h_layout = QHBoxLayout()
        self.button_connect = QPushButton('Connect signals')
        self.button_disconnect = QPushButton('Disconnect signals')
        
        self.button_connect.clicked.connect(
            self.on_connect_button_clicked)
        self.button_disconnect.clicked.connect(
            self.on_disconnect_button_clicked)
        
        h_layout.addWidget(self.button_connect)
        h_layout.addWidget(self.button_disconnect)
        layout.addLayout(h_layout)

    def on_connect_button_clicked(self):
        
        self.checkbox_1.checkStateChanged.connect(
            self.on_state_changed)
        self.checkbox_2.checkStateChanged.connect(
            self.on_state_changed)
        
        self.update_checkbox_texts()

    def on_disconnect_button_clicked(self):
        
        self.checkbox_1.checkStateChanged.disconnect(
            self.on_state_changed)
        self.checkbox_2.checkStateChanged.disconnect(
            self.on_state_changed)
        self.update_checkbox_texts()
        
    def update_checkbox_texts(self):
        
        '''
        sig_bytearray = QMetaMethod.fromSignal(
            self.checkbox_1.checkStateChanged)
        sig_str = sig_bytearray.methodSignature().data().decode()
        print(sig_str)
        '''
        
        count1 = self.checkbox_1.receivers(
            SIGNAL('checkStateChanged(Qt::CheckState)'))
        count2 = self.checkbox_2.receivers(
            SIGNAL('checkStateChanged(Qt::CheckState)'))
        
        self.checkbox_1.setText(f'Checkbox 1: {count1} receivers')
        self.checkbox_2.setText(f'Checkbox 2: {count2} receivers')
        
    @Slot(Qt.CheckState)
    def on_state_changed(self, state):
        sender_name = self.sender().objectName()
        self.label.setText(f'{sender_name} {state}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())