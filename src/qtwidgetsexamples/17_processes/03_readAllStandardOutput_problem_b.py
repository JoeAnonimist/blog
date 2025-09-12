import sys
from PySide6.QtCore import QProcess
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QTextEdit, QCheckBox, QLabel
)

# Subprocess script: Outputs a long string in small chunks, with delays and partial lines.
SUBPROCESS_SCRIPT = """
import sys
import time

text = "This is a long demonstration sentence that will be split into arbitrary chunks without regard for newlines or word boundaries. Repeat: "
full_text = text * 5  # Make it longer

# Write in small, timed bursts (simulate streaming output)
for i in range(0, len(full_text), 20):  # 20-byte chunks
    sys.stdout.write(full_text[i:i+20])
    sys.stdout.flush()  # Force flush to trigger readyRead
    if i % 100 == 0:
        sys.stderr.write("Error chunk at offset {}!\\n".format(i))
        sys.stderr.flush()
    time.sleep(0.1)  # Slow it down for visibility
"""

class ChunkDemoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QProcess Chunk Pitfalls Demo (Bad Mode)")

        # Text edit with sans-serif font and larger size
        self.text_edit = QTextEdit(readOnly=True)
        self.text_edit.setFont(QFont("Arial"))  # Sans-serif, 14pt

        # Run button
        self.run_button = QPushButton("Run (Bad Chunk Handling)")
        self.run_button.clicked.connect(self.run_process)

        # Checkbox
        self.show_raw_checkbox = QCheckBox("Show Raw Chunks (with splits visible)")
        self.show_raw_checkbox.setChecked(True)

        # Layout
        layout = QVBoxLayout(self)
        label = QLabel("Demo: Treating chunks as full lines (pitfall: partial/garbled output)")
        layout.addWidget(label)
        layout.addWidget(self.text_edit)
        layout.addWidget(self.run_button)
        layout.addWidget(self.show_raw_checkbox)

        self.process = None

    def run_process(self):
        self.text_edit.clear()
        self.text_edit.append("--- Starting Bad Mode (Naive Chunk Handling) ---")

        self.process = QProcess(self)
        self.process.readyReadStandardOutput.connect(self.handle_stdout)
        self.process.readyReadStandardError.connect(self.handle_stderr)
        self.process.finished.connect(lambda: self.text_edit.append("\n--- Process Finished ---"))

        # Run script inline using sys.executable -c
        self.process.start(sys.executable, ["-c", SUBPROCESS_SCRIPT])

    def handle_stdout(self):
        data = self.process.readAllStandardOutput()
        chunk = bytes(data).decode("utf-8", errors="replace")

        if self.show_raw_checkbox.isChecked():
            self.text_edit.append(f"STDOUT Chunk (len={len(chunk)}): '{chunk.replace('\\n', '\\\\n')}'")
        # Bad: Assume chunk is a full unit (pitfall: shows partial/garbled output)
        self.text_edit.append(f"Bad STDOUT (assumed full): {chunk}")

    def handle_stderr(self):
        data = self.process.readAllStandardError()
        chunk = bytes(data).decode("utf-8", errors="replace")

        if self.show_raw_checkbox.isChecked():
            self.text_edit.append(f"STDERR Chunk (len={len(chunk)}): '{chunk.replace('\\n', '\\\\n')}'")
        # Bad: No buffering, just dump
        self.text_edit.append(f"Bad STDERR (assumed full): {chunk}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ChunkDemoWindow()
    win.resize(800, 600)
    win.show()
    sys.exit(app.exec())