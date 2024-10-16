# The QSpinBox class provides a spin box widget.
# The QDial class provides a rounded range control
# (like a speedometer or potentiometer).
#
# Access their current value using their value() property

import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication,
    QWidget, QVBoxLayout, QSpinBox, QDial, QLabel)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1 - Create the widgets
        
        self.spinbox = QSpinBox()
        self.spinbox.setRange(0, 100)
        self.spinbox.setSingleStep(5)
        
        self.dial = QDial()
        self.dial.setRange(0, 100)
        
        self.label = QLabel()
        
        # 3. Connect the signals with the slot functions
        
        self.spinbox.valueChanged.connect(
            self.on_spinbox_value_changed)
            
        self.dial.valueChanged.connect(
            self.on_dial_value_changed)
        
        layout.addWidget(self.spinbox)
        layout.addWidget(self.dial)
        layout.addWidget(self.label)
    
    # 2. Write the slots. The value passed
    #    from the signals is an integer. 
    
    @Slot()    
    def on_spinbox_value_changed(self, i):
        self.dial.setValue(i)
        self.label.setText(str(i))
    
    @Slot()
    def on_dial_value_changed(self, i):
        self.spinbox.setValue(i)
        self.label.setText(str(i))


if __name__ == '__main__':

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
