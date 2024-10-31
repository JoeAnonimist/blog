---
title: QGroupBox Example
layout: default
nav_order: 1
parent: 08 Containers
---

## PySide6 QGroupBox Example

![QScrollArea](/blog/images/qtwidgetsexamples/08_containers/01_group_box.png)

```python
{% include src/qtwidgetsexamples/08_containers/01_group_box.py %}
```

`QGroupBox` is a widget that has a frame and a title on top and allows you to display various other widgets inside itself but is commonly used to group checkboxes or radiobuttons. `QGroupBox` does not lay out its child widgets automatically - you need to do it yourself using one of the Qt layout classes. You can set a `QGroupBox` to be `checkable` which lets the user enable or disable all its child widgets simultaneously. To use a group box in your application

1. Create a `QGroupBox` object and add a layout to it as you can't add widgets directly. In the example we use a `QVBoxLayout`.

2. Create widgets and add them to the layout. In the example we add three `QRadioButton`s. We also set one of the radio buttons to `checked`.

3. Create the slot method to handle `QRadioButton.toggled` signals. The slot sets a label's text to the text of the checked radiobutton and the last two radiobuttons also toggle the group box `togglable` property.

4. Connect `QRadioButton.toggled` signals with the slot.