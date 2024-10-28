---
title: QListView Example
layout: default
nav_order: 1
parent: 07 Item Views
---

## PySide6 QListView Example

```python
{% include src/qtwidgetsexamples/07_item_views/01_list_view.py %}
```

`QListView` is one of the Qt view classes. Visually, it looks exactly the same as `QListWidget`, its child class, but lacks methods for item manipulation like `addItem()` and similar. Instead, it makes you create a model to provide the data, which may be more work but is more flexible. For instance, one model can be associated with multiple views. To use `QListView` in your application

1. Create a `QListView` instance.

2. Create a model to support it. In this example we use `QStandardItemModel`, a class provided by the Qt framework, but it is quite possible (and fairly common) to make your own custom model by subclassing `QAbstractItemModel` or `QAbstractListModel`. In the example we populate the model by adding all entries from the user's home directory to it.

3. Set the view's model using `QListView.setModel()`