---
title: QTreeWidget Example
layout: default
nav_order: 3
parent: 06 Item Widgets
---

## PySide6 QTreeWidget Example

```python
{% include src/qtwidgetsexamples/06_item_widgets/03_tree_widget.py %}
```

The `QTreeWidget` provides a standard tree widget. It uses a predefined item model - each tree node is represented with a `QTreeWidgetItem` instance. To use `QTreeWidget in your application

1. Create a `QTreeWidget` object

```mermaid
graph TD;
A-->B;
A-->C;
B-->D;
C-->D;
```