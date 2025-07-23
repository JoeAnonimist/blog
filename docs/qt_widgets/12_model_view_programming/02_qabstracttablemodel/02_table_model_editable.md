---
title: Editable QAbstractTableModel Subclass
layout: default
nav_order: 2
parent: 02 QAbstractTableModel Examples
---

## Editable `QAbstractTableModel` Subclass

```python
{% include src/qtwidgetsexamples/12_model_view_programming/02_qabstracttablemodel/02_table_model_editable.py %}
```

In the previous example we created a read-only `QAbstractTableModel` subclass by implementing three methods: `rowCount()`, `columnCount()` and `data()`. To make a model editable you need to implement two more: `setData()` and `flags()`. To use an editable table model

1. Create a subclass of `QAbstractTableModel`

2. Implement its `rowCount()`, `columnCount()` and `data()` methods. The implementation is the same as in the read-only model example.

3. Implement the `setData()` method. `setData()` accepts three arguments: `index`, a `QModelIndex` object that you will use to get the coordinates of the data point to be changed, `value` which is the new data value and `role`, one of the `Qt.ItemDataRole` enumeration members, in most cases `EditRole`. In the method body check if `role` is equal to `EditRole`, check if the new data is actually different from the current data, change the data and emit the `dataChanged()` signal.

4. Implement the `flags()` method. In this method you return the item flags given its index. In the example all items (ie. fields) are flagged as selectable, enabled and editable. This does not have to be the case. For instance, if you had a model based on a SQL table you would flag the primary key fields as selectable only, making only the primary keys read-only.

5. Then, in the main class, create a model instance, create a `QTableView` instance and use `QTableView.setModel()` to connect the two.