import sys
from PySide6.QtCore import QPropertyAnimation, Signal, Property, QSequentialAnimationGroup, QPauseAnimation
from PySide6.QtWidgets import (QApplication, 
    QWidget, QPushButton, QVBoxLayout)


class MyButton(QPushButton):
    
    borderChanged = Signal(int)
    
    def __init__(self, parent):
        
        super().__init__(parent)
        self._border = 0
        
        self.borderChanged.connect(self.on_border_changed)        
        
    def setBorder(self, value):
        if value != self._border:
            self._border = value
            print(value)
            self.borderChanged.emit(value)
            
    def getBorder(self):
        return self._border
    
    border = Property(int, fget = getBorder, fset=setBorder, notify=borderChanged)
    
    def on_border_changed(self):
        qss = f'''
            QPushButton {{ border: {self._border}px solid orange; }}
        '''
        self.setStyleSheet(qss)
        self.style().unpolish(self)
        self.style().polish(self)
        self.update()
        
    def reset_style(self):
        self.setStyleSheet('')        


class Window(QWidget):
    
    def __init__(self, parent=None):

        super().__init__(parent)

        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.button = MyButton(self)
        self.button.setText('Animated button')
        self.button.border = 0
        
        self.button.clicked.connect(self.on_button_clicked)
        
        self.anim_group = QSequentialAnimationGroup(self)
        
        for _ in range(3):
            anim_on = QPropertyAnimation(self.button, b'border')
            anim_on.setDuration(0)
            anim_on.setEndValue(1)
            self.anim_group.addAnimation(anim_on)
            
            pause_on = QPauseAnimation(300)
            self.anim_group.addAnimation(pause_on)
            
            anim_off = QPropertyAnimation(self.button, b'border')
            anim_off.setDuration(0)
            anim_off.setEndValue(0)
            self.anim_group.addAnimation(anim_off)
            
            pause_off = QPauseAnimation(300)
            self.anim_group.addAnimation(pause_off)
        
        self.anim_group.finished.connect(self.button.reset_style)

        layout.addWidget(self.button)
        
    def on_button_clicked(self):
        print('button clicked')
        self.anim_group.start()

if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())