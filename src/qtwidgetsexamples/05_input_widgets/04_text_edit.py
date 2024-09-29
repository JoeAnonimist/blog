# The QTextEdit class provides a widget that is used 
# to edit and display both plain and rich text.

from PySide6.QtWidgets import (QApplication, 
    QWidget, QVBoxLayout, QTextEdit, QLabel)
import sys


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1 - Create the text edit widget
        
        self.text_edit = QTextEdit()
        
        # QTextEdit supports an HTML subset:
        
        html = '''
<div style="color: red;">This line is red</div>
<div style="font-size: 14px;">This line is 14px</div>
<div style="font-weight: bold;">This line is bold</div>
<div style="background-color: LightGray;">You can edit me.</div>
<div>Use Ctrl-v, Ctrl-c and other key bindings to manipulate the text.</div>
'''
        
        # 2 - Add formatted text to the widget
        
        self.text_edit.setHtml(html)
        self.text_edit.textChanged.connect(self.on_text_changed)
        layout.addWidget(self.text_edit)
        
        self.label = QLabel()
        layout.addWidget(self.label)
        
    # 3 - Access the plain text using
    #     QTextEdit.document().toPlainText()
        
    def on_text_changed(self):
        print(self.text_edit.document().toPlainText())
        self.label.setText(
            self.text_edit.document().toPlainText())


if __name__ == '__main__':

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())