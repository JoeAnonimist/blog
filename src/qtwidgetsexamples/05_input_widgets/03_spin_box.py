# The QSpinBox class provides a spin box widget.
# The QDial class provides a rounded range control
# (like a speedometer or potentiometer).
#
# Access their curent value using their value() property

from PySide6.QtWidgets import (QApplication, 
    QWidget, QVBoxLayout, QSpinBox, QDial, QLabel)
import sys


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1 - Create the widgets
        
        spin_box = QSpinBox()
        spin_box.setRange(0, 100)
        spin_box.setSingleStep(5)
        
        dial = QDial()
        dial.setRange(0, 100)
        
        self.label = QLabel()
        
        # You can pass additional arguments to Qt slots
        # using Python lambda
        
        spin_box.valueChanged.connect(
            lambda: self.on_value_changed(spin_box, dial))
            
        dial.valueChanged.connect(
            lambda: self.on_value_changed(dial, spin_box))
        
        # 2 - Add widgets to the layout
        
        layout.addWidget(spin_box)
        layout.addWidget(dial)
        layout.addWidget(self.label)

    # 3 - Get widget value. It's an integer.
        
    def on_value_changed(self, sender, target):
        
        value = sender.value()
        target.setValue(value)
        self.label.setText(str(value))


if __name__ == '__main__':

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())