---
title: QMainWindow Toolbar Example
layout: default
nav_order: 4
parent: 09 Main Window
---

## PySide6 QMainWindow Toolbar Example

![QMainWindow toolbar](/blog/images/qtwidgetsexamples/09_main_window/04_toolbar.png)

```python
{% include src/qtwidgetsexamples/09_main_window/04_toolbar.py %}
```

The `QToolBar` class represents an application toolbar. To use it in your application

1. Create the toolbar using `QMainWindow.addToolBar()`.

2. Add `QAction`s, `QWidget`s and separators to it. Note how we reuse the same `QAction`s for both the toolbar and the menu. We also add icons to the actions and they appear both in the menu items and on the toolbar.