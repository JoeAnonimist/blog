---
title: Monitor File Creation
layout: default
nav_order: 1
parent: Miscellaneous
tags: monitoring
---

## Monitor File Creation Using `QFileSystemModel`

```python
{% include src/miscellaneous/0001_monitor_file_creation.py %}
```

The need to monitor file system events - file or directory creation, modification or deletion comes up fairly often. There's a Qt class named `QFileSystemWatcher` that lets do this but this class' `directoryChanged` signal does not report which file from the monitored directory has triggered it. In the example, instead of `QFileSystemWatcher`, we (ab)use the `QFileSystemModel` class whose `rowsInserted` signal lets us get the created file name. To monitor a directory for file creation

1. Create a `QFileSystemModel` object, set its root path to the path of the directory you want to monitor, and add a filter to exclude subdirectories.

2. Create the slot method to handle the `rowsInserted` signals. `rowsInserted` passes the `first` and the `last` row that was changed and we use the row numbers to get `QModelIndex` instances and the changed files names and set the label text to their paths.

3. Connect the signal and the slot.