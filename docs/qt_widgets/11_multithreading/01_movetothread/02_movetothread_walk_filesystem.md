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

In [the `moveToThread()` template]({% link docs/qt_widgets/11_multithreading/01_movetothread/01_movetothread_template.md %} we saw a template for moving a `QObject` to a `QThread` but the worker object object did nothing but print a message in the terminal. Now let's see a more realistic example - the `Worker.process()` method walks the file system using `os.walk()` starting with the file system root. This can take some time and could actually block the Gui if done from the main thread. To walk the file system from the background thread using `QObject.moveToThread()`

