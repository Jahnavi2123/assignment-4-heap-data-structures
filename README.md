# Assignment 4: Heap Data Structures – Implementation, Analysis, and Applications

---

# Project Overview

This project explores heap data structures and their applications in sorting and task scheduling.

The assignment includes:

1. Implementation of Heapsort
2. Comparison of Heapsort with Quicksort and Merge Sort
3. Implementation of a Priority Queue using a Binary Max Heap
4. Development of a simple task scheduler using the priority queue

---

# Repository Structure

```text
assignment-4-heap-data-structures/
│
├── heapsort.py
├── quicksort.py
├── merge_sort.py
├── benchmark.py
├── priority_queue.py
├── scheduler.py
├── report.md
└── README.md
```

---

# Requirements

- Python 3.8+
- No external libraries required

---

# Running the Programs

### Heapsort

```bash
python3 heapsort.py
```

### Quicksort

```bash
python3 quicksort.py
```

### Merge Sort

```bash
python3 merge_sort.py
```

### Benchmark Comparison

```bash
python3 benchmark.py
```

### Priority Queue Demo

```bash
python3 priority_queue.py
```

### Scheduler Simulation

```bash
python3 scheduler.py
```

---

# Benchmark Results

| Size | Distribution | Heapsort | Quicksort | Merge Sort |
|------|-------------|-----------|------------|------------|
|100|Random|0.000033|0.000032|0.000042|
|100|Sorted|0.000033|0.000028|0.000032|
|100|Reverse|0.000030|0.000037|0.000034|
|500|Random|0.000236|0.000202|0.000241|
|500|Sorted|0.000220|0.000200|0.000171|
|500|Reverse|0.000212|0.000190|0.000174|
|1000|Random|0.000505|0.000443|0.000567|
|1000|Sorted|0.000521|0.000412|0.000369|
|1000|Reverse|0.000447|0.000407|0.000381|
|2000|Random|0.001157|0.000962|0.003588|
|2000|Sorted|0.001364|0.000926|0.000799|
|2000|Reverse|0.001052|0.000922|0.000800|
|5000|Random|0.003355|0.002718|0.003182|
|5000|Sorted|0.003315|0.002416|0.002039|
|5000|Reverse|0.003005|0.002472|0.002168|

---

# Scheduler Results

| Task | Priority | Arrival | Start | Finish | Wait | Deadline | Met Deadline |
|------|-----------|----------|--------|---------|------|-----------|---------------|
|1|3|0|0|3|0|8|Yes|
|2|5|1|3|5|2|6|Yes|
|4|4|4|5|7|1|10|Yes|
|3|2|2|7|11|5|12|Yes|
|5|1|5|11|12|6|15|Yes|

Average Waiting Time: **2.80**

Deadlines Met: **5/5**

---

# Summary of Findings

- Quicksort achieved the fastest execution times in most tests.
- Heapsort maintained stable performance across all input types.
- Merge Sort showed strong performance on ordered inputs.
- The priority queue correctly maintained heap ordering after priority updates.
- The scheduler successfully completed all tasks before their deadlines.
- Lower-priority tasks experienced longer waiting times, illustrating the trade-offs in priority-based scheduling.

---

# Complexity Summary

## Heapsort

| Case | Complexity |
|------|------------|
|Best|O(n log n)|
|Average|O(n log n)|
|Worst|O(n log n)|

Algorithm auxiliary space:

```text
O(1)
```

Current implementation (due to copying input):

```text
O(n)
```

---

## Priority Queue

| Operation | Complexity |
|-----------|------------|
|insert()|O(log n)|
|extract_max()|O(log n)|
|increase_key()|O(log n)|
|decrease_key()|O(log n)|
|peek_max()|O(1)|
|is_empty()|O(1)|

---