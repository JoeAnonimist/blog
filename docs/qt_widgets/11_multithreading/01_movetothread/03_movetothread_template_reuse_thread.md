---
title: QObject.moveToThread() Reuse Thread Template
layout: default
nav_order: 3
parent: 01 Move QObject to Thread
---

## Use the Same `QThread` Object Multiple Times

```python
{% include src/qtwidgetsexamples/11_multithreading/01_movetothread/03_movetothread_template_reuse_thread.py %}
```

In the first two examples the background/worker thread is created each time we want to execute the long running task but in [the example from the `QThread` documentation](https://doc.qt.io/qt-6/qthread.html) both the thread and the worker objects are created in the main class constructor so let's try to replicate that:

1. Create the worker class. The method to be executed in the background is called `do_work()` just as in the `QThread` documentation. Then, in the main window class

2. Create the worker thread,

3. Create the `Worker` object and move it to the the worker thread using `QObject.moveToThread()`,

4. Connect the signals with the slots. We want the worker object deleted when the thread finishes so we connect `QThread.finished` with `QObject.deleteLater`. We want to send a custom signal (`operate`) to the worker object to start the work so we connect `Controller.operate` with `Worker.do_work`. Finally, we connect `Worker.result_ready` with `Controller.handle_result` so we can handle the `do_work` result in the main class.

5. Start the worker thread. The steps 2 through 5 are executed in the `Controller.__init__()` method which means both the thread and the worker objects will exist until the main window is closed or we delete them explicitly.

6. On the button click emit the `operate` signal. This executes the `Worker.do_work()` method.

7. Override `QWidget.closeEvent()` to quit the thread using the `QThread.quit()` and `QThread.wait()` pair.