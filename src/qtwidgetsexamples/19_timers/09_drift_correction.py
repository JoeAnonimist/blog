import sys
from PySide6.QtCore import QTimer, QElapsedTimer, Slot
from PySide6.QtWidgets import (QApplication, QWidget,
    QPushButton, QVBoxLayout)


class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()

        self.resize(200, 100)

        self.expected_interval = 1000  # ms
        self.correct_drift = False

        self.counter = 0
        self.cumulative_drift = 0

        self.elapsed_timer = QElapsedTimer()
        self.start_time = 0
        self.last_tick_time = self.start_time

        layout = QVBoxLayout(self)
        self.toggle_button = QPushButton('Drift Correction: Off')
        self.toggle_button.clicked.connect(self.toggle_drift_correction)
        layout.addWidget(self.toggle_button)

        self.counter = 0
        self.cumulative_drift = 0

        self.elapsed_timer.start()
        self.start_time = self.elapsed_timer.elapsed()

        print('Timer started')
        QTimer.singleShot(self.expected_interval, self.on_timeout)

    @Slot()
    def toggle_drift_correction(self):
        
        self.correct_drift = not self.correct_drift
        state = 'On' if self.correct_drift else 'Off'
        self.toggle_button.setText(f'Drift Correction: {state}')
        print(f'Drift Correction: {state}')

    def schedule_next_tick(self):

        current_time = self.elapsed_timer.elapsed()

        if self.correct_drift:
            ideal_next_time = self.start_time + (self.counter + 1) * self.expected_interval
            delay = max(0, ideal_next_time - current_time)
        else:
            delay = self.expected_interval

        QTimer.singleShot(int(delay), self.on_timeout)
    
    @Slot()
    def on_timeout(self):
        self.counter += 1
    
        current_time = self.elapsed_timer.elapsed()

        expected_total_time = self.counter * self.expected_interval
        total_drift = current_time - expected_total_time
    
        if self.counter == 1:
            tick_drift = current_time - self.start_time - self.expected_interval
        else:
            tick_drift = current_time - self.last_tick_time - self.expected_interval
    
        self.last_tick_time = current_time
    
        print(f'Tick {self.counter}: Tick Drift = {tick_drift:.1f} ms, Total Drift = {total_drift:.1f} ms')
    
        self.schedule_next_tick()



if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    
    window = Window()
    window.show()

    sys.exit(app.exec())