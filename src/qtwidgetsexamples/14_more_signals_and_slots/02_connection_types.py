import sys
from PySide6.QtCore import Slot, Qt, SIGNAL
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
        
        self.checkbox_3 = QCheckBox('Checkbox 3: 0 receivers')
        self.checkbox_3.setObjectName('Checkbox3')
        
        self.label = QLabel()
        
        layout.addWidget(self.checkbox_1)
        layout.addWidget(self.checkbox_2)
        layout.addWidget(self.checkbox_3)
        
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
            self.on_state_changed, Qt.ConnectionType.UniqueConnection)
        self.checkbox_3.checkStateChanged.connect(
            self.on_checkbox3_state_changed)
        
        self.update_checkbox_texts()

    def on_disconnect_button_clicked(self):

        self.checkbox_1.checkStateChanged.disconnect(
            self.on_state_changed)
        self.checkbox_2.checkStateChanged.disconnect(
            self.on_state_changed)
        self.checkbox_3.checkStateChanged.disconnect(
            self.on_checkbox3_state_chenged)

        '''
        QObject.disconnect(
            self.checkbox_1,
            SIGNAL('checkStateChanged(Qt::CheckState)'),
            self,
            SLOT('on_state_changed(Qt::CheckState)'))
        
        QObject.disconnect(
            self.checkbox_2,
            SIGNAL('checkStateChanged(Qt::CheckState)'),
            self,
            SLOT('on_state_changed(Qt::CheckState)'))
        '''
        '''
        metaobj = self.checkbox_1.metaObject()
        index = metaobj.indexOfSignal(
            'checkStateChanged(Qt::CheckState)')
        signal_method = metaobj.method(index)

        metaobj_self = self.metaObject()
        index_slot = metaobj_self.indexOfSlot(
            'on_state_changed(Qt::CheckState)')
        slot_method = metaobj_self.method(index_slot)

        QObject.disconnect(self.checkbox_1,
            signal_method, self, slot_method)
        QObject.disconnect(self.checkbox_2,
            signal_method, self, slot_method)
        '''
        
        '''
        # disconnect one connection at a time
        self.checkbox_1.disconnect(SIGNAL('checkStateChanged(Qt::CheckState)'), self.on_state_changed)
        self.checkbox_2.disconnect(SIGNAL('checkStateChanged(Qt::CheckState)'), self.on_state_changed)
        '''
        '''
        self.checkbox_1.disconnect(self, SLOT('on_state_changed(Qt::CheckState)'))
        self.checkbox_2.disconnect(self, SLOT('on_state_changed(Qt::CheckState)'))
        '''

        self.update_checkbox_texts()
        
    @Slot(Qt.CheckState)
    def on_state_changed(self, state):
        sender_name = self.sender().objectName()
        self.label.setText(f'{sender_name} {state.name}')
        
    @Slot(Qt.CheckState)
    def on_checkbox3_state_changed(self, state):
        self.label.setText('Checkbox3 ' + state.name)
        
    def update_checkbox_texts(self):
        
        '''
        sig_bytearray = QMetaMethod.fromSignal(
            self.checkbox_1.checkStateChanged)
        sig_str = sig_bytearray.methodSignature().data().decode()
        print(sig_str)
        '''

        self.checkbox_1.setText('Checkbox 1: ' +
            str(self.receiver_count(self.checkbox_1)) + ' receivers')
        self.checkbox_2.setText('Checkbox 2: ' +
            str(self.receiver_count(self.checkbox_2)) + ' receivers')
        self.checkbox_3.setText('Checkbox 3: ' +
            str(self.receiver_count(self.checkbox_3)) + ' receivers')
        
    def receiver_count(self, checkbox):
        return checkbox.receivers(SIGNAL(
            'checkStateChanged(Qt::CheckState)'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())