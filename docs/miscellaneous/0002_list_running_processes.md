---
title: List Running Processes
layout: default
nav_order: 2
parent: Miscellaneous
tags: processes, QListWidget
---

## List Running Processes in a `QListWidget`

![List running processes](/blog/images/miscellaneous/0002_list_running_processes.png)

```python
{% include src/miscellaneous/0002_list_running_processes.py %}
```

The `psutil` Python module lets you get various information about your operating system and, among other things, you can use it to list the running processes on your machine. To use `psutil` to list the currently active processes in a `QListWidget`

1. Create a `QListWidget` object.

2. Use `psutil.process_iter()` to get the running processes. For each process create a `QListWidgetItem` instance and set its text to the process name. Use `QListWidgetItem.setData()` to add additional information about the process to the `QListWidgetItem` setting the data role to the `Qt.ItemDataRole.UserRole` constant.

3. Add the list widget object to the window layout.

4. Optionally, display the additional data about a process when the user clicks on its item.