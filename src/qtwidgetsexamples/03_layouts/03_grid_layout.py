# QGridLayout lays out widgets, well, in a grid
import sys

from PySide6.QtWidgets import (QApplication, 
    QWidget, QPushButton, QLabel, QGridLayout)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        # 1 - Create the layout:
        
        layout = QGridLayout()
        self.setLayout(layout)
        
        # 2 - Create widgets:
        # Button 1 and button 2 are in the row 0 of the grid.
        # Button 3 and button 4  are in the row 1.
        # Label is used to display button row and column on click.
        
        button_1 = QPushButton('Button 1')
        button_2 = QPushButton('Button 2')
        button_3 = QPushButton('Button 3')
        button_4 = QPushButton('Button 4')
        self.label = QLabel('')
        self.position_string = '{} position: \n row: {}, column: {}'

        # 3 - Add widgets to grid
        # (0, 0) is the top left cell
        # The first integer is the row number
        # The secont int is the column number
        
        layout.addWidget(button_1, 0, 0)
        layout.addWidget(button_2, 0, 1)
        layout.addWidget(button_3, 1, 0)
        layout.addWidget(button_4, 1, 1)
        
        # The label starts in row 2, column 0
        # and spans one row and two columns.
        
        layout.addWidget(self.label, 2, 0, 1, 2)
        
        # Handle button events
        
        button_1.clicked.connect(self.on_button_clicked)
        button_2.clicked.connect(self.on_button_clicked)
        button_3.clicked.connect(self.on_button_clicked)
        button_4.clicked.connect(self.on_button_clicked)
    
    # The slot method
        
    def on_button_clicked(self):
        
        # Get a reference to the clicked button
        
        clicked_button = self.sender()
        index = self.layout().indexOf(clicked_button)
        
        if index >= 0:
            position = (self.layout().getItemPosition(index))
            self.label.setText(self.position_string.format(
                clicked_button.text(), 
                str(position[0]), str(position[1]),))
        


if __name__ == '__main__':

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())