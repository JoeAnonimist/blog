import sys
from PySide6.QtCore import Signal, QEvent
from PySide6.QtWidgets import (QApplication, 
    QWidget, QPushButton, QVBoxLayout)


class Window(QWidget):
    
    custom_signal = Signal()
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.button = QPushButton('Click me!')
        layout.addWidget(self.button)
        
        self.button.clicked.connect(self.on_button_clicked)
        
        self.custom_signal.connect(self.on_custom_signal_1)
        self.custom_signal.connect(self.on_custom_signal_2)
        self.custom_signal.connect(self.on_custom_signal_3)
    
    def on_button_clicked(self):
        print('on_button_clicked: Emitting custom signal\n')
        self.custom_signal.emit()
        print('on_button_clicked: Returning')
        
    def on_custom_signal_1(self):
        print('First custom slot executed')
        
    def on_custom_signal_2(self):
        print('Second custom slot executed')
        
        
    def on_custom_signal_3(self):
        print('Third custom slot executed\n')
        
    def event(self, event):
        if event.type() == QEvent.Type.MetaCall:
            print(f"Queued signal (MetaCallEvent) intercepted")
        return QWidget.event(self, event)


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()
    
    sys.exit(app.exec())

