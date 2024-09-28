---
title: QCheckBox Example
layout: default
nav_order: 2
parent: 04 Buttons
---

## PySide6 QCheckBox Example

```python
{% include src/qtwidgetsexamples/04_buttons/02_check_box.py %}
```

`QCheckBox` is  a widget that has a graphical check box and a label. it can be checked, unchecked and, if you set its `tristate` property to `True`, partially checked. Checkboxes are commonly used to represent options that are __not__ mutually exclusive - more than one checkbox in a group can be checked at the same time. To use `QCheckBox` in your application

1. Create a `QCheckBox` object passing the text to be displayed to the constructor. In the example we create three checkboxes, one for each popular operating system and add each of them to the window's layout

2. Create the slot to process checkboxes' `stateChanged