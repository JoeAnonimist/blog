---
title: QTreeView Example
layout: default
nav_order: 3
parent: 07 Item Views
---

## PySide6 QTreeView Example

![QTreeView](/blog/images/qtwidgetsexamples/07_item_views/03_tree_view.png)

```python
{% include src/qtwidgetsexamples/07_item_views/03_tree_view.py %}
```

Just as `QTableView` is `QTableWidget`'s parent, `QTreeView`1 is the parent class of `QTreeWidget` designed to display tree-like data structures. To use `QTreeView` in your application

1. Create a `QTreeView` instance.

2. Create a model object. In the example we use `QFileSystemModel` a ready-made subclass of `QAbstractItemModel` provided by Qt that models the file system hierarchy. If you need to display your own custom tree-like data structures you need to create a `QAbstractItemModel` subclass yourself, implementing the required methods. Also set the model's root path to the current user's home directory.

3. Set the treeview's model using `QTreeView.setModel()`.

4. Set the `QTreeView` root index to the index of the current user's home directory.

`QFileSystemModel` will pick up any changes to to file system tree and update the view automatically.