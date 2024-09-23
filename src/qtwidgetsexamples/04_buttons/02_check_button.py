# A QCheckBox is an option button that can be 
# switched on (checked) or off (unchecked). 

from PySide6.QtWidgets import (QApplication, 
    QWidget, QVBoxLayout, QCheckBox, QLabel)
import sys


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1 - Create the checkboxes and add them to the layout
        
        self.windows_checkbox = QCheckBox('Windows')
        self.linux_checkbox = QCheckBox('Linux')
        self.mac_checkbox = QCheckBox('Mac')
        
        self.label = QLabel()
        
        layout.addWidget(self.windows_checkbox)
        layout.addWidget(self.linux_checkbox)
        layout.addWidget(self.mac_checkbox)
        layout.addWidget(self.label)
        
        # 3 - For each checkbox connect QCheckBox.stateChanged signal
        #     with the slot. stateChanged is emitted when a checkbox
        #     is checked or unchecked.
        
        self.windows_checkbox.stateChanged.connect(self.on_state_changed)
        self.linux_checkbox.stateChanged.connect(self.on_state_changed)
        self.mac_checkbox.stateChanged.connect(self.on_state_changed)
    
    # 2 - Create the slot. You are interested in
    #     QCheckBox.isChecked() which can be true or false
        
    def on_state_changed(self):
        
        label_text =  ''
        
        if self.windows_checkbox.isChecked():
            label_text += 'Windows\n'
            
        if self.linux_checkbox.isChecked():
            label_text += 'Linux\n'
            
        if self.mac_checkbox.isChecked():
            label_text += 'Mac\n'
            
        self.label.setText(label_text)


if __name__ == '__main__':

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())