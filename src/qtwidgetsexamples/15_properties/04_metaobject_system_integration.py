import sys
from PySide6.QtCore import Property, Signal
from PySide6.QtWidgets import (QApplication, QWidget,
    QLabel, QPushButton, QVBoxLayout)


class MyLabel(QLabel):
    
    colorChanged = Signal(str, str)
    bgColorChanged = Signal()
    
    def __init__(self, text, parent):
        
        super().__init__(text, parent)
        
        self._color = 'black'
        self._background_color = 'lightgrey'
    
    def color(self):
        return self._color
    
    def setColor(self, color):
        
        if color != self._color:
            old_color = self._color
            self._color = color
            self.colorChanged.emit(old_color, color)
            
    def resetColor(self):
        if self._color != 'black':
            old_color = self._color
            self._color = 'black'
            self.colorChanged.emit(old_color, 'black')
            
        
    color = Property(str, fget=color, fset=setColor,
                     notify=colorChanged, freset=resetColor)

    @Property(str, notify=bgColorChanged)
    def backgroundColor(self):
        return self._background_color
    
    @backgroundColor.setter
    def backgroundColor(self, background_color):
        
        if background_color != self._background_color:
            self._background_color = background_color
            self.bgColorChanged.emit()


class Window(QWidget):
    
    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.label = MyLabel('Hello, World!', self)
        layout.addWidget(self.label)
        
        button = QPushButton('List properties')
        layout.addWidget(button)
        button.clicked.connect(self.on_button_clicked)
        
    def on_button_clicked(self):
        
        count = self.label.metaObject().propertyCount()
        print(f"{'Name':<20} {'Type':<25} "
              f"{'Scriptable':<12} {'Stored':<8}")
        for i  in range(count):
            property = self.label.metaObject().property(i)
            print(f"{property.name():<20} "
                f"{property.metaType().name():<25} "
                f"{str(property.isScriptable()):<12} "
                f"{str(property.isStored()):<8}")
    
    def on_reset_clicked(self):
        pass
        

if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())