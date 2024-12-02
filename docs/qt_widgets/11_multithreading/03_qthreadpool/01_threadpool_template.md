---
title: QThreadPool Template
layout: default
nav_order: 1
parent: 03 QThreadPool
---

## A Minimal `QThreadPool` Example

```python
{% include src/qtwidgetsexamples/11_multithreading/03_qthreadpool/01_threadpool_template.py %}
```

The `QThreadPool` class manages a collection of `QThread`s and is used together with the `QRunnable` class. To use it in your application

1. Create a `QRunnable` subclass and implement its `run()` method to contain the code you want to execute in a background thread. `QRunnable` itself is not a subclass of `QObject` so you can not add signals to it directly but you can easily work around this limitation by creating a separate `QObject` subclass (named `Signals` in the example) and adding an object of that class to your `QRunnable`. In the example the `run()` methods emits the `Signals.progress` signal and prints a message in the terminal.

2. In the main window, create a `Runnable` instance

3. Use `QThreadPool.globalInstance()` to get a reference to the global thread pool instance and `QThreadPool.start()` to execute the `Runnable.run()` method in one of the threads the global thread pool manages.