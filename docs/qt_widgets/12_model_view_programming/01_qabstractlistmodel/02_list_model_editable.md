---
title: An Editable QAbstractListModel Subclass
layout: default
nav_order: 2
parent: 01 QAbstractListModel Examples
---

## An Editable QAbstractListModel Subclass

```python
{% include src/qtwidgetsexamples/12_model_view_programming/01_qabstractlistmodel/02_list_model_editable.py %}
```

In [the read-only list model example]({% link docs/qt_widgets/12_model_view_programming/01_qabstractlistmodel/01_list_model.md %}) we saw that, at minimum, we needed to implement two methods to create a working list model: `rowCount()` and `data()`. Now let's see how to make that model editable:

1. Create a `QAbstractListModel` subclass and make the data available to it in some way.

2. Create the `rowCount()` and `data()` methods just as you did for the read-only model.

3. Implement the `setData()` method. `setData()` accepts three arguments: `index`, `value` and `role`. In the method we check if the role is equal to `Qt.ItemDataRole.EditRole` and, if it is, we set the model data for the `index.row()` to `value`. If the data is set successfully `setData()` returns `True` and `False` otherwise.

4. Implement the `flags()` method. In this method we signal to views that the model data is editable by adding `Qt.ItemFlags.ItemIsEditable` to the flags. Note that we can make list model items editable selectively by checking the `flags()`  `index` parameter. In the example we ignore `index` which means that all the model items are editable.

Now if you double-click any of the list view lines you are able to edit it and the changes are saved in the model (ie. to the `CsvModel.csv_data` list and signaled by the `dataChanged` signal. You can also implement the logic to update the CSV file from the `csv_data` values but we omit that in this example.