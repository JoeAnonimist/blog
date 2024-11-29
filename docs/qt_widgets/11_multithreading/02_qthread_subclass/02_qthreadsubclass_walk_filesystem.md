---
title: QThread Subclass Walk the Filesystem
layout: default
nav_order: 2
parent: 02 QThread Subclass
---

## QThread Subclass Walk the Filesystem

```python
{% include src/qtwidgetsexamples/11_multithreading/02_qthread_subclass/02_qthreadsubclass_walk_filesystem.py %}
```

Now let's walk the filesystem using a `QThread` subclass:

1. Create a `QThread` subclass named `WorkerThread` and override its `run()` method. In `run()` we first print the current thread object name to show that it indeed runs in the worker thread and after that we use `os.walk` to walk the filesystem recursively. For each filesystem object we emit the `progress` signal with the object's name as the argument. Then, in the main window

2. On the start button click create a `WorkerThread` object and set its object name to "Worker thread",

3. Connect the signals with the slots. Each time `WorkerThread.progress` is emitted we execute `Window.on_progress)` which sets the label's text to the filesystem object name that `progress` emits as the argument. We also connect the `WorkerThread.finished` signal with `WorkerThread.deleteLater()` to dispose of the thread when it finishes.

4. Handle the signals. When `WorkerThread.progress` is emitted `Window.on_progress()` updates the label text. When the cancel button is clicked we request the worker thread interruption using `QThread.requestInterruption()` and wait for it to finish.

5. Start the worker thread each time the start button is clicked.

To make sure the thread is deleted when the user closes the main window we also override `Qwidget.closeEvent()`. Note that we didn't need to call `QThread.quit()` but only `QThread.wait()` because the thread event loop is not running.