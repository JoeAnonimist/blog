---
title: QGridLayout Demo
layout: default
nav_order: 3
parent: 03 Layouts
---

## `QGridLayout`

![QGridLayout](/blog/images/qtwidgetsexamples/03_layouts/03_grid_layout.png)

```python
{% include src/qtwidgetsexamples/03_layouts/03_grid_layout.py %}
```

QGridLayout lays out widgets, well, in a grid. Unlike with `QVBoxLayout` and `QHBoxLayout`  you need to specify the `QWidget`'s position (ie. row and column) when adding it to the grid. To use `QGridLayout` in your application:

1. Create a `QGridLayout` instance and set it as your `QWidget` layout

2. Create the widgets and add them to the layout using `QGridLayout.addWidget()`. When adding them you need to specify the widget's position (ie.its row and column) which means you can leave some grid cells empty.In addition, you can specify how many rows and columns the widget will span eg. if you use `layout.addWidget(self.label, 4, 0, 1, 4)` and `self.label` will span one row and four columns.

In this script we fill the grid layout with sixteen `QPushButton`s, in four rows and four columns, and use a single `Slot` to handle all buttons' signals.  The buttons are added dynamically, using two for loops, and we never keep a reference to any of them. It is still possible to get a reference to the button that was clicked using `QObject.sender()` and getting the sender's position is possible if a bit involved.