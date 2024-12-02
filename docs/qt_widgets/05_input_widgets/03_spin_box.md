---
title: QSpinBox and QDial Example
layout: default
nav_order: 3
parent: 05 Input Widgets
---

## `QSpinBox` and `QDial`

![QSpinBox](/blog/images/qtwidgetsexamples/05_input_widgets/03_spin_box.png)

```python
{% include src/qtwidgetsexamples/05_input_widgets/03_spin_box.py %}
```

`QSpinBox` provides a spin box widget with up and down arrows and `QDial` is a rounded range widget visually similar to a potentiometer. While both widgets provide similar functionality, ie. let the user select an integer from a range of values they do not inherit each other. Here is what their inheritance tree looks like:

```
QWidget
    ...
    QAbstractSlider
        QDial
        QScrollBar
        QSlider
    ...
    QAbstractSpinBox
        QDateTimeEdit
            QDateEdit
            QTimeEdit
        QDoubleSpinBox
        QSpinBox
    ...
```

`QSpinBox` parent class is `QAbstractSpinBox` while `QDial` parent is `QAbstractSlider` and their common ancestor is `QWidget`, shared with all the Qt widget classes. To use `QSpinBox` and `QDial` in your application

1. Create the widgets and set their value range. In the example the range is between 0 and 100 for both widget objects. The example also has a `QLabel` that echoes the current value.

2. Write the slot methods. Both widgets' `valueChanged()` signals passes an integer value to slots so if you want to use it to set a label's text you first need to convert it to a string.

3. Connect the widgets' `valueChanged()` signals to the slots.