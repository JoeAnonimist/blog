---
title: QSpinBox and QDial Example
layout: default
nav_order: 3
parent: 05 Input Widgets
---

## PySide6 QSpinBox and QDial Example

```python
{% include src/qtwidgetsexamples/05_input_widgets/03_spin_box.py %}
```

`QSpinBox` provides a spin box widget and `QDial` is a rounded range widget visually similar to a potentiometer. While both widgets provide similar functionality, ie. let the user select an integer from a range of values they do not inherit each other. Here is what their inheritance tree looks like:

```
QWidget
    ...
    QAbstractSlider
        <Strong>QDial</Strong>
        QScrollBar
        QSlider
    ...
    QAbstractSpinBox
        QDateTimeEdit
            QDateEdit
            QTimeEdit
        QDoubleSpinBox
        <Strong>QSpinBox</Strong>
    ...
```