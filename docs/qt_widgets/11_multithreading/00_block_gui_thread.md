---
title: 00 Block the Qt QUI Thread
layout: default
parent: 11 Multithreading
nav_order: 0
---

## Block the Qt GUI Thread or how not to do things

```python
{% include src/qtwidgetsexamples/11_multithreading/00_block_gui_thread.py %}
```

Threads of execution let you execute your code concurrently sharing the program memory and other resources and are represented in Qt by the `QThread` class. There are two use cases for threads:

- Make processing faster by using more than one processor core,
- Keep the Gui thread responsive by moving long running tasks to other threads

We'll focus on the second one but first let's see what a nonresponsive Qt Gui looks like. To demonstrate a long lasting task that blocks the Gui

1. Create the task. In the example we use `os.walk()` and a blocking ("tight") `for` loop to search the file system for a bogus file. We also try to report progress after each file using a custom Qt signal. This does not work because the loop blocks the Qt event loop and no signals are sent or events processed until the loop exits. The loop is executed in the main application thread (also called the Gui thread) so the whole application becomes nonresponsive - it freezes and you can't even close it.

2. Create a push button,

3. Create a slot that starts the long running task when the push button is clicked.
