---
title: QSplitter Example
layout: default
nav_order: 5
parent: 08 Containers
---

## PySide6 QSplitter Example

![QSplitter](/blog/images/qtwidgetsexamples/08_containers/05_splitters.png)

```python
{% include src/qtwidgetsexamples/08_containers/05_splitters.py %}
```

The `QSplitter` class lets the user resize its child widgets using the mouse.To use it in your application

1. Create the `QSplitter` object. It lays its child widgets horizontally by default but you can change that using the `QSplitter.setOrientation()` method.

2. Create the child widgets. In the example we create three `QGroupBox` objects. We also add two radio buttons to the first group box - selecting the buttons changes the `QSplitter` orientation dynamically.

3. Add the child widgets to the splitter.