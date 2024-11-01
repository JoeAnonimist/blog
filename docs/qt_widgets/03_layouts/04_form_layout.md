---
title: QFormLayout Demo
layout: default
nav_order: 4
parent: 03 Layouts
---

## PySide6 QFormLayout Example

![QFormLayout](/blog/images/qtwidgetsexamples/03_layouts/04_form_layout.png)

```python
{% include src/qtwidgetsexamples/03_layouts/04_form_layout.py %}
```

`QFormLayout` lays out its child widgets in a two-column form. You can use `QFormLayout.addRow()` to  add widgets to the form layout along with its associated label similar to HTML forms. To use `QFormLayout` in your application

1. Create a `QFormLayout` instance and set it as the `QWidget` layout

2. Create child widgets. Since we'll need to access the widgets from the slot method make the widgets instance members of `Window`.

3. Add child widgets to the form using `QFormLayout.addRow(label_text, widget)` to add the label-widget pair to the layout. `addRow()` is a convenience method so you can add two widgets to the layout at a time but you can still use `addWidget()` as with `QVBoxLayout`.

In the example form we have three `QLineEdit` widgets and handle their `editingFinished` with a single slot. `editingFinished` is emitted when the Return or Enter key is pressed or when the line edit whose contents have changed loses focus. The slot simply  sets `summary_label` text to the values of the three `QLineEdit` widgets.