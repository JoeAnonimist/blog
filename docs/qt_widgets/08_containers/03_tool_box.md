---
title: QToolBox Example
layout: default
nav_order: 3
parent: 08 Containers
---

## PySide6 QToolBox Example

![QToolBox](/blog/images/qtwidgetsexamples/08_containers/03_tool_box.png)

```python
{% include src/qtwidgetsexamples/08_containers/03_tool_box.py %}
```

`QToolBox` provides a column of tabbed widget items. This doesn't really tell you much - it is a Qt container widget pretty similar to the ubiquitous accordion widget that lets you pack multiple widgets within a relatively small space and expand or collapse them as needed. `QToolBox` pages are called items in the documentation. To use `QToolBox` in your application

1. Create a `QToolBox` object

2. Create the child widgets. In the example we simply create three push buttons each representing a popular operating system. You can also add multiple child widgets to a page by adding them to a layout as demonstrated on the `Linux' page.

3. Add the widgets to the toolbox using `QToolBox.addItem()`

In the example we also handle the child push buttons `clicked` signals for demonstration purposes, setting a label's text to the text of the clicked button.