---
title: QMainWindow Dock Widget Example
layout: default
nav_order: 5
parent: 09 Main Window
---

## PySide6 QMainWindow Dock Widget Example

![QMainWindow dock widget](/blog/images/qtwidgetsexamples/09_main_window/05_dock_widget.png)

```python
{% include src/qtwidgetsexamples/09_main_window/05_dock_widget.py %}
```

The `QDockWidget` class represent a dockable widget. To use it in your application

1. Create a `QDockWidget` object and set its properties.

2. Create its child widgets and add them to it. In the example we create two push buttons to toggle the `QTextEdit` bold and italic properties and a spinbox to control the text size.

3. Handle the relevant child widgets' signals.

We end up with a rudimentary text editor in about 160 lines of PySide6 code.