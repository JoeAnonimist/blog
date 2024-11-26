---
title: QThread Subclass Template
layout: default
nav_order: 1
parent: 02 QThread Subclass
---

## QThread Subclass Template

```python
{% include src/qtwidgetsexamples/11_multithreading/02_qthread_subclass/01_qthreadsubclass_template.py %}
```

There are two ways you can use `QThread` to run a task in a background thread:

- Create a worker object and moving it to a background thread using `QObject.moveToThread()` and
- Create a `QThread` subclass and override its `run()` method.

The first four examples show to use `QObject.moveToThread()` but let's see an example of a `QThread` subclass:

1. 