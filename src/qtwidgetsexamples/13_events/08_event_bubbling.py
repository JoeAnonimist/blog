import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QWidget, QLineEdit, QLabel,
    QGroupBox, QVBoxLayout, QPushButton, QFrame)


class MyGroupBox(QGroupBox):

    def mousePressEvent(self, event):
        print(f'Mouse press bubbled to {self.objectName()}')
        super().mousePressEvent(event)

    def keyPressEvent(self, event):
        print(f'Key press bubbled to {self.objectName()}: {event.text()}')
        super().keyPressEvent(event)


class MyCustomLineEdit(QLineEdit):

    def mousePressEvent(self, event):
        event.ignore()
        super().mousePressEvent(event)

    def keyPressEvent(self, event):
        event.ignore()
        super().keyPressEvent(event)


class MyCustomLabel(QLabel):

    def mousePressEvent(self, event):
        event.ignore()
        super().mousePressEvent(event)

    def keyPressEvent(self, event):
        event.ignore()
        super().keyPressEvent(event)


class MyCustomFrame(QFrame):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFrameShape(QFrame.Box)
        self.setFrameShadow(QFrame.Sunken)
        self.setLineWidth(2)
        self.setMinimumHeight(50)

    def mousePressEvent(self, event):
        event.ignore()
        print("Mouse clicked on Frame")
        #super().mousePressEvent(event)

    def keyPressEvent(self, event):
        event.ignore()
        print("Key pressed on Frame:", event.text())
        #super().keyPressEvent(event)


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setObjectName('MainWindow')

        layout = QVBoxLayout(self)
        self.setLayout(layout)

        self.groupbox1 = MyGroupBox("GroupBox1")
        self.groupbox1.setObjectName("GroupBox1")

        self.groupbox2 = MyGroupBox("GroupBox2", self.groupbox1)
        self.groupbox2.setObjectName("GroupBox2")

        self.label = MyCustomLabel("Label", self.groupbox2)
        self.label.setFocusPolicy(Qt.StrongFocus)

        self.line_edit = MyCustomLineEdit("LineEdit", self.groupbox2)

        self.frame = MyCustomFrame(self.groupbox2)
        self.frame.setFocusPolicy(Qt.StrongFocus)

        self.label.show()
        self.line_edit.hide()
        self.frame.hide()
        self.current_index = 0
        self.widgets = [self.label, self.line_edit, self.frame]

        layout2 = QVBoxLayout(self.groupbox2)
        for w in self.widgets:
            layout2.addWidget(w)

        layout1 = QVBoxLayout(self.groupbox1)
        layout1.addWidget(self.groupbox2)

        self.button = QPushButton("Switch Widget")
        self.button.clicked.connect(self.on_button_clicked)
        layout1.addWidget(self.button)

        layout.addWidget(self.groupbox1)
        layout.addStretch()

    def on_button_clicked(self):

        self.widgets[self.current_index].hide()
        self.current_index = (self.current_index + 1) % len(self.widgets)
        self.widgets[self.current_index].show()
        self.widgets[self.current_index].setFocus()
        print(f"Switched to {type(self.widgets[self.current_index]).__name__}")

    def mousePressEvent(self, event):
        print("Mouse pressed bubbled to Window")
        super().mousePressEvent(event)
        
    def keyPressEvent(self, event):
        print(f'Key press bubbled to Window', event.text())
        super().keyPressEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
