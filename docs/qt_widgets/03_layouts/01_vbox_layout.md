---
title: QVBoxLayout Demo
layout: default
nav_order: 1
parent: 03 Layouts
---

## PySide6 QVBoxLayout Example

![QVBoxLayout](/blog/images/qtwidgetsexamples/03_layouts/01_vbox_layout.png)

```python
{% include src/qtwidgetsexamples/03_layouts/01_vbox_layout.py %}
```

[`QVBoxLayout`](https://doc.qt.io/qt-6/qvboxlayout.html) lines up widgets in a column. If you go to the previous link and follow the inheritance chain you'll notice that `QWidget` is **not** one of the `QVBoxLayout`'s parent classes - this means you can not `show()` it on the screen like `QWidget` child classes. To add a vertical layout to your `QWidget`

1. Create a new `QVBoxLayout` object and use the `QWidget.setLayout()` method to set it as your widget layout. This works for `QWidget` subclasses  as well as `QWidget`s that are not top level windows. You can also have layouts within another layout.

2. Create widgets you want to lay out. In this example I created three `QPushButton`s

3. Add your widgets to the layout using `QVBoxLayout.addWidget()`. If you want to have an inner layout use `QVBoxLayout.addLayout()` instead.

If you run the script and resize the window with your mouse you'll notice that the layout will resize with it but the buttons will only resize horizontally, keeping their height constant. There are two ways you can change this: If you add stretchable space after the widgets (using `layout.addStretch()`) it will stretch and keep the buttons neatly lined up. If you want a child widget to change its size with the layout set its size policy to `Expanding` (eg. `button_1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)`)

Another thing to note in the above script is that I connected all three `QPushButton`s' clicked signal to a single slot named `on_button_clicked`. If you do that you can tell which button was clicked using [`QObject.sender()`](https://doc.qt.io/qt-6/qobject.html#sender) but remember the following warning (copied from the documentation):

> Warning: This function violates the object-oriented principle of modularity. However, getting access to the sender might be useful when many signals are connected to a single slot.