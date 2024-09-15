---
title: A Signal and Slot Example Using Python Lambdas
layout: default
nav_order: 2
parent: 02 Signals and Slots
---

## A PySide6 Signal and Slot Example using Lambdas

```python
{% include src/qtwidgetsexamples/02_signals_and_slots/02_using_lambdas.py %}
```

The pattern is the same as in [the basic signals-slots example]({% link docs/qt_widgets/02_signals_and_slots/01_basic_example.md %}):

1. Create the widget. It's the same `QPushButton` as in the first script only now we set its `checkable()` property to `True` so it can double as a toggle button. Without this its `checked` property doesn't toggle on mouse click.

2. Connect the `QPushButton.clicked()` signals with slots. There are three things to note here:

    - You can connect a Python lambda function (ie. a  function without a name) instead of an ordinary method/function to a signal,

    - There are two slots (in this case lambdas) connected to the same signal and each will be called when the signal is emitted. You can also connect multiple signals with a single slot.

    - You can use a lambda to pass parameters to a slot. In the script, `checked` that matches the signal signature, but `'Something else'` is additional data passed to the actual function that will handle the signal.
    
(Can you add the `@Slot()` annotation to a lambda?)