---
title: QTreeWidget Example
layout: default
nav_order: 3
parent: 06 Item Widgets
---

## PySide6 QTreeWidget Example

![QTreeWidget](/blog/images/qtwidgetsexamples/06_item_widgets/03_tree_widget.png)

```python
{% include src/qtwidgetsexamples/06_item_widgets/03_tree_widget.py %}
```

The `QTreeWidget` provides a standard tree widget. It uses a predefined item model - each tree node is represented with a `QTreeWidgetItem` instance. To use `QTreeWidget in your application

1. Create a `QTreeWidget` object. It has only one constructor that optionally accepts the tree widget's parent widget but we don't set it here because adding a widget to a layout automatically sets the widget's parent.

2. Create `QTreeWidgetItem` objects and add them to the tree widget. Each tree node is represented by a `QTreeWidgetItem` object. If you set the `QTreeWidget` as its parent, like we do with the `apes` `QTreeWidgetItem` it becomes a root/top level item. If you set another `QTreeWidgetItem` as the parent that item becomes the parent and you use this parent-child relationship to form a tree structure that is displayed it the tree widget. We also use string lists like `['Gibbons']` to set the text to be displayed for each `QTreeWidgetItem`. `QTreeWidget` has one column by default but you can add more if you need.

3. Add necessary slots, connect them with the appropriate `QTreeWidget` signals and add the tree widget to the window layout. In the example we set a label's text to the current item text each time the tree widget current item changes.