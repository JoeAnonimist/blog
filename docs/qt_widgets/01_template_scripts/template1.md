---
title: PySide6 template script - empty
layout: default
nav_order: 2
parent: 01 Template Scripts
---

## PySide6 script that shows an empty window

```python
{% include src/qtwidgetsexamples/01_script_template/helloworld.py %}
```

This is a simple template script I use so I don't have to remember the boilerplate code each time I want to use PySide6. The only thing it does is display an empty Qt window but it has all the elements of a Qt/PySide application nonetheless, So here's the breakdown: 

After the necessary imports

1. Create a Python  class that is a `QWidget` subclass. `QWidget` is the base class of all Qt widget classes so you could use `QPushButton` or `QDialog` here instead. For more involved application that have toolbars, menubars etc you would use `QMainWindow` that provides them out of the box. In your class' `__init__()` you have to `__init__()` the superclass (ie. `QWidget`) or you get a runtime error.

In the main script code

2. Create a `QApplication` instance. This should be the first thing you do in your application/script. For non Qt Widget GUI application there is `QGuiApplication` and for terminal/console applications there is `QCoreApplication`. `QApplication` is singleton so if you try to create it twice you get `RuntimeError: Please destroy the QApplication singleton before creating a new QApplication instance.`

3. Create an object of your class (in the script `Window`) and `.show()` it. (`QWidget.show()`, well, shows it on the screen.)

4. Use `QApplication.exec()` to start the application event loop. With this your application's main windows is displayed on your screen and is able to process events. When you exit the application, for instance by pressing the window's close button `app.exec()` returns and your application exits. That's about it.