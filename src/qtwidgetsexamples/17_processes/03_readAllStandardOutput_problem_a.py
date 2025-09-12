import sys
import os
import platform
from PySide6.QtCore import QProcess
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QVBoxLayout, QTextEdit, QHBoxLayout
)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QProcess Split Output Demo (Crossplatform)")

        self.text_edit = QTextEdit(readOnly=True)

        # Buttons
        self.run_button = QPushButton("Run command")
        self.run_button.clicked.connect(self.run_command)

        self.stop_button = QPushButton("Stop command")
        self.stop_button.clicked.connect(self.stop_command)
        self.stop_button.setEnabled(False)

        # Layouts
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.run_button)
        button_layout.addWidget(self.stop_button)

        layout = QVBoxLayout(self)
        layout.addWidget(self.text_edit)
        layout.addLayout(button_layout)

        # Process
        self.process = QProcess(self)
        self.process.readyReadStandardOutput.connect(self.handle_stdout)
        self.process.readyReadStandardError.connect(self.handle_stderr)
        self.process.finished.connect(self.process_finished)

    def run_command(self):
        self.text_edit.clear()

        if platform.system() == "Windows":
            home_dir = os.path.expanduser("~")
            self.process.start("cmd.exe", ["/C", f"dir /s \"{home_dir}\""])
        else:
            self.process.start("bash", ["-c", "find /usr -type f -printf '%p\\n' 2>&1"])

        self.run_button.setEnabled(False)
        self.stop_button.setEnabled(True)

    def stop_command(self):
        if self.process.state() == QProcess.Running:
            self.process.kill()
            self.text_edit.append("\n--- Process killed ---")
        self.run_button.setEnabled(True)
        self.stop_button.setEnabled(False)

    def _append_chunk(self, label: str, text: str):
        if not text:
            return
        preview_len = 50
        if len(text) > preview_len * 2:
            begin = text[:preview_len].replace("\n", "\\n")
            end = text[-preview_len:].replace("\n", "\\n")
            msg = f"{label} (len={len(text)}): '{begin}' ... '{end}'"
        else:
            one_line = text.replace("\n", "\\n")
            msg = f"{label} (len={len(text)}): '{one_line}'"
        self.text_edit.append(msg)

    def handle_stdout(self):
        data = self.process.readAllStandardOutput()
        text = bytes(data).decode("utf-8", errors="replace")
        self._append_chunk("STDOUT CHUNK", text)

    def handle_stderr(self):
        data = self.process.readAllStandardError()
        text = bytes(data).decode("utf-8", errors="replace")
        self._append_chunk("STDERR CHUNK", text)

    def process_finished(self):
        self.text_edit.append("\n--- Process finished ---")
        self.run_button.setEnabled(True)
        self.stop_button.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.resize(900, 600)
    win.show()
    sys.exit(app.exec())
