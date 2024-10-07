# A group box provides a frame, a title on top
# and displays various other widgets inside itself.

import sys

from PySide6.QtWidgets import (QApplication,
    QWidget, QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButton, QLabel)


class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initUi()
        
        self.show()
        
    def initUi(self):

        layout = QHBoxLayout()

        self.label = QLabel()
        self.label.setFixedWidth(80)
        
        # 1 - Create the group box
        
        groupbox = QGroupBox()
        groupbox.setTitle('Group box')
        
        # 2 - Set the group box layout
        #     You can't add widgets directly to the group box.
        
        groupbox_layout = QVBoxLayout()
        groupbox.setLayout(groupbox_layout)

        # 3 - Add widgets to the layout.

        self.radiobutton_1 = QRadioButton('Option 1')
        self.radiobutton_2 = QRadioButton('Option 2')

        groupbox_layout.addWidget(self.radiobutton_1)
        groupbox_layout.addWidget(self.radiobutton_2)
        
        # Handle radio button toggle signals
        
        self.radiobutton_1.toggled.connect(self.on_toggled)
        self.radiobutton_2.toggled.connect(self.on_toggled)

        layout.addWidget(groupbox)
        layout.addWidget(self.label)
        
        self.setLayout(layout)

    # The slot method. If there are multiple radio buttons
    # in a group box only one can be checked.
    # Not so with check boxes.
    
    def on_toggled(self):
        if self.radiobutton_1.isChecked():
            self.label.setText(self.radiobutton_1.text())
        else:
            self.label.setText(self.radiobutton_2.text())


if __name__ == '__main__':

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
