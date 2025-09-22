import sys
from PySide6.QtWidgets import (QApplication, 
    QWidget, QLineEdit, QPushButton, QVBoxLayout)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        self.setObjectName('Main Window')
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.show_button = QPushButton('Show widgets')
        self.show_button.clicked.connect(self.show_widgets)
        layout.addWidget(self.show_button)
        
        self.switch_button = QPushButton('Switch QLineEdit parent')
        self.switch_button.clicked.connect(self.switch_parent)
        self.switch_button.setDisabled(True)
        layout.addWidget(self.switch_button)
        
        self.widget1 = QWidget()
        self.widget1.setObjectName('widget1')
        self.widget1.setLayout(QVBoxLayout())
        
        self.widget2 = QWidget()
        self.widget2.setObjectName('widget2')
        self.widget2.setLayout(QVBoxLayout())
        
        self.edit = QLineEdit()
        self.widget1.layout().addWidget(self.edit)
        
        print('In Widget.__init__():')
        print(f'Widget 1 parent: {self.widget1.parent()}')
        print(f'Widget 2 parent: {self.widget2.parent()}')
        print(f'Line edit parent: {self.edit.parent().objectName()}')
        
    def show_widgets(self):
        
        self.show_button.setDisabled(True)
        self.switch_button.setEnabled(True)
        
        
        main_geom = self.geometry()
        spacing = 20
        
        self.widget1.resize(200, 40)
        self.widget2.resize(200, 40)
    
        x1 = main_geom.x()
        y1 = main_geom.y() + main_geom.height() + spacing
        self.widget1.move(x1, y1)
    
        x2 = x1 
        y2 = y1 + self.widget1.height() + spacing
        self.widget2.move(x2, y2)
        
        self.widget1.show()
        self.widget2.show()
        
    def switch_parent(self):
        
        self.edit.parent().layout().removeWidget(self.edit)
        
        print(self.widget1.layout().count())
        print(self.widget2.layout().count())
        
        if self.edit.parent().objectName() == 'widget1':
            self.edit.setParent(self.widget2)
        else:
            self.edit.setParent(self.widget1)

        self.edit.parent().layout().addWidget(self.edit)

        print('After parent switch:')
        print(f'Widget 1 parent: {self.widget1.parent()}')
        print(f'Widget 2 parent: {self.widget2.parent()}')
        print(f'Line edit parent: {self.edit.parent().objectName()}')


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()
    
    sys.exit(app.exec())
