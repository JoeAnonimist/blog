---
title: Read-Only QAbstractTableModel Subclass
layout: default
nav_order: 1
parent: 02 QAbstractTableModel Examples
---

## Read-Only `QAbstractTableModel` Subclass

```python
{% include src/qtwidgetsexamples/12_model_view_programming/02_qabstracttablemodel/01_table_model.py %}
```

`QAbstractTableModel` lets you make your two-dimensional data available to Qt views. Just as with `QAbstractListModel` it can be read-only, editable and resizable, depending on the base class methods you choose to implement. To use a read-only `QAbstractTableMOdel` object in your program

1. Create a subclass of `QAbstractTableModel` named `CsvModel` and make external data available to it. We read the data from the same csv file as in the `QAbstractListModel` example, `data.csv` using Python's csv reader and store it in a member variable named `self.csv_data`. `csv_data` is a list and csv reader's rows are also lists which effectively makes `csv_data` a two-dimensional list suitable for use with `QAbstractTableModel` subclasses

2. Implement the `rowCount()` and the `columnCount()` methods. `rowCount()` is the length of the `self.csv_data` list and never changes since the model is read-only. `columnCount()` is hard-coded to return 4, the number of columns in the csv file.

3. Implement the `data()` method. `data()` expects two arguments: `index`, a `QModelIndex` instance and `role`, a member of the `DisplayRole` enumeration. In the `data()` body we check if `role` is equal to `DisplayRole` and if it is we return the data that the index points to. Note  that we need to use both `index.row()` and `index.column()` as the data has two dimensions. With this you have a functional `QAbstracttableModel` subclass. 

4. In your main class (`Window`), create a `CsvModel` object, create a `QTableView` object and set its model using `QTableView()setModel()`

`QAbstractTableModel` subclasses are commonly used with `QTableView` but not necessarily so. `QTableView` is able to display table headers using the header data you provide to it in the model `headerData()` method but implementing `headerData()` is still not mandatory.