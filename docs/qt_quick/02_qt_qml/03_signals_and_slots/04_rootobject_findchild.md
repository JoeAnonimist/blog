---
title: Qml Signal - PySide6 Slot Using QObject.findChild()
layout: default
nav_order: 4
parent: 02 QtQuick Signals and Slots
---

## Qml Signal - PySide6 Slot Using QObject.findChild()

Finally, we have a Qml signal, a PySide6 slow and the connection is established in PySide6 code. To do this

```qml
{% include src/qtquickexamples/02_qt_qml/02_signals_and_slots/04_rootobject_findchild.qml %}
```

```python
{% include src/qtquickexamples/02_qt_qml/02_signals_and_slots/04_rootobject_findchild.py %}
```

1. Add a Qml `Button` to the main window and set its `objectName` so you can find in in the PySide6 code.

2. Use `QQmlApplicationEngine.rootObjects()` to get the main window object reference in the PySide6 code and `QObject.findChild()` to get the reference to the `Button` object.

3. Create a `Logger` class instance and connect its `log()` method with the `Button`'s `clicked` signal. We don't need to use `Logger` in Qml so we don't decorate it with `QmlElement`.