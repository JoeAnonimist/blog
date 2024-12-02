---
title: QTableView
layout: default
nav_order: 2
parent: 07 Item Views
---

## `QTableView`

![QTableView](/blog/images/qtwidgetsexamples/07_item_views/02_table_view.png)

```python
{% include src/qtwidgetsexamples/07_item_views/02_table_view.py %}
```

`QTableView` is another one of the Qt view classes and, just as `QListWidget` is a subclass of `QListView`, `QTableWidget` is a subclass of `QTableView`. To use it in your application

1. Create a `QTableView` instance

2. Create a model instance. In the example we use   `QSqlQueryModel`, a model provided by Qt that is suitable for use with `QTableView` but we could have used `QSqlTableModel` or `QSqlRelationalTableModel` as well. For the purpose of the example we set up an in-memory SQLite database with one table which we populate with sample data.

3. Set the view's model using `QTableView.setModel()`

In this example we use the `QSqlDatabase`, `QSqlQuery` and `QSqlQueryModel` classes which are part of the QtSQL module. You might have noticed that `QSqlQery` and `QSqlQueryModel` both use SQL queries against our in-memory database but we don't specify the database connection explicitly - they both use `database` implicitly as it is set as the default connection (but more on that later). 

Also note that we didn't make `database` a Window member (ie. we didn't use `self.database`).