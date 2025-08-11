---
title: Signals and Slots Across Threads
layout: default
nav_order: 5
parent: 01 Move QObject to Thread
---

## Signals and Slots Across Threads


| Connection Type | Emitter Thread | Receiver Thread |       Invoked                                    | Executed In           | Blocks | Unique |
|-----------------|----------------|-----------------|--------------------------------------------|-----------------------|--------|--------|
| Auto            |        A       |        A        | immediately when the signal is emitted |        A              |        | No     |
| Auto            |        A       |        B        | when control returns to the event loop of the receiver's thread |        B              |        | No     |
| Direct          |        A       |        B        | immediately when the signal is emitted |        A              |        | No     |
| Queued          |        A       |        B        | when control returns to the event loop of the receiver's thread |        B              |        | No     |
| Blocking Queued |        A       |        B        | when control returns to the event loop of the receiver's thread |        B              |        | No     |
| Unique          |        A       |        A        | immediately when the signal is emitted |        A              |        | Yes    |
| Unique          |        A       |        B        | when control returns to the event loop of the receiver's thread |        B              |        | Yes    |


```python
{% include src/qtwidgetsexamples/11_multithreading/01_movetothread/05_signals_and_slots_across_threads.py %}
```
