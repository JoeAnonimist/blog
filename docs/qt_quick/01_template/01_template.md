---
title: PySide6 QtQuick Hello World
layout: default
nav_order: 1
parent: 01 QtQuick Template Scripts
---

## PySide6 QtQuick script that shows a label

Unlike the [Qt Widgets Hello, World! script]({% link docs/qt_widgets/01_template_scripts/template1.md %}) this one consists of two files: one written in Qml, a Qt declarative language used to design a QtQuick user interface and the other written in Python, used to actually show the Qui and start the QtQuick application.

```qml
{% include src/qtquickexamples/01_template/01_hello_world.qml %}
```

On the Qml side of things, after the necessary imports

1. Create an instance of the `ApplicationWindow` Qml type. Similarly to `QMainWindow`, `ApplicationWindow` is a top-level window with support for menus, a header and a footer. Qml components form a hierarchy so all `ApplicationWindow` child components are declared within its curly braces, along with its properties. In the example we set the window size and title. Don't forget to set `ApplicationWindow.visible` to `true`.

2. Add a layout to `ApplicationWindow`. In the example, `ApplicationWindow`'s only child is a `RowLayout` whose only child component, in turn, is a `Label` which displays a message that says 'Hello Qml!'

```python
{% include src/qtquickexamples/01_template/01_hello_world.py %}
```


Back in Python/Pyside6 we

3. Create an instance of the `QGuiApplication` class. `QGuiApplication` is suitable for QtQuick applications just as `QApplication` is suitable for Qt Widget applications while you would use `QCoreApplication` for non-Gui Qt applications. Since `QGuiApplication` handles your application initialization you must create it before any other objects related to the user interface.

4. Create an instance of the `QQmlApplicationEngine` class and connect its `quit` signal to the `QGuiApplication.quit()` slot to make sure both the application and the engine exit at the same time.

5. Use `QQmlApplicationEngine.load()` to load the Qml file. `QQmlApplicationEngine` is a convenience class that lets you load a single Qml file into your application.

6. Finally use `QGuiApplication.exec()` to start the main event loop.