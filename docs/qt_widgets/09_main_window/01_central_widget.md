---
title: QMainWindow Central Widget Example
layout: default
nav_order: 1
parent: 09 Main Window
---

## PySide6 QMainWindow Central Widget Example

![QMainWindow central widget](/blog/images/qtwidgetsexamples/09_main_window/01_central_widget.png)

```python
{% include src/qtwidgetsexamples/09_main_window/01_central_widget.py %}
```

The `QMainWindow` class provides support for the following UI elements out of the box:
    - Toolbars
    - Dock widgets
    - Menu bars
    - A status bar
and is a good starting point for making complex user interfaces. To use it in your application

1. Create a class that inherits `QMainWindow`. In the example the child class name is `Editor` as the example will be used to make a rudimantary text editor.

2. In the `Editor` `__init__` method create to be used as its central widget, `QTextEdit` in the example.

3. Set the created `QTextEdit` object as the editor's central widget using `QMainWindow.setCentralWidget()`

Now, if you run the example you'll see a Qt window filled with the text widget.