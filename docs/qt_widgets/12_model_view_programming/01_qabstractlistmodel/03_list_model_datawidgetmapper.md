---
title: Using QDataWidgetMapper with a QAbstractListModel Subclass
layout: default
nav_order: 3
parent: 01 QAbstractListModel Examples
---

## Using `QDataWidgetMapper` with a `QAbstractListModel` Subclass

```python
{% include src/qtwidgetsexamples/12_model_view_programming/01_qabstractlistmodel/03_list_model_datawidgetmapper.py %}
```

`QDataWidgetMapper` lets you map a model row (or column) to a set of widgets - this comes in handy when creating forms and makes data viewing/editing more comfortable for the user. To use it in your application

1. Create a `QAbstractListModel` subclass to represent your model, then, in the main window class

2. Create your model object and the widgets for displaying and editing your model data

3. Create the mapper object and use `QDataWidgetMapper.setModel()` to connect your model with it

4. Use `QDataWidgetMapper.addMapping()` to map your model columns with the widgets. The model from the example has only one column and we map it to a `QLineEdit` widget.

5. Synchronize the view current item with the model current index so that both are updated when the user changes the view current item.

In the example we set the mapper submit policy to manual and update the model on the 'Submit` button click. Now the line edit text changes according to the current view item and the user can update the current model item by changing the line edit value and clicking the 'Submit' button.