---
title: QObject.moveToThread() Walk the Filesystem
layout: default
nav_order: 2
parent: 01 Move QObject to Thread
---

## QObject.moveToThread() Walk the Filesystem

```python
{% include src/qtwidgetsexamples/11_multithreading/01_movetothread/02_movetothread_walk_filesystem.py %}
```

In [the `moveToThread()` template]({% link docs/qt_widgets/11_multithreading/01_movetothread/01_movetothread_template.md %}) we saw a template for moving a `QObject` to a `QThread` but the worker object object did nothing but print a message in the terminal. Now let's see a more realistic example - the `Worker.process()` method walks the file system using `os.walk()` starting from the file system root. This can take some time and would actually block the Gui if done from the main thread. To walk the file system from the background thread using `QObject.moveToThread()`

1. Create the worker class. The method to be executed is called `process()` just as in the template script but now it uses the Python `os.walk()` to walk the file system. For each file system object `walk()` enumerates we emit a custom signal named `progress` that we added to `Worker` along with `finished` and `error`. If something requests the background thread interruption we return from the `process()` method which triggers the signal and slot chain to stop and delete both the worker object and the background thread. Note how in `Worker.process()` we access the current (ie background) thread using the static `QThread.currentThread()` method.

2. In the main window class, create the thread object.

3. Create a `Worker` object and move it to the created `QThread` using `QObject.moveToThread()`

4. Use signals and slots to make sure that both the worker and the background thread are created and deleted properly: - starting the background thread triggers the `Worker.process()` execution - `QObject.finished` triggers both `QThread.quit()` and `Worker.deleteLater()` - `QThread.finished` triggers `QThread.deleteLater()`.

5. Finally start the background thread. All this happens in the `Window.on_start_button_clicked()` slot which means new `QThread` and `Worker` objects are created each time the start button is clicked.

One thing to note is that we override `QWidget.closeEvent()` to interrupt the background thread which makes sure the thread and the worker are deleted if the user closes the main window while the thread is still running. The same sequence, `QThread.requestInterruption()` + `QThread.quit()` + `QThread.wait()`, is used in `Window.on_cancel_button_clicked()` to make sure that the background thread exits cleanly when interrupted.
