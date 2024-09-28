---
title: QPushButton Example
layout: default
nav_order: 1
parent: 04 Buttons
---

## PySide6 QPushButton Example

```python
{% include src/qtwidgetsexamples/04_buttons/01_push_button.py %}
```

QPushButton is a simple widget and is a commonly used Gui element. It sends `clicked`, `pressed`, `released` and `toggled` signals. `toggled` is useful only if you set `QPushButton.checkable` property to `True` in which case you effectively turn it into a toggle button - if you press it it stays pressed until you press it again. To use `QPushButton` in your application

1. Create a `QPushButton` object, setting the text to be displayed on the button. You don't have to add text to a button. If you look at [`QPushButton` documentation](https://doc.qt.io/qt-6/qpushbutton.html) you'll notice that the `QPushButton` class has three constructors (those with the same name as the class itself):

    - The one that optionally accepts only the button's parent. If you use it the button will initially be shown without any text

    - The one that, in addition to parent, accepts the text to be displayed on the button. This is the one we use in the example
    
    - The one that, in addition to parent and text, accepts an icon so you can add an image to a button
    
That a class has more than one constructor is a common situation in Qt and in the OOP world in general. The Qt documentation is comprehensive and you can consult it to find the most suitable constructor for your use case.