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

Of these three classes, `QAbstractListModel` is the easiest one to subclass. Qt also provides concrete several concrete model classes like

- `QStandardItemModel`
- `QFileSystemModel`
- `QSqlQueryModel`

that you can readily use with the Qt view classes. We've  already seen how to use [some of these classes]({% link docs/qt_widgets/07_item_views.md %}) with the Qt view classes but now we'll focus on writing your own custom model classes.