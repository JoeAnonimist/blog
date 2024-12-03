---
title: QStatusBar
layout: default
nav_order: 2
parent: 09 Main Window
---

## Main Window's Status Bar

![QMainWindow status bar](/blog/images/qtwidgetsexamples/09_main_window/02_status_bar.png)

```python
{% include src/qtwidgetsexamples/09_main_window/02_status_bar.py %}
```

The `QStatusBar` class represents the main window status bar. It can display three kinds of information:

- Temporary, eg. short help messages,
- Normal, eg. row and column number
- Permanent, eg. the Caps Lock status

To use it in your application

1. Create the widgets to hold the desired status information. In the example we create two labels, one to display the cursor row and column and the other to display total character count.

2. Add the widgets to the status bar. You access the status bar using the `QMainWindow.statusBar()` method and add widgets to it with either `addWidget()` or `addPermanentWidget()`. The widgets added with the former method are placed on the left and the widgets added with the latter are placed on the right hand side of the status bar.

3. Use the appropriate signals to display the status information. In the example we display three pieces of information: the total character count, which displayed permanently, the current cursor position (normal) and a message to notify the user when there is selected text available for copying (temporary). The temporary message, "Copy available!" is displayed for two seconds and hides the normal status widgets but does not hide the permanent status information.