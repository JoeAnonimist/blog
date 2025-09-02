import sys
from PySide6.QtCore import QObject, SIGNAL, SLOT, QMetaMethod, Qt
from PySide6.QtWidgets import QApplication, QLabel, QScrollBar


# Example slot functions
def handler():
    print("handler() called")

def context_handler():
    print("context-bound handler() called")

class Receiver(QObject):
    def __init__(self):
        super().__init__()

    def cleanup(self):
        print("Receiver.cleanup() called")

    def onFired(self):
        print("Receiver.onFired() called")


class Demo(QObject):
    def __init__(self):
        super().__init__()
        self.receiver = Receiver()

        # ------------------------------------------------
        print("\n1. connect(signal: str, functor)")
        # Legacy
        self.connect(SIGNAL("fired()"), handler)
        # Modern
        # (simulate "fired" as destroyed for demo)
        self.destroyed.connect(handler)

        # ------------------------------------------------
        print("\n2. static connect(sender, signal: str, functor)")
        sender = QObject()
        # Legacy
        QObject.connect(sender, SIGNAL("destroyed()"), handler)
        # Modern
        sender.destroyed.connect(handler)
        sender.deleteLater()

        # ------------------------------------------------
        print("\n3. connect(sender, signal: str, member: str)")
        sender = QObject()
        # Legacy
        self.connect(sender, SIGNAL("destroyed()"), SLOT("cleanup()"))
        # Modern
        sender.destroyed.connect(self.receiver.cleanup)
        sender.deleteLater()

        # ------------------------------------------------
        print("\n4. connect(signal: str, receiver, method: str)")
        # Legacy
        self.connect(SIGNAL("destroyed()"), self.receiver, SLOT("onFired()"))
        # Modern
        self.destroyed.connect(self.receiver.onFired)

        # ------------------------------------------------
        print("\n5. static connect(sender, QMetaMethod, receiver, QMetaMethod)")
        sender = QObject()
        sig = sender.metaObject().method(
            sender.metaObject().indexOfSignal("destroyed(QObject*)"))
        slot = self.receiver.metaObject().method(
            self.receiver.metaObject().indexOfSlot("deleteLater()"))
        # Legacy
        QObject.connect(sender, sig, self.receiver, slot)
        # Modern
        sender.destroyed.connect(self.receiver.deleteLater)
        sender.deleteLater()

        # ------------------------------------------------
        print("\n6. static connect(sender, signal: str, context, functor)")
        sender = QObject()
        context = QObject()
        
        # Legacy (string-based)
        QObject.connect(sender, SIGNAL("destroyed()"), context, SLOT("deleteLater()"))
        
        # Modern equivalent: just connect the signal to a method on `context`
        sender.destroyed.connect(context_handler)
        
        # When context is destroyed, the handler reference goes away if it's a method.
        # For a free function like `context_handler`, you’d disconnect manually if needed.

        # ------------------------------------------------
        print("\n7. static connect(sender, signal: str, receiver, member: str)")
        label = QLabel()
        scroll = QScrollBar()
        # Legacy
        QObject.connect(scroll, SIGNAL("valueChanged(int)"), label, SLOT("setNum(int)"))
        # Modern
        scroll.valueChanged.connect(label.setNum)

        # Trigger scroll bar to demonstrate
        scroll.setValue(42)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    sys.exit(app.exec())
