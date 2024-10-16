---
title: PySide6 Signal - QtQuick Slot Using QObject.findChild()
layout: default
nav_order: 1
parent: 02 QtQuick Signals and Slots
---

## PySide6 Signal - QtQuick Slot Using QObject.findChild()

In the [Qt Widgets examples]({% link docs/qt_widgets/02_signals_and_slots.md %}) we've seen that a signal is emitted when an event occurs, a slot is typically a Python method, and that you need to connect them for the mechanism to work. In a hybrid Pyside6/QtQuick application both PySide6 and Qml objects can emit signals, slots can be defined in both Python and Qml files and connections between them can be established either in Python or in Qml. This complicates things a bit but let's start with a simple example. To use the signals and slots mechanism in a QtQuick application

```qml
{% include src/qtquickexamples/02_signals_and_slots/01_rootobject_findchild.qml %}
```

1. Add a function to a Qml object. In the example we start with the [template Qml file]({% link docs/qt_quick/01_template/01_template.md %}) and add a JavaScript function to the label. Qml comes with a JavaScript engine that lets you manipulate Qml objects and our function will simply set the label's text to the current time when executed. NOte that we also set two label's properties: `id` and `objectName`. The `id` property is used to refer to an object from JavaScript code as in `label.text = ...`. The `objectName` property sets `QObject.objectName` to the given string which is useful when you need to find the object using `QObject`'s `findChild()` or `findChildren()` methods. Note also that `id` is not a string.

In the Python file

```python
{% include src/qtquickexamples/02_signals_and_slots/01_rootobject_findchild.py %}
```

1. Get a reference to the Qml Label. Get the root objects using `QQmlApplicationEngine.rootObjects()` - `rootObjects()` returns a list and `ApplicationWindow` is the first (and the only) element in it. As `ApplicationWindow` is ultimately a `QObject` we use `QObject.findChild()` to find the label.

2. Create a `QTimer` instance and connect the timer's `timeout` signal to the label's `updateText` slot just as you would in a Qt Widgets application. Finally start the timer and the application itself.

That's it - every time the timer ticks `updateText` is executed and the label's text is updated. To recap, we have

- a JavaScript function
- a PySide6 signal
- the connection is created in PySide6 code