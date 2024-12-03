---
title: QThreadPool Walk the Filesystem
layout: default
nav_order: 2
parent: 03 QThreadPool
---

## QThreadPool Walk the Filesystem

```python
{% include src/qtwidgetsexamples/11_multithreading/03_qthreadpool/02_threadpool_walk_filesystem.py %}
```

Let's see what the "walk the filesystem" example looks like rewritten to use the `QThreadPool` - `QRunnable` pair:

1. Create a `QRunnable` subclass and implement its `run()` method. Add a member variable that contains the signals to be emitted from the runnable. Also add a Boolean flag named `do_work` to signal the `run()` method interruption. The `run()` method itself uses the Python `os.walk()` method to enumerate filesystem objects and reports each enumerated object by emitting the `progress` signal.

2. In the main window class, add a custom signal when the background task needs to be interrupted named `cancel_unnable`. Connect `cancel_runnable` with the `Runnable.on_cancel_emitted` slot that sets the `Runnable.do_work` flag to `False`.

3. In the main window `on_start_button_clicked` create a `Runnable` object and connects the signals with the slots. When the `progress` signal is emitted we set the label's text to the reported file or directory. When the cancel button is clicked and the `cancel_runnable` signal emitted we change the `Runnable.do_work` value to `False`.

4. Access the global instance of the thread pool and run the task using `QThreadPool.start()` method.