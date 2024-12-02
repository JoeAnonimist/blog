---
title: QObject.moveToThread() Template
layout: default
nav_order: 1
parent: 01 Move QObject to Thread
---

## A Minimal `QObject.moveToThread()` Example

```python
{% include src/qtwidgetsexamples/11_multithreading/01_movetothread/01_movetothread_template.py %}
```

[The previous example]({% link docs/qt_widgets/01_template_scripts/template1.md %}) shows how a PySide6 Gui can become non-responsive. Now let's see how we can use Qt threads to execute long running tasks in the background while keeping the Gui responsive:

1. Create a `QObject` subclass that contains the slot / method to be executed in a background thread (ie a thread other than the Gui thread). In the example, the slot is named `process()` and simply prints a message and emits a custom signal named `finished` before it returns. This is how you communicate between `QThread`s - using signals and slots. In addition to `finished` the `Worker` class declares another signal named `error` which we never call but would be emitted on error conditions in the `process()` execution. Then, in the main window class

2. Create a `QThread` object named `background_thread` or something similar (don't call it `thread` as that name is already taken). Note how we use `self` to make `background_thread` the main window member - this ensures that `background_thread` doesn't go out of scope while the thread is still running.

3. Create a `Worker` object and use `QObject.moveToThread()` to move it to `background_thread`. Now the `Worker.process()` method will be executed in `background_thread`.

4. Connect the appropriate signals and slots:
    - connect the `background_thread.started` signal with the `worker.process()` slot. This means that `Worker.process()` will be executed as soon as the background thread is started,
    - connect the `Worker.finished` signal with the `background_thread.quit` method. This means that the background thread will quit as soon as the `Worker.process()` method returns,
    - connect the `Worker.finished` signal with the `Worker.deleteLater()` method. This means that the worker object will be deleted some time after it emits the `finished` signal.
    - connect the `background_thread.finished` signal with the `background_thread.deleteLater()` method. This means that the background thread will be deleted some time after it finishes.
    
5. Finally, start the `background_thread` using the `QThread.start()` method.

With the above setup the `process()` method is executed as soon as the thread is started, the thread quits as soon as the method returns and both the worker object and the thread object are destroyed while the Gui stays responsive.