---
title: 12 Model-View Programming
layout: default
parent: Qt Widgets
nav_order: 12
---

## Model-View Programming

```mermaid

classDiagram
    QAbstractItemModel <|-- QAbstractListModel
    QAbstractItemModel <|-- QAbstractTableModel
    class QAbstractItemModel{
    }
    class QAbstractListModel{
    }
    class QAbstractTableModel{
    }

```