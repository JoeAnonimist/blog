---
title: PySide6 template script - QLabel
layout: default
parent: 01 Template Scripts
tags: templates
nav_order: 3
---

## PySide6 starter script that shows a QLabel

![Template 1](/blog/images/qtwidgetsexamples/01_template_scripts/02_helloworld1.png)

```python
{% include src/qtwidgetsexamples/01_script_template/helloworld1.py %}
```

In [the previous post]({% link docs/qt_widgets/01_template_scripts/template1.md %}) I described a simple PySide6 scripts that shows an empty  window on the screen. Now let's start adding widgets to that window.

1. Create a class inherited from `QWidget`. This class is used as the application main window. In the class' `__init__()` method

2. Create a `QVBoxLayout` instance and set it as the window layout. `QVBoxLayout` lays out its child widgets vertically. There's also `QHBoxLayout`, `QFormLayout`, `QGridLayout` and `QStackedLayout` to choose from. You don't actually have to use layouts - you can position widgets manually, but layouts are more flexible and, as far as I can tell, are commonly used in Qt/PySide6 applications.

3. Create an instance (object) of the QLabel class and add it to the layout. QLabel is a widget that is used to display multi-line text that you can format but can not edit.

The rest of the code is the same as in the script that shows an empty window.