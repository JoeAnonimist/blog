---
title: QObject.moveToThread() Reuse Thread  - Walk the Filesystem
layout: default
nav_order: 5
parent: 01 Move QObject to Thread
---

## Signals and Slots Across Threads


| Connection Type | Emitter Thread | Receiver Thread | Invoked                                    | Executed In           | Blocks | Unique |
|-----------------|----------------|-----------------|--------------------------------------------|-----------------------|--------|--------|
| Auto            | Thread A       | Thread A        | immediately when<br/>the signal is emitted | Thread A              |        | No     |
| Auto            | Thread A       | Thread B        | when control returns to the<br/>event loop of the receiver's thread | Thread B              |        | No     |
| Direct          | Thread A       | Thread B        | immediately when<br/>the signal is emitted | Thread A              |        | No     |
| Queued          | Thread A       | Thread B        | when control returns to the<br/>event loop of the receiver's thread | Thread B              |        | No     |
| Blocking Queued | Thread A       | Thread B        | when control returns to the<br/>event loop of the receiver's thread | Thread B              |        | No     |
| Unique          | Thread A       | Thread A        | immediately when<br/>the signal is emitted | Thread A              |        | Yes    |
| Unique          | Thread A       | Thread B        | when control returns to the<br/>event loop of the receiver's thread | Thread B              |        | Yes    |


```python
{% include src/qtwidgetsexamples/11_multithreading/01_movetothread/05_signals_and_slots_across_threads.py %}
```
