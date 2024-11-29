---
title: QObject.moveToThread() Reuse Thread  - Walk the Filesystem
layout: default
nav_order: 4
parent: 01 Move QObject to Thread
---

## QObject.moveToThread() Walk the Filesystem Reusing the Thread

```python
{% include src/qtwidgetsexamples/11_multithreading/01_movetothread/04_movetothread_walkfs_reuse_thread.py %}
```

Let's see a more realistic example of reusing the worker thread. To walk the file system from the worker thread method

1. Create the worker class. There are several differences from [the first walk filesystem example]({% link docs/qt_widgets/11_multithreading/01_movetothread/02_movetothread_walk_filesystem.md %}): Instead of using `QThread.isInterruptionRequested()` to check if we should interrupt the `do_work()` method we use a boolean flag named `Worker.interruption_requested`. We also add two methods, `Worker.stop()` and `Worker.reset()` to set `interruption_requested` to `True` and `False`. Finally each use of `Worker.interruption_requested` is guarded with the `QMutextLocker` - `QMutex` pair.

2. In `Controller.__init__()` create the worker thread object,

3. Create the worker object and move it to the worker thread using `QObject.moveToThread()`

4. Connect the signals with the slots. When the main class emits the `operate` signal the `Worker.do_work()` method is executed.

5. Start the worker thread.

6. On the start button click reset the worker using `Worker.reset()` and emit the `operate` signal,

7. On the cancel button click stop the worker using `Worker.stop()`,

8. Quit the thread when the main window is closed.

But how did we end up using a boolean flag guarded with `QMutexLock` to control the worker execution? Turns out that `QThread.requestInterruption()` can only be used one time: once you use it to request the thread interruption `QThread.isInterruptionRequested()` will always return `True` and there is no way you can un-request it. Sending a signal from the main thread to toggle a custom boolean flag in the worker (ie `Worker.interruption_requested`) would work but only if we used `QApplication.processEvents()` - we have a blocking loop which means no signals are processed otherwise. Setting the flag directly might seem to work but it is not thread-safe as the worker and the main class are in different threads, so we guard each use of `Worker.interruption_requested` with `QMutex` - `QMutexLock` making sure its value is consistent.