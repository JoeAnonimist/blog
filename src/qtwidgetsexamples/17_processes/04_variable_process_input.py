import sys
from random import randint
from PySide6.QtCore import QProcess, QTextStream
from PySide6.QtWidgets import (QApplication, QWidget,
    QPushButton, QVBoxLayout, QTextEdit)

script_text = '''
import sys

low = 1
high = 100

while low <= high:
    guess = (low + high) // 2
    print(f"My guess is {guess}")
    feedback = input("Enter 'c' if correct, 'h' if too high, 'l' if too low: ").lower()
    if feedback == 'c':
        print("I guessed it!")
        break
    elif feedback == 'h':
        high = guess - 1
    elif feedback == 'l':
        low = guess + 1
    else:
        print("Invalid input, try again.")
'''

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
        self.my_number = randint(1, 100)
        self.button.setDisabled(True)
        self.text_edit.clear()
        self.text_edit.append(f"Secret number: {self.my_number}\n" + "="*30 + "\n")  # Show for demo
        self.process.start(sys.executable, ['-c', script_text])

    def on_stdout(self):
        stream = QTextStream(self.process)
        while not stream.atEnd():
            line = stream.readLine().strip()
            if line:
                self.text_edit.append(line)
                if "My guess is" in line:
                    try:
                        guess_str = line.split("My guess is ")[1].strip()
                        guess = int(guess_str)
                        if guess == self.my_number:
                            feedback = b'c\n'
                            self.process.write(feedback)
                            self.process.closeWriteChannel()
                            print(f"Sent feedback: {feedback.decode().strip()} for guess {guess}")
                        elif guess > self.my_number:
                            feedback = b'h\n'
                            self.process.write(feedback)
                            print(f"Sent feedback: {feedback.decode().strip()} for guess {guess}")
                        else:
                            feedback = b'l\n'
                            self.process.write(feedback)
                            print(f"Sent feedback: {feedback.decode().strip()} for guess {guess}")
                    except (IndexError, ValueError):
                        pass  # Ignore malformed guess lines


    def on_stderr(self):
        stream = QTextStream(self.process)
        while not stream.atEnd():
            line = stream.readLine().strip()
            if line:
                self.text_edit.append("STDERR: " + line)

    def on_error_occurred(self):
        self.text_edit.append("ERROR: " + self.process.errorString())
        self.button.setEnabled(True)
        
    def on_finished(self):
        print('process finished')
        self.button.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())