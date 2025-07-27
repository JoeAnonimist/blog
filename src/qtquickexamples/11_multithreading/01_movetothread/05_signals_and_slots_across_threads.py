import sys

from PySide6.QtCore import QObject, QThread, Signal, Slot, Property, Qt
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, QmlElement


QML_IMPORT_NAME = 'examples.workerthread'
QML_IMPORT_MAJOR_VERSION = 1

class Worker(QObject):
    
    auto_signal = Signal()
    direct_signal = Signal()
    queued_signal = Signal()
    blocking_signal = Signal()
    
    @Slot()
    def auto_slot(self):
        print('Auto connection')
        print('In', QThread.currentThread().objectName(),
            ', Loop level', QThread.currentThread().loopLevel())

    @Slot()
    def direct_slot(self):
        print('Direct connection')
        print('In', QThread.currentThread().objectName(),
            ', Loop level', QThread.currentThread().loopLevel())
    @Slot()
    def queued_slot(self):
        print('Queued connection')
        print('In', QThread.currentThread().objectName(),
            ', Loop level', QThread.currentThread().loopLevel())
        
    @Slot()
    def blocking_slot(self):
        print('Blocking Queued connection')
        print('In', QThread.currentThread().objectName(),
            ', Loop level', QThread.currentThread().loopLevel())
        QThread.sleep(10)

        
@QmlElement
class Controller(QObject):
    
    emitter = None
    receiver = None
    
    def __init__(self, parent=None):
        
        super().__init__(parent)
        QGuiApplication.instance().aboutToQuit.connect(self.cleanup)
        
        QThread.currentThread().setObjectName('Main thread')
    
        self.emitting_thread = QThread()
        self.emitting_thread.setObjectName('Emitting Thread')
        
        self.emitter_obj = Worker()
        self.emitter_obj.moveToThread(self.emitting_thread)
        
        self.receiving_thread = QThread()
        self.receiving_thread.setObjectName('Receiving Thread')
        
        self.receiver_obj = Worker()
        self.receiver.moveToThread(self.receiving_thread)
        
        self.emitter_obj.auto_signal.connect(self.receiver_obj.auto_slot, Qt.ConnectionType.AutoConnection)
        self.emitter_obj.direct_signal.connect(self.receiver_obj.direct_slot, Qt.ConnectionType.DirectConnection)
        self.emitter_obj.queued_signal.connect(self.receiver_obj.queued_slot, Qt.ConnectionType.QueuedConnection)
        self.emitter_obj.blocking_signal.connect(self.receiver_obj.blocking_slot, Qt.ConnectionType.BlockingQueuedConnection)
        
        self.emitting_thread.start()
        self.receiving_thread.start()
        
    def getEmitter(self):
        return self.emitter_obj

    emitter = Property(QObject, fget=getEmitter)
    
    def getReceiver(self):
        return self.receiver_obj

    receiver = Property(QObject, fget=getReceiver)

    @Slot(result=str)
    def print_current_thread(self):
        return QThread.currentThread().objectName()

    @Slot()
    def cleanup(self):
        print("Cleaning up...")
        try:
            self.emitting_thread.requestInterruption()
            self.emitting_thread.quit()
            self.emitting_thread.wait()
            self.receiving_thread.requestInterruption()
            self.receiving_thread.quit()
            self.receiving_thread.wait()
        except Exception as e:
            print(e)


if __name__ == '__main__':

    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('05_signals_and_slots_across_threads.qml')

    sys.exit(app.exec())