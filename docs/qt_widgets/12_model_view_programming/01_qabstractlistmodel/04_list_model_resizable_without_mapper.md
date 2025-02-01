---
title: Resizable QAbstractListModel Subclass
layout: default
nav_order: 4
parent: 01 QAbstractListModel Examples
---

## Resizable `QAbstractListModel` Subclass

```python
{% include src/qtwidgetsexamples/12_model_view_programming/01_qabstractlistmodel/04_list_model_resizable_without_mapper.py %}
```

For a basic `QAbstractListModel` subclass you need to implement at least two methods: `rowCount()` and `data()`. If you want to make the model editable you  need to implement two more: `setData()` and `flags()`. If you also want to be able to add or remove rows to the models you need to implement `insertRows()` and `removeRows()`. To make a resizable `QAbstractListModel` subclass

1. Create a subclass of the `QAbstractListModel` class. Just as in the previous examples we read the actual data from a CSV file and store it in a Python list named `self.csv_data`.

2. Implement the `QAbstractListModel.insertRows()` method. In the example we make it easy on ourselves and only allow inserting one row at a time filled with a template text that says "\<insert row data\>". Note that we guard the actual data insertion with the `QAbstractListModel.beginInsertRows()` and `QAbstractListModel.endInsertRows()`. `beginInsertRows()` takes three arguments: `parent` which in our example is an invalid `QModelIndex()`, `first` and `last` are the row numbers that the inserted  will have after they have been inserted and have the same value in the example.