---
title: QRadioButton Example
layout: default
nav_order: 3
parent: 04 Buttons
---

## `QRadioButton`

![QRadioButton](/blog/images/qtwidgetsexamples/04_buttons/03_radio_button.png)

```python
{% include src/qtwidgetsexamples/04_buttons/03_radio_button.py %}
```

`QRadioButton` is a widget that presents the user with a set of mutually exclusive options. When you select (check) a radio button all the radio buttons that have the same parent widget are switched off. To use `QRadioButton`s in your application

1. Create the radio button objects and add them to the layout. `QLayout` and its child classes are not `QWidget`s so when you add a widget to a layout it is not the layout that becomes the widget's parent but the widget that the layout is assigned to. In this example all three radio buttons have the same parent widget - the `Window` object which is also the main application widget.

2. Create the slot to handle the radio buttons `toggled` signal. In this case the slot has an argument that `toggled` does not provide named `color`. `color` holds a string containing a color name and each radio button provides an appropriate color to the slot using a lambda. There is a Qt's version of CSS - cascading style sheets - named [QSS](https://doc.qt.io/qt-6/stylesheet-syntax.html) which you can apply to Qt widgets using `QWidget.setStyleSheet()` and this is how we change the `QLabel` background and foreground color on radio button `toggled`.

3. Connect the signals and the slot. In this case lambdas are needed to pass the extra argument to the slot.

`QRadioButton`s form a group of mutually exclusive states based on the common parent widget but this can be bypassed using [`QButtonGroup`](https://doc.qt.io/qt-6/qbuttongroup.html) a class that warrants its own example.