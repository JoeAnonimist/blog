---
title: QLineEdit
layout: default
nav_order: 1
parent: 05 Input Widgets
---

## `QLineEdit`

![QLineEdit](/blog/images/qtwidgetsexamples/05_input_widgets/01_line_edit.png)

```python
{% include src/qtwidgetsexamples/05_input_widgets/01_line_edit.py %}
```
`QLineEdit` lets you edit a line of plain text. You can enter, `copy()`, `cut()`, `paste()`, `undo()`, `redo()` or `selectAll()` the text using the standard keyboard shortcuts or the built-in context menu. You can constrain the text content using `QValidator`s or input masks. This example features a `QRegularExpressionValidator` that allows only alphabetic input. You can turn it into a password input field setting its `echoMode` property to `EchoMode.Password`. To use `QLineEdit` in your application

1. Create a `QLineEdit` instance and add it to a layout.

2. Create the slots to handle `QLineEdit` signals. The `textChanged` signal is emitted whenever the line edit text changes. The `editingFinished` signal is emitted when the Enter key is pressed or the line edit widget loses focus. The `inputRejected` signal is emitted when the user tries to enter invalid input. In this example all three slots set the label text based on the emitted signal.

3. Connect the signals with the slot methods using the standard PySide6 notation.

Note how we connect the `QLineEdit.textChanged` signal directly to `QLabel.setText`. We didn't need to write a custom slot in our code to handle `textChanged`.  `QLabel.setText` is itself a slot and their signatures match: `textChanged` emits a string and `setText` accepts a string, so we were able to save a few lines of code.