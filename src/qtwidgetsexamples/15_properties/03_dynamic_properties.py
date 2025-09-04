import sys
from PySide6.QtWidgets import (QApplication, QWidget,
    QLineEdit, QPushButton, QVBoxLayout)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.usernameEdit = QLineEdit(self)
        self.usernameEdit.setProperty('role', 'required')
        layout.addWidget(self.usernameEdit)
        
        self.emailEdit = QLineEdit(self)
        self.emailEdit.setProperty('role', 'required')
        layout.addWidget(self.emailEdit)
        
        self.title_edit = QLineEdit()
        self.title_edit.setProperty('role', 'optional')
        layout.addWidget(self.title_edit)
        
        qss = '''
            QLineEdit[role="required"] {border: 1px solid orange;}
            QLineEdit[role="optional"] {border: 1px solid green;}
        '''
        self.setStyleSheet(qss)

        for widget in [self.usernameEdit, self.emailEdit]:
            widget.style().unpolish(widget)
            widget.style().polish(widget)
            widget.update()
        
        button = QPushButton('Process Form')
        button.clicked.connect(self.processForm)
        layout.addWidget(button)
        
        for name in self.title_edit.dynamicPropertyNames():
            print(name.toStdString())
    
    def processForm(self):

        for widget in self.findChildren(QLineEdit):
            role = widget.property("role")
            value = widget.text()
            print(f'Widget Role: {role}, Value: {value}')


if __name__ == '__main__':

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    
    window = Window()
    window.show()
    sys.exit(app.exec())