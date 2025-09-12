import sys
import os
import platform
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit
from PySide6.QtCore import QProcess

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("readAllStandardOutput() Borked Lines Demo")

        self.text_edit = QTextEdit(readOnly=True)
        self.button_naive = QPushButton("Run Naive (Show Borked Only)")
        self.button_buffered = QPushButton("Run Buffered (Show All)")
        self.button_naive.clicked.connect(lambda: self.run_process(naive=True))
        self.button_buffered.clicked.connect(lambda: self.run_process(naive=False))

        layout = QVBoxLayout(self)
        layout.addWidget(self.text_edit)
        layout.addWidget(self.button_naive)
        layout.addWidget(self.button_buffered)

        self.process = QProcess(self)
        self.process.readyReadStandardOutput.connect(self.on_stdout)
        self.process.finished.connect(self.on_finished)
        self.process.readyReadStandardError.connect(self.on_stderr)

        # Initialize for buffering
        self.buffer = ""
        self.naive_mode = True
        self.partial_count = 0  # Count partial lines
        self.line_count = 0    # Count complete lines

    def run_process(self, naive=True):
        self.text_edit.clear()
        self.buffer = ""
        self.partial_count = 0
        self.line_count = 0
        self.naive_mode = naive
        self.text_edit.append(f"Running {'Naive (Borked Only)' if naive else 'Buffered (All)'} Mode\n{'='*30}\n")
        
        # Choose command for recursive filename listing from home directory
        home_dir = os.path.expanduser("~")
        if platform.system() == "Windows":
            # Use cmd.exe to run for loop
            cmd = ["cmd.exe", "/c", f"cd /d {home_dir} && for /r %i in (*) do @echo %~ni"]
        else:
            # Use find to list filenames only
            cmd = ["find", home_dir, "-type", "f", "-printf", "%f\n"]
        
        self.process.start(cmd[0], cmd[1:])

    def on_stdout(self):
        raw = self.process.readAllStandardOutput().data().decode(errors='replace')
        print(f"Raw chunk: {repr(raw)}")  # Debug: Show chunk boundaries
        if self.naive_mode:
            # Naive: Show only partial (borked) lines
            lines = raw.split('\n')
            for line in lines[:-1]:
                if line.strip():
                    self.line_count += 1  # Count complete lines silently
            if lines[-1]:
                self.text_edit.append(f"Partial: {lines[-1]}")  # Show only partial
                self.partial_count += 1
        else:
            # Buffered: Show all complete lines
            self.buffer += raw
            lines = self.buffer.split('\n')
            self.buffer = lines[-1]  # Keep partial
            for line in lines[:-1]:
                if line.strip():
                    self.text_edit.append(f"Got: {line}")
                    self.line_count += 1

    def on_stderr(self):
        raw = self.process.readAllStandardError().data().decode(errors='replace')
        self.text_edit.append(f"Stderr: {raw}")

    def on_finished(self):
        # Process remaining buffer in buffered mode
        if not self.naive_mode and self.buffer:
            lines = self.buffer.split('\n')
            for line in lines:
                if line.strip():
                    self.text_edit.append(f"Got: {line}")
                    self.line_count += 1
        if self.naive_mode:
            self.text_edit.append(f"== Process finished ==\nPartial lines: {self.partial_count}\nComplete lines (not shown): {self.line_count}")
        else:
            self.text_edit.append(f"== Process finished ==\nTotal lines: {self.line_count}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec())