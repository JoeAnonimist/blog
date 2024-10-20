---
title: QTableWidget Example
layout: default
nav_order: 2
parent: 06 Item Widgets
---

## PySide6 QTableWidget Example

```python
{% include src/qtwidgetsexamples/06_item_widgets/02_table_widget.py %}
```

The `QTableWidget` class provides an item-based table view with a default model. Simply put, it's a table. To use it in your application

1. Create a `QTableWidget` instance and set the table dimensions. The table in the example has three rows and four columns. We also add a `QLabel` to the window.

2. Fill the table cells with data. Each table cell is represented with a `QTableWidgetItem` instance so we use a nested loop to create `3 * 4 = 12` `QTableWidgetItem` instances. We set each item's data to a random integer using `QTableWidgetItem.setData()`. `data()` is a `QVariant` so you can set it to other common data types as well. After that each `QTableWidgetItem` is assigned to a table cell using `QTableWidget.setItem(row, column, item)`

3. Create two slot methods to create two `QTableWidget` signals: `currentItemChanged` and `itemChanged`. The first signal is emitted when the current item changes and the slot sets the label's text to the current item's text. The second signal is emitted when an item's value changed. Our `QTableWidget` is editable and if you double-click on a cell, change its value and press Enter, the label's text is updated accordingly. Note that when you double-click on a cell to enter its edit mode Qt recognizes the value as an integer and adds a spin box to the cell.