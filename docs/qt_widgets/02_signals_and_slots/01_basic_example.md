---
title: A Basic Signal and Slot Example
layout: default
nav_order: 1
parent: 02 Signals and Slots
---

## PySide6 Basic Signal and Slot Example

```python
{% include src/qtwidgetsexamples/02_signals_and_slots/01_basic_example.py %}
```

The signals and slots mechanism is a fundamental concept in Qt. A signal is emitted when an event (eg. mouse click) occurs and a slot is a Python method or function that is executed when a signal is emitted. In order for a slot to actually be called you need to **connect** the two. So, starting with [the template PySide6 script]({% link docs/qt_widgets/01_template_scripts/template1.md %})

1. Create a `QPushButton` instance and add it to the layout. `QPushButton` is a common widget that sends a signal when you click on it. Aside from `clicked`, `QPushButton` sends `pressed`, `released` and `toggled`   signals. `clicked` combines `pressed` and `released`.

2. Add a method  to `Window` that will be called when the button is clicked. This is the slot and it is marked by the `Slot()` decorator. You don't have to use the decorator but [the documentation](https://doc.qt.io/qtforpython-6/tutorials/basictutorial/signals_and_slots.html) that you do as not doing so causes run-time overhead.   
If you look at the `on_button_clicked` signature you'll see that it accepts a parameter named `checked`. The signature of `on_button_clicked` matches the [signature of `QPushButton.clicked`](https://doc.qt.io/qt-6/qabstractbutton.html#clicked). In this example `checked` is always `False` because its `checkable` property is set to `False` by default and we didn't change it. The signature could have been `on_button_clicked(self)` as well in which case `checked` would have been ignored.

3. Connect the signal and the slot. The Python syntax to make the connection is `object.signal_name.connect(slot_name)`. Note there are no parentheses after `self.on_button_clicked` because `button.clicked.connect()` accepts a function object.