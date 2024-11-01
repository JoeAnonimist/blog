---
title: QCheckBox Example
layout: default
nav_order: 2
parent: 04 Buttons
---

## PySide6 QCheckBox Example

![QCheckBox](/blog/images/qtwidgetsexamples/04_buttons/02_check_box.png)

```python
{% include src/qtwidgetsexamples/04_buttons/02_check_box.py %}
```

`QCheckBox` is  a widget that has a graphical check box and a label. it can be checked, unchecked and, if you set its `tristate` property to `True`, partially checked. Checkboxes are commonly used to represent options that are __not__ mutually exclusive - more than one checkbox in a group can be checked at the same time. To use `QCheckBox` in your application

1. Create a `QCheckBox` object passing the text to be displayed to the constructor. In the example we create three checkboxes, one for each popular operating system and add each of them to the window's layout. We also set each checkbox `objectName` property. Setting `objectName` can be useful in debugging or when you need to find a widget using `QObject.findChild()` as `objectName` is initially empty.

2. Create the slot to process checkboxes' `checkStateChanged` signals. The documentation suggests that you mark it with the `Slot()` decorator but if you do you also need to import the `Qt` class from `PySide6.QtCore`. If you don't PySide6 will complain:

    > TypeError: Cannot call meta function "void on_state_changed(Qt::CheckState)" because parameter 0 of type "Qt::CheckState" cannot be converted.

    This is because `checkStateChanged` `state` argument is of type `Qt.CheckState` and `Qt.CheckState`, like many other Qt enums, resides in `PySide6.QtCore.Qt` so you'll often need to import it. So, in this case, either import `Qt` or omit the `Slot()` decorator.
    
3. Finally, connect each checkbox' `checkStateChanged` signal to the created slot.
