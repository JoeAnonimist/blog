# The QSpinBox class provides a spin box widget.
# The QDial class provides a rounded range control
# (like a speedometer or potentiometer).
#
# Access their current value using their value() property

from PySide6.QtWidgets import (QApplication, 
    QWidget, QVBoxLayout, QSpinBox, QDial, QLabel)
import sys


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
        
        self.spinbox.valueChanged.connect(
            self.on_spinbox_value_changed)
            
        self.dial.valueChanged.connect(
            self.on_dial_value_changed)
        
        # 2 - Add widgets to the layout
        
        layout.addWidget(self.spinbox)
        layout.addWidget(self.dial)
        layout.addWidget(self.label)

    # 3 - Get widget value. It's an integer.
        
    def on_spinbox_value_changed(self, i):
        self.dial.setValue(i)
        self.label.setText(str(i))
        
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