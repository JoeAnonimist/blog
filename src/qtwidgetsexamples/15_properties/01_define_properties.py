'''
The READ function is const and returns the property type.
The WRITE function returns void and has exactly
one parameter of the property type.
The meta-object compiler enforces these requirements.
'''

import sys
from PySide6.QtCore import Property, Signal
from PySide6.QtWidgets import (QApplication, QWidget,
    QLabel, QPushButton, QVBoxLayout)



class MyLabel(QLabel):
    
    STYLE = 'MyLabel {{background-color: {}; color: {};}}'
    
    colorChanged = Signal(str, str)
    bgColorChanged = Signal()
    styleChanged = Signal(str)
    
    def __init__(self, text, parent):
        
        super().__init__(text, parent)
        
        self._color = 'black'
        self._background_color = 'lightgrey'
        self._style = ''
        
        self.setStyle()
        
        self.colorChanged.connect(self.setStyle)
        self.bgColorChanged.connect(self.setStyle)
    
    def color(self):
        return self._color
    
    def setColor(self, color):
        
        if color != self._color:
            old_color = self._color
            self._color = color
            self.colorChanged.emit(old_color, color)
            
        
    color = Property(str, fget=color, fset=setColor, notify=colorChanged)
        
    @Property(str, notify=bgColorChanged)
    def backgroundColor(self):
        return self._background_color
    
    @backgroundColor.setter
    def backgroundColor(self, background_color):
        
        if background_color != self._background_color:
            self._background_color = background_color
            self.bgColorChanged.emit()

    def getStyle(self):
        return self._style
    
    def setStyle(self):
        self._style = self.STYLE.format(
            self._background_color, self.color)
        self.setStyleSheet(self._style)
        self.styleChanged.emit(self._style)
                
    style = Property(str, fget=getStyle, notify=styleChanged)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.label = MyLabel('Hello, World!', self)
        self.label.colorChanged.connect(self.on_color_changed)
        self.label.bgColorChanged.connect(self.on_bg_color_changed)
        self.label.styleChanged.connect(self.on_style_changed)

        layout.addWidget(self.label)
        
        button = QPushButton('Change colors')
        layout.addWidget(button)
        button.clicked.connect(self.on_button_clicked)
        
    def on_color_changed(self, old, new):
        print('color changed: ', old, new)
        
    def on_bg_color_changed(self):
        print('background color changed')
        
    def on_style_changed(self, style):
        print('Style changed: ', style)
        
    def on_button_clicked(self):
        self.label.color = '#fff'
        self.label.backgroundColor = 'steelblue'


if __name__ == '__main__':

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())