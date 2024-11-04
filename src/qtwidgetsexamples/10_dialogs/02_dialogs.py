# The QColorDialog class provides a dialog widget for specifying colors.
# The QFileDialog class provides a dialog that allow users to select files or directories.
# The QFontDialog class provides a dialog widget for selecting a font.
# The QInputDialog class provides a simple convenience dialog to get a single value from the user.


from PySide6.QtWidgets import (QApplication, QWidget, 
    QPushButton, QLabel, QColorDialog, QFileDialog, 
    QFontDialog, QInputDialog, QLineEdit, QGridLayout)
from PySide6.QtGui import QFont
from PySide6.QtCore import QFile, QFileInfo
import sys


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QGridLayout()
        self.setLayout(layout)
        
        # Each of the buttons opens a file dialog

        button_color = QPushButton('Show color dialog')
        button_file = QPushButton('Show file dialog')
        button_font = QPushButton('Show font dialog')
        button_input = QPushButton('Show input dialog')
        
        # Each label is affected by dialog return value
        
        self.label_color = QLabel('Color label')
        self.label_file = QLabel('File label')
        self.label_font = QLabel('Font label')
        self.label_input = QLabel('Input label')
               
        layout.addWidget(button_color, 0, 0)
        layout.addWidget(button_file, 1, 0)
        layout.addWidget(button_font, 2, 0)
        layout.addWidget(button_input, 3, 0)
        
        layout.addWidget(self.label_color, 0, 1)
        layout.addWidget(self.label_file, 1, 1)
        layout.addWidget(self.label_font, 2, 1)
        layout.addWidget(self.label_input, 3, 1)
        
        button_color.clicked.connect(self.on_button_color_clicked)
        button_file.clicked.connect(self.on_button_file_clicked)
        button_font.clicked.connect(self.on_button_font_clicked)
        button_input.clicked.connect(self.on_button_input_clicked) 
        
        
    def on_button_color_clicked(self):
        
        # 1 - Create the dialog using one of the static functions
        #     The function return value contains user selection
        #     QColorDialog.getColor()   returns a QColor instance
        
        color = QColorDialog.getColor()
        style_sheet = 'QLabel {background-color: ' + color.name() + '}'
         
        # 2 - Use the return value
         
        self.label_color.setStyleSheet(style_sheet)
        
    # 3 - Repeat for each of your dialogs
    
    def on_button_file_clicked(self):
        
        # QFDileDialog.getOpenFileName() returns a QStringList
        # There are other static functions as well.
        
        file_path = QFileDialog.getOpenFileName()[0]
        file = QFile(file_path)
        file_info = QFileInfo(file)
        self.label_file.setText(file_info.fileName())
        
        
    def on_button_font_clicked(self):
        
        # QFontDialog.getFont() returns (bool, QFont).
        
        font = QFontDialog.getFont()
        self.label_font.setFont(font[1])
        
        
    def on_button_input_clicked(self):
        
        # QInputDialog.getText() returns (QString, bool)
        # You can also use getDouble(), getInt(), getItem()
        # and getMultiLineText().
        
        text = QInputDialog.getText(
                self, 'Enter text', 'Some text')
        self.label_input.setText(text[0])


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())