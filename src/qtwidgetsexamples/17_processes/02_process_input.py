import sys
from PySide6.QtCore import QProcess
from PySide6.QtWidgets import (QApplication, QWidget,
    QPushButton, QVBoxLayout, QTextEdit)

script_text = '''
name = input()
print(f"Hello {name}")
x = int(input())
print("you entered ", x)
y = int(input())
print("you entered ", y)
print("x + y = ", x + y)
'''

input_args = [b'Joe\n', b'1\n', b'1\n']


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
        self.process.stateChanged.connect(self.on_state_changed)
        self.process.finished.connect(self.on_finished)

    def run_command(self):
        self.button.setDisabled(True)
        self.text_edit.clear()
        self.process.start(sys.executable, ['-c', script_text])

    def on_stdout(self):
        output = self.process.readAllStandardOutput().data().decode()
        self.text_edit.setText(output)
        
    def on_stderr(self):
        output = self.process.readAllStandardError().data().decode()
        self.text_edit.setText(output)
        
    def on_error_occurred(self):
        self.text_edit.setText(self.process.errorString())
        self.button.setEnabled(True)
        
    def on_state_changed(self, state):
        if state == QProcess.ProcessState.Running:
            for arg in input_args:
                bytes_written = self.process.write(arg)
                print(bytes_written)
                if bytes_written == -1:
                    print(self.process.errorString())
            self.process.closeWriteChannel()
        
    def on_finished(self):
        print('process finished')
        self.button.setEnabled(True)

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    
    window = Window()
    window.show()
    
    sys.exit(app.exec())
