---
title: Qml Signal - PySide6 Slot Using QmlElement
layout: default
nav_order: 3
parent: 02 QtQuick Signals and Slots
---

## Qml Signal - PySide6 Slot Using QmlElement

In this example we have a Qml signal, a PySide6 slot and we connect them in our Qml code. To do that

```qml
{% include src/qtquickexamples/02_qt_qml/03_signals_and_slots/03_qmlelement.qml %}
```

```python
{% include src/qtquickexamples/02_qt_qml/03_signals_and_slots/03_qmlelement.py %}
```

1. Create a Python class with a slot method and register it with the Qml type sistem so it can be used from within Qml. The class needs to be derived from `QObject` and you need to decorate it with the `@QmlElement` decorator. Remember how using the `@Slot` decorator was recommended but not mandatory in Qt Widget applications? Here you **have to** decorate your slot method with `@Slot` or the Qml engine will say `TypeError: Property 'log' of object Logger(0x1884cdefae0) is not a function`. Lastly, you need to set two global variables: `QML_IMPORT_NAME` to hold the name by which your class will be referred in Qml, and `QML_IMPORT_MAJOR_VERSION` which is usually set to `1`. The [PySide6 documentation on the two](https://doc.qt.io/qtforpython-6/PySide6/QtQml/QmlElement.html) is a bit sparse but if you omit them PySide6 will say `TypeError: You need specify QML_IMPORT_NAME in order to use QmlElement.`. The two variables are also listed as [qmake variable names](https://doc.qt.io/qt-6/qmake-variable-reference.html) but also very briefly.

2. Import the `Logger` class using the name specified in QML_IMPORT_NAME (in the example `import examples.logger`),  add a `Logger` instance to the application assigning it an id, in this case `logger`.

3. Connect the Qml `Button.clicked` signal to the PySide6 slot. The `clicked` signal matching event handler is named `onClicked` and you just call the PySide6 slot from within it.