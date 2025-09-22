import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QWidget,
    QGroupBox, QVBoxLayout, QPushButton, QLabel)


class SubTreeWidget(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setObjectName('Subtree')

        layout = QVBoxLayout(self)

        self.label = QLabel('A subtree label')
        layout.addWidget(self.label)

        self.button = QPushButton('Set group checkable')
        self.button.setCheckable(True)
        layout.addWidget(self.button)


class MainWindow(QWidget):
    
    def __init__(self):
        
        super().__init__()

        layout = QVBoxLayout(self)

        self.group1 = QGroupBox('Group 1')
        self.group1.setLayout(QVBoxLayout())
        self.group1.setObjectName('Group 1')
        layout.addWidget(self.group1)

        self.group2 = QGroupBox('Group 2')
        self.group2.setLayout(QVBoxLayout())
        self.group2.setObjectName('Group 2')
        layout.addWidget(self.group2)

        self.subtree = SubTreeWidget()
        self.group1.layout().addWidget(self.subtree)

        self.switch_button = QPushButton('Move Subtree')
        layout.addWidget(self.switch_button)
        self.switch_button.clicked.connect(self.move_subtree)

        self.subtree.button.clicked.connect(
            self.toggle_current_group_checkable)

    @Slot(bool)
    def toggle_current_group_checkable(self, checked):
        current_group = self.subtree.parent()
        if current_group:
            current_group.setCheckable(checked)

    def move_subtree(self):
        
        old_parent = self.subtree.parent()
        if not old_parent:
            return

        self.subtree.button.clicked.disconnect(
            self.toggle_current_group_checkable)

        old_parent.layout().removeWidget(self.subtree)
        old_parent.setCheckable(False)
        
        if old_parent == self.group1:
            new_parent = self.group2
        else:
            new_parent = self.group1

        self.subtree.setParent(new_parent)
        new_parent.layout().addWidget(self.subtree)

        if self.subtree.button.isChecked():
            new_parent.setCheckable(True)

        self.subtree.button.clicked.connect(
            self.toggle_current_group_checkable)
        print(f'Parent: {new_parent.objectName()}')


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    
    win = MainWindow()
    win.show()
    
    sys.exit(app.exec())
