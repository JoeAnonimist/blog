---
title: QListWidget Example
layout: default
nav_order: 1
parent: 06 Item Widgets
---

## PySide6 QListWidget Example

```python
{% include src/qtwidgetsexamples/06_item_widgets/01_list_widget.py %}
```

The `QListWidget` is a widget that displays a list of items. There are two main ways you can add items to a `QListWidget`: a) by creating a series of `QListWidgetItem` objects and adding them to your `QListWidget` using the `QListWidget.addItem()` method or b) by passing a list of strings to the `QListWidget` constructor, in which case `QListWidget` automatically creates a `QListWidgetItem` for each string in the list. To use `QListWidget` in your application

1. Create a `QListWidget` instance and add items to it. In the example we create three `QListWidgetItem`s and add the to the `QListWidget` but there are also two `addItems()` methods that allow you to add a list of `QListWidgetItem`s or strings. We also create a `QLabel` instance whose background color will change when `QListWidget` current item changes.

2. Create a slot to handle the `QListWidget.currentItemChanged` signals. `currentItemChanged` has two arguments, `current` and `previous` and we use `current` to get the currently selected item text and set the `QLabel`'s style sheet accordingly.

3. Connect the signal and the slot. In addition to the `currentItemChanged`, `QListWidget` provides several other signals related to its item manipulation.

This is a basic example of `QListWidget` usage. In addition to the above, you can add icons and checkboxes to items or make them editable. `QListWidget`'s parent class, `QListView` is part of the Qt model/view framework which makes it even more flexible.