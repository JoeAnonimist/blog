---
title: QObject.moveToThread() Template
layout: default
nav_order: 1
parent: 01 Move QObject to Thread
---

## QObject.moveToThread() Template

```python
{% include src/qtwidgetsexamples/11_multithreading/01_movetothread/01_movetothread_template.py %}
```

In [the previous example]({% link docs/qt_widgets/01_template_scripts/template1.md %}) we demonstrated how a PySide6 Gui can become nonresponsive. Now let's see how we can use Qt threads to execute long running tasks in the background while keeping the Gui responsive

1. Create a `QObject` subclass that contains a slot / method to be executed in a background thread (ie a thread other than the Gui thread). In the example, the slot to be executed is called `process()` and simply prints a message and emits a custom signal named `finished` before it returns. This is how you communicate between Qt threads - using signals and slots. In addition to `finished` the `Worker` class declares another signal named `error` which we never call but would be emitted on error conditions in the `process()` execution.

In the main window class

2. Create a `QThread` object named `background_thread` or something similar (don't call it `thread` as that name is already taken). Note how we use `self` to make `background_thread` the main window member - this makes sure `background_thread` doesn't go out of scope while the thread is still running.

3. Create a `Worker` object and use `QObject.moveToThread()` to move it to `background_thread`. Now `process()` will be executed in `background_thread`.

4. Connect the appropriate signals and slots:
    - connect the `background_thread.started` signal with the `worker.process()` slot. This means that `process()` will be executed as soon as the background thread is started,