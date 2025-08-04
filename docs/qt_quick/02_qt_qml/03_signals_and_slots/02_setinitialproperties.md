---
title: PySide6 Signal - QtQuick Slot Using QQmlApplicationEngine.setInitialProperties()
layout: default
nav_order: 2
parent: 02 QtQuick Signals and Slots
---

## PySide6 Signal - QtQuick Slot Using QQmlApplicationEngine.setInitialProperties()

In the [previous example]({% link docs/qt_quick/02_qt_qml/02_signals_and_slots/01_rootobject_findchild.md %}) we've had a PySide6 signal, a Qml slot, and the connection is made in PySide6. In this one we still have a  PySide6 signal and a Qml slot but we connect them in the Qml file. To do this

```qml
{% include src/qtquickexamples/02_qt_qml/02_signals_and_slots/02_setinitialproperties.qml %}
```

```python
{% include src/qtquickexamples/02_qt_qml/02_signals_and_slots/02_setinitialproperties.py %}
```

1. Add a custom property to the Qml ApplicationWindow. Custom properties can be of any of the Qml value types like `bool`, `int` or `string` but as `QTimer` is an object we set the property type to `variant` (although `var` would also work).

2. In the PySide6 file, create a `QTimer` object named `timer` and use `QQmalApplicationEngine.setInitialProperties()` to assign `timer` to the `ApplicationWindow.timer` property we created in 1. `setInitialProperties()` accepts a Python dictionary and in this case it has only one element. You need to `setInitialProperties()` before you `load()` the Qml file or the Qml engine will complain: `Unable to assign [undefined] to QObject*`.

3. Back in Qml, use the `Connections` type to create the slot and connect the signal with it. `Connections.target` holds a reference to the object that emits the signal and the slot and the signal names need to match: the signal's name is `timeout` so the slot needs to be named `onTimeout`. The slot sets the label's text to the current time just as in the first example.