---
title: QTabWidget
layout: default
nav_order: 4
parent: 08 Containers
---

## `QTabWidget`

![QTabWidget](/blog/images/qtwidgetsexamples/08_containers/04_tab_widget.png)

```python
{% include src/qtwidgetsexamples/08_containers/04_tab_widget.py %}
```

`QTabWidget` is a tabbed container widget - when you click on a tab its associated page is shown. To use it in your application

1. Create a `QTabWidget` object. 

2. Create its intended child widgets. Each page contains a single widget but that widget, in turn, can be a `QWidget` or a container class which allows you to pack multiple children into a `QTabWidget` page.

3. Use `QTabWidget.addTab()` to add the child widgets to the tab widget object. In the example we have two `QWidget`s and add each to the tab widget. The first `QWidget` has three check boxes as its children and the second `QWidget`s  children are three radio buttons.

The tab indexes start with zero so the first tab has the index of `0` and the second has the index of `1`. Each tab has a label (`Styles` and `Margins` in the example). You can change the tab position (`North`, `South`, `West` and `East`) and shape (`Rounded` and `Triangular`). 