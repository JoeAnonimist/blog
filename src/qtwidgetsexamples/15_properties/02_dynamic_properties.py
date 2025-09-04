import sys
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import (QApplication, QWidget,
    QLineEdit, QVBoxLayout)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setPlaceholderText(
            'Enter a number between 1 and 100')
        layout.addWidget(self.lineEdit)
        
        self.validator = QIntValidator(1, 100)
        
        qss = '''
            QLineEdit[error=true] { border: 1px solid orange; }
            QLineEdit[error=false] { border: 1px solid gray; }
        '''
        self.setStyleSheet(qss)
        
        self.lineEdit.textChanged.connect(self.validateInput)
        self.validateInput(self.lineEdit.text())
    
    def validateInput(self, text):
        
        cursor_pos = self.lineEdit.cursorPosition()
        state, _, _ = self.validator.validate(text, cursor_pos) 
        is_valid = state == QIntValidator.State.Acceptable

        self.lineEdit.setProperty("error", not is_valid)
        
        self.lineEdit.style().unpolish(self.lineEdit)
        self.lineEdit.style().polish(self.lineEdit)
        self.lineEdit.update()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
