---
title: 12 Model-View Programming
layout: default
parent: Qt Widgets
nav_order: 12
---

## Model-View Programming


| **Base Class**     | **Type** | **Must Implement** |
|---------------------|-----------|-----------------|
| `QAbstractListModel`  | **Read-Only** | `rowCount()`<br/>`data()` |
|                     | **Editable**  | `rowCount()`<br/>`data()`<br/>`setData()`<br/>`flags()` |
|                     | **Resizable** | `rowCount()`<br/>`data()`<br/>`setData()`<br/>`flags()`<br/>`insertRows()`<br/>`removeRows()` |
| `QAbstractTableModel` | **Read-Only** | `rowCount()`<br/>`columnCount()`<br/>`data()`<br/> |
|                     | **Editable**  | `rowCount()`<br/>`columnCount()`<br/>`data()`<br/>`setData()`<br/>`flags()` |
|                     | **Resizable** | `rowCount()`<br/>`columnCount()`<br/>`data()`<br/>`setData()`<br/>`flags()`<br/>`insertRows()`<br/>`insertColumns()`<br/>`removeRows()`<br/>`removeColumns()` |
| `QAbstractItemModel`  | **Read-Only** | `index()`<br/>`parent()`<br/>`rowCount()`<br/>`columnCount()`<br/>`data()` |
|                     | **Editable**  | `index()`<br/>`parent()`<br/>`rowCount()`<br/>`columnCount()`<br/>`data()`<br/>`setData()`<br/>`flags()` |
|                     | **Resizable** | `index()`<br/>`parent()`<br/>`rowCount()`<br/>`columnCount()`<br/>`data()`<br/>`setData()`<br/>`flags()`<br/>`insertRows()`<br/>`insertColumns()`<br/>`removeRows()`<br/>`removeColumns()` |

