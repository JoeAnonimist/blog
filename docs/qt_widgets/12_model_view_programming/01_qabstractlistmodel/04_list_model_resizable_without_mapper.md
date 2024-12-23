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

1. 