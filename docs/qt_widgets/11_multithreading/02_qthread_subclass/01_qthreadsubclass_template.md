---
title: QThread Subclass Template
layout: default
nav_order: 1
parent: 02 QThread Subclass
---

## QThread Subclass Template

Perhaps the most important thing to remember about `QThread` is that **a `QThread` object does not represent an operating system thread - it is a thread manager**. What this means in practice is that only the `QThread.run()` method will be executed in the new thread. All other `QThread` methods are executed in the thread that created the `QThread` object.

Another thing to have in mind when subclassing `QThread` is that **a `QThread` subclass does not start its event loop unless you explicitly start one by calling `QThread.exec()` in your `QThread.run()` implementation.**

```python
{% include src/qtwidgetsexamples/11_multithreading/02_qthread_subclass/01_qthreadsubclass_template.py %}
```

There are two ways you can use `QThread` to run a task in a background thread:

- Create a worker object and moving it to a background thread using `QObject.moveToThread()` and
- Create a `QThread` subclass and override its `run()` method.

The first four examples show how to use the `QObject.moveToThread()` method but let's see what a minimal example of a `QThread` subclass could look like:

1. Create a `QThread` subclass (named `WorkerThread` in the example) and override its `run()` method. Add your custom signals to the `QThread` subclass and emit them from `run()` to communicate with the main thread.

2. In your main window class create a `WorkerThread` instance

3. Connect the `WorkerThread` signals with the main window slots. Also connect the `WorkerThread.finished` signal with the `WorkerThread.deleteLater` slot to make sure the worker thread exits cleanly.

4. In the main window create the slots to handle `WorkerThread` signals. In the example we set a `QLabel`s text to "Hello, World" when the `WorkerThread.result_ready` signal is emitted.

5. Start the worker thread.

When you create a `QThread` object without subclassing it (like we do in the `moveToThread()` examples) the following sequence of actions occurs:

- You call `QThread.start()` from the main thread to start the background thread,
- The background `QThread` emits its `started` signal,
- `QThread.start()` calls the `QThread.run()` method,
- `QThread.run()` calls `QThread.exec()`,
- `QThread.exec()` enters the thread-local event loop and waits for `QThread.exit()` or `QThread.quit()` to be called,
- You call `QThread.exit()` or `QThread.quit()` to stop the background thread,
- The thread-local event loop stops running and the `QThread.finished` signals is emitted,
- The `QObjects` for which `QObject.deleteLater()` was called are deleted.

(Remember how in the `moveToThread` examples we connected the `QThread.started` signal with a worker object slot so that the slot was executed immediately on `QThread.start()`; and also connected the worker `finished` signal with `QThread.quit()` so that the `QThread` finishes as soon as the worker object slot returned)

When you subclass `QThread`, the subclass does not run its local event loop unless you explicitly call `QThread.exec()` in your `QThread.run()` implementation. If your `QThread` subclass runs without an event loop it won't be able to use the classes that need one (like `QTimer`, `QTcpSocket` and `QProcess`). It will be able to emit signals however.

In the example, `Window.start_work_in_a_thread()` is executed in the main thread and `QThread.loopLevel()` is one which means that the main thread event loop is running. `WorkerThread.__init__()` is also executed in the main loop while only `WorkerThread.run()` is executed in the worker thread and `QThread.loopLevel()` is equal to zero which means that the worker thread event loop is not running.