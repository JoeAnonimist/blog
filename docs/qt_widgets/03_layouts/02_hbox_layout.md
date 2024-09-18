---
title: QHBoxLayout Demo
layout: default
nav_order: 2
parent: 03 Layouts
---

## PySide6 QHBoxLayout Example

```python
{% include src/qtwidgetsexamples/03_layouts/02_hbox_layout.py %}
```

`QHBoxLayout` lines up its child widgets horizontally. The steps to use it in your application are the same as for `QVBoxLayout` but here they are anyway:

1. Create the layout and set it as a `QWidget`'s layout using `QWidget.setLayout()`

2. Create child widgets. In this example we create a `QPushButton` and a `QLabel`. We also set the `QLabel` minimum width to accommodate for the width of the text it will hold.

3. Add the widgets and add them to the layout using `QHBoxLayout.addWidget()` in order you want them to appear in the layout.

We also add some interactivity to the window by handling the `QPushButtons` click events and set `QLabel`'s text to the current time. This brings us to an important point: Qt is more than a GUI framework - it is packed with features that you could use in a non-GUI application. But so is Python, the 'batteries included' programming language which leads to duplication of functionality, and it's up to the developer to decide whether to use eg. Python's `time`, Qt's `QTime` or something entirely different.

Here are a few Qt classes from the `QtCore` namespace just to get the taste of what is available:

- `QCalendar`
- `QDate`
- `QDateTime`
- `QDir`
- `QFile`
- `QFileSystemWatcher`
- `QJsonDocument`
- `QJsonObject`
- `QRandomGenerator`
- `QRegularExpression`
- `QSettings`
- `QStandardPaths`
- `QStorageInfo`
- `QSysInfo`
- `QTextStream`
- `QThread`
- `QTime`
- `QUrl`
- `QUuid`
- `QXmlStreamReader`
- `QXmlStreamWriter`
