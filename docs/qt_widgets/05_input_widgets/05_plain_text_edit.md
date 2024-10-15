---
title: QPlainTextEdit Example
layout: default
nav_order: 5
parent: 05 Input Widgets
---

## PySide6 QPlainTextEdit Example

```python
{% include src/qtwidgetsexamples/05_input_widgets/05_plain_text_edit.py %}
```

`QPlainTextEdit` is a multi-line text edit widget. It is used to edit plain text so you can't use it to style text the way you can in `QTextEdit` ie. its formatting abilities are limited. You can use `QSyntaxHighlighter` with it so it is possible to make a simple programming editor with it. If you set `QPlainTextEdit.setEnabled(False)` you can use this widget to display multi-line text that doesn't need to be edited. To use `QPlainTextEdit` in your application

1. Create an instance of `QPLainTextEdit` and optionally set its font using `QFont`. In the example we set the font to Droid Sans Mono, set the font size in pixels and add a style hint to it to use a monospace font if Droid Sans Mono is not installed on the user's system. We also create two labels, one for displaying total character count and another to display cursor position in the `QPLainTextEdit`.

2. Write the slot methods. The first slot the first label's text to the total number of entered characters every time the text in the `QPLainTextEdit` changes. The second slot sets the second label's text to the current cursor position in the `QPLainTextEdit` when the cursor is moved.

    Just like with `QTextEdit` you can access `QPLainTextEdit`'s underlying `QTextDocument` using `QPlainTextEdit.document()` and its `QTextCursor` using `QPLainTextEdit.textCursor()`

3. Add the `QPlainTextEdit` and the two labels to the window's layout and connect the slots to the `QPlainTextEdit`'s `textChanged` and `cursorPositionChanged` signals.