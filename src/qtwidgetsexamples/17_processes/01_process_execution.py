import sys
from PySide6.QtCore import QProcess
from PySide6.QtWidgets import (QApplication, QWidget,
    QPushButton, QVBoxLayout, QTextEdit)

class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.button = QPushButton('Run Command')
        self.button.clicked.connect(self.run_command)

        layout = QVBoxLayout(self)
        layout.addWidget(self.text_edit)
        layout.addWidget(self.button)

        self.process = QProcess(self)
        self.process.readyReadStandardOutput.connect(self.on_stdout)
        self.process.readyReadStandardError.connect(self.on_stderr)
        self.process.errorOccurred.connect(self.on_error_occurred)
        self.process.finished.connect(self.on_finished)

    def run_command(self):
        self.button.setDisabled(True)
        self.text_edit.clear()
        self.process.start(sys.executable, [
            '-c', 'import time\ntime.sleep(3)\nprint("Done")'])
        #self.process.start('python', ['-c', 'print("Hello")'])
        # self.process.start('python', ['-c', 'prin("Hello")'])
        # self.process.start('pytho', ['-c', 'print("Hello")'])

    def on_stdout(self):
        output = self.process.readAllStandardOutput().data().decode()
        self.text_edit.setText(output)
        
    def on_stderr(self):
        output = self.process.readAllStandardError().data().decode()
        self.text_edit.setText(output)
        
    def on_error_occurred(self, e):
        print(self.process.error())
        self.text_edit.setText(e.name)
        
    def on_finished(self):
        print('process finished')
        self.button.setEnabled(True)

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    
    window = Window()
    window.show()
    
    sys.exit(app.exec())
