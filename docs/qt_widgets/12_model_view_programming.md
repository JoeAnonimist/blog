---
title: 12 Model-View Programming
layout: default
parent: Qt Widgets
nav_order: 12
---

## Model-View Programming


| **Base Class**     | **Type** | **Must Implement** |
|---------------------|-----------|-----------------|
| `QAbstractListModel`  | **Read-Only** | `rowCount()`      |
|                     |           | `data()`          |
|                     | **Editable**  | `rowCount()`      |
|                     |           | `data()`          |
|                     |           | `setData()`       |
|                     |           | `flags()`         |
|                     | **Resizable** | `rowCount()`      |
|                     |           | `data()`          |
|                     |           | `setData()`       |
|                     |           | `flags()`         |
|                     |           | `insertRows()`    |
|                     |           | `removeRows()`    |
| `QAbstractTableModel` | **Read-Only** | `rowCount()`      |
|                     |           | `columnCount()`   |
|                     |           | `data()`          |
|                     | **Editable**  | `rowCount()`      |
|                     |           | `columnCount()`   |
|                     |           | `data()`          |
|                     |           | `setData()`       |
|                     |           | `flags()`         |
|                     | **Resizable** | `rowCount()`      |
|                     |           | `columnCount()`   |
|                     |           | `data()`          |
|                     |           | `setData()`       |
|                     |           | `flags()`         |
|                     |           | `insertRows()`    |
|                     |           | `insertColumns()` |
|                     |           | `removeRows()`    |
|                     |           | `removeColumns()` |
| `QAbstractItemModel`  | **Read-Only** | `index()`         |
|                     |           | `parent()`        |
|                     |           | `rowCount()`      |
|                     |           | `columnCount()`   |
|                     |           | `data()`          |
|                     | **Editable**  | `index()`         |
|                     |           | `parent()`        |
|                     |           | `rowCount()`      |
|                     |           | `columnCount()`   |
|                     |           | `data()`          |
|                     |           | `setData()`       |
|                     |           | `flags()`         |
|                     | **Resizable** | `index()`         |
|                     |           | `parent()`        |
|                     |           | `rowCount()`      |
|                     |           | `columnCount()`   |
|                     |           | `data()`          |
|                     |           | `setData()`       |
|                     |           | `flags()`         |
|                     |           | `insertRows()`    |
|                     |           | `insertColumns()` |
|                     |           | `removeRows()`    |
|                     |           | `removeColumns()` |

