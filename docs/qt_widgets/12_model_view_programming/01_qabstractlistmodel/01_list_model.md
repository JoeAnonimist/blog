---
title: A Read-Only Subclass of QAbstractListModel
layout: default
nav_order: 1
parent: 01 QAbstractListModel Examples
---

## A Read-Only Subclass of `QAbstractListModel`

```python
{% include src/qtwidgetsexamples/12_model_view_programming/01_qabstractlistmodel/01_list_model.py %}
```

The Qt model-view architecture is the Qt variation of the model-view-controller (MVC) design pattern where, per the documentation, the controller and the view are combined. The model and the view are decoupled which lets you use the same model with multiple views. Using the model and view Qt classes does not automatically mean that the overall design of your application follows the MVC design pattern.

Qt provides several abstract classes that you can subclass to make your own custom models:

- `QAbstractItemModel`
- `QAbstractTableModel`
- `QAbstractListModel`

Of these three classes, `QAbstractListModel` is the easiest one to subclass. Qt also provides several concrete model classes like

- `QStandardItemModel`
- `QFileSystemModel`
- `QSqlQueryModel`

that you can readily use with the Qt view classes. We've  already seen how to use [some of these classes]({% link docs/qt_widgets/07_item_views.md %}) with the Qt view classes and now we'll focus on writing your own custom model classes. To create a read-only list model

1. Create a subclass of `QAbstractListModel` and make the data source available to it. In the example the data source is a coma-separated values (CSV) file - we read the whole file contents in the `__init__()` method and store it in a Python list named `CsvModel.csv_data`, each list element containing all the CSV columns for a given row joined together in a single string value. This does not have to be the case as you can also retrieve your data dynamically.

2. Implement the `rowCount()` method. The view classes use this method to get the information about the model list length. In the example we simply return the the `csv_data` list length using the `len` Python function. By default, Qt list models only have one column.

3. Implement the `data()` method. The `data()` method returns the model data for a given index and role. The index is a `QModelIndex` instance and we get the model data from the `csv_data` list using `QModelIndex.row()`. The role is a member of the `Qt.ItemDataRole` enumeration and in the example we return the data only for the `ItemDataRole.DisplayRole`, ie. the text to be displayed by the view.

4. Optionally, implement the `headerData()` method for the given section (row or column). In the example the only column header is a string that contains all the CSV file column names joined in a single string. `QListView`, the view class that we use in this example does not display model headers but if we were to use a `QTableView` it would have been shown.

A note about the `QModelIndex` class: It is used by the views to locate an item in the model. Qt models are table based - you can view the model in this example as a table having one column and `n` rows - and you can use `QModelIndex.row()` and `QModelIndex.column()` to refer to a single table cell. When creating your own model classes you may need to create new `QModelIndex` objects using `QModelIndexcreateIndex()` method. You may also need to create invalid `QModelIndex` objects which can be done using the `QModelIndex` constructor, ie. using `QModelIndex()`. You can access the actual model data referred to by an index using the `QModelIndex.internalPointer()` method.

Another note about `QAbstractItemModelTester` a class that comes in handy when implementing your own model classes - pass your model instance to its constructor and it report many possible implementation errors, printed out in the terminal.