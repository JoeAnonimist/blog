---
title: Menus
layout: default
nav_order: 3
parent: 09 Main Window
---

## Menus

![QMainWindow menus](/blog/images/qtwidgetsexamples/09_main_window/03_menus.png)

```python
{% include src/qtwidgetsexamples/09_main_window/03_menus.py %}
```

The `QMenuBar` class represents a horizontal menu bar, the `QMenu` class represents a menu widget and the `QAction` class represents user commands. To add drop-down menus to your main window

1. Get the reference to the main window menu bar using `QMainWindow.menuBar()` and add the menu to it using `QMenuBar.addMenu()`.

2. Create a `QAction` object and connect a slot to its `triggered` signal. The `QAction` needs to live for the entire `Editor` lifetime so set it as its member variable.

3. Add the action to the menu using the `QMenu.addAction()` method.

Optionally you can assign keyboard shortcuts to menus (accelerators) adding ampersand characters to their text. For instance, `&File` will open the File menu. Adding an ampersand does not work for `QAction` objects so you need to add keyboard shortcuts to them using `QAction.setShortcut()`