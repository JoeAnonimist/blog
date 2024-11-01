---
title: QTextEdit Example
layout: default
nav_order: 4
parent: 05 Input Widgets
---

## PySide6 QTextEdit Example

![QTextEdit](/blog/images/qtwidgetsexamples/05_input_widgets/04_text_edit.png)

```python
{% include src/qtwidgetsexamples/05_input_widgets/04_text_edit.py %}
```

`QTextEdit` is a ready-made rich text editor you can use in your applications. The text can be described using markdown or a subset of HTML. It comes with scrollbars, a right-click menu and standard keyboard shortcuts. To use `QTextEdit` in your application

1. Create a `QTextEdit` object. One of the `QTextEdit` constructors accepts initial text which is interpreted as HTML.

2. Write the slot methods. You can access the plain text from the `QTextObject` using its `toPlainText()` method. You can access the styled text using the `toMarkdown()` and `toHtml()` methods. You can access the underlying `QTextDocument` using the `document()` method.

3. Connect the signals with the slots. In this example we highlight the word under cursor using `QTextCursor.selection()` and `QTextCharFormat`. To restore the previous formatting we keep track 