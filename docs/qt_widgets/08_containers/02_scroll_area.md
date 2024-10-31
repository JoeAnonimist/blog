---
title: QScrollArea Example
layout: default
nav_order: 2
parent: 08 Containers
---

## PySide6 QScrollArea Example

```python
{% include src/qtwidgetsexamples/08_containers/02_scroll_area.py %}
```

If a `QScrollArea`' child widget exceeds its size it provides scrollbars so that the whole child widget can be viewed. To use it in your application

1. Create a `QScrollArea` object

2. Create the child widget. In the example we use a `QPlainTextEdit` object and set its wrap mode to `WrapMode.NoWrap` so that it expands when text is entered

3. Add the `QPlainTextEdit` to the scroll area using `QScrollArea.addWidget()`. We also set the `QScrollArea.widgetResizable` property to `True` so that the text box resizes along with the scroll area.

Now if you enter a long line of text in the text box the scroll area shows the horizontal scrollbar and if you enter several lines the scroll area shows the vertical scrollbar.