---
title: QComboBox Example
layout: default
nav_order: 2
parent: 05 Input Widgets
---

## PySide6 QComboBox Example

![QComboBox](/blog/images/qtwidgetsexamples/05_input_widgets/02_combo_box.png)

```python
{% include src/qtwidgetsexamples/05_input_widgets/02_combo_box.py %}
```

`QComboBox` combines a button and a pop-up list. When the button is clicked the list pops up and lets you select one of the items which saves precious UI space. To use `QComboBox` in your application

1. Create the `QComboBox` object. There isn't a constructor that accepts a list of combobox items.

2. Add items to the combobox. You can manipulate individual `QComboBox` items using `addItem()`, `insertItem()` and `removeItem()`. You can manipulate items en gros using `addItems()`, `insertItems()` and `clear()`. Lastly, as `QComboBox` is part of the Qt model-view framework, you can set its items using its `model()` property.

3. Write the methods to handle `QComboBox` signals. `QComboBox` emits several types of signals and the ones of interest are `currentIndexChanged`, `currentTextChanged` and `textActivated`. In your slots, you can use `currentData()`, `currentText()` and `currentIndex()` to get information about the selected item which we demonstrate in the example.