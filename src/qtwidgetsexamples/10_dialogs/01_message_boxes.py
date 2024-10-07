
import sys
from PySide6.QtWidgets import (QApplication, 
    QWidget, QPushButton, QVBoxLayout, QMessageBox)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)
        
        button = QPushButton('Show msgbox')
        layout.addWidget(button)
        
        button.clicked.connect(self.on_button_clicked)
        
    def on_button_clicked(self):
        
        msg_box = QMessageBox()
        msg_box.setText('Some message')
        msg_box.setStandardButtons(
            QMessageBox.Yes | 
            QMessageBox.No | 
            QMessageBox.YesToAll | 
            QMessageBox.NoToAll)
        ret = msg_box.exec()
        print(ret)
      

if __name__ == '__main__':

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
