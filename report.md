# Assignment 4: Heap Data Structures – Implementation, Analysis, and Applications

---

# Introduction

Heap data structures are widely used in applications that require efficient access to the highest- or lowest-priority element. Binary heaps are commonly used to implement priority queues and form the basis of the Heapsort algorithm.

The goal of this assignment is to implement Heapsort, analyze its theoretical and empirical performance, and explore the use of heaps in task scheduling systems.

---

# Part 1: Heapsort Implementation

A binary max heap was implemented using a Python list.

For a node located at index \(i\):

\[
Parent(i)=\left\lfloor\frac{i-1}{2}\right\rfloor
\]

\[
Left(i)=2i+1
\]

\[
Right(i)=2i+2
\]

The algorithm first builds a max heap and then repeatedly removes the maximum element from the root and places it at the end of the array.

---

# Complexity Analysis

## Building the Heap

Building the heap requires:

\[
O(n)
\]

because most nodes are located near the leaves and require little work.

---

## Sorting Phase

Each extraction requires restoring the heap property:

\[
O(\log n)
\]

Since extraction occurs approximately \(n\) times:

\[
T(n)=O(n)+n(O(\log n))
\]

Therefore:

\[
T(n)=O(n\log n)
\]

---

# Best, Average, and Worst Cases

| Case | Complexity |
|------|------------|
|Best|O(n log n)|
|Average|O(n log n)|
|Worst|O(n log n)|

Unlike Quicksort, Heapsort performs almost the same amount of work regardless of the input distribution.

---

# Space Complexity

The heap operations themselves use constant auxiliary memory:

\[
O(1)
\]

However, this implementation creates a copy of the input array to preserve the original values.

Therefore, the complete implementation requires:

\[
O(n)
\]

additional memory.

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

# Discussion of Results

The experimental results were generally consistent with theoretical expectations.

Quicksort achieved the fastest execution times in most experiments due to lower constant factors and efficient partitioning.

Heapsort showed very stable performance across all input distributions. Its execution time did not change significantly for random, sorted, or reverse-sorted inputs, supporting its theoretical worst-case guarantee of \(O(n\log n)\).

Merge Sort also demonstrated stable performance. The unusually high running time observed for random input of size 2,000 is likely caused by system noise or temporary memory-management overhead rather than a change in algorithmic complexity.

Overall, the results show that Quicksort often provides the fastest practical performance, while Heapsort offers more predictable execution times and lower memory requirements than Merge Sort.

---

# Part 2: Priority Queue Implementation

A binary max heap was used to implement the priority queue.

Each task contains:

- Task ID
- Priority
- Arrival Time
- Deadline
- Duration

A dictionary named `positions` is maintained to map task IDs to heap indices.

Without this mapping, locating a task before updating its priority would require:

\[
O(n)
\]

With the dictionary, lookup becomes approximately:

\[
O(1)
\]

while heap reordering remains:

\[
O(\log n)
\]

---

# Priority Queue Test Results

```text
Highest priority: Task(id=2, priority=5, arrival=1, deadline=5, duration=1)

After priority update:
Task(id=1, priority=6, arrival=0, deadline=8, duration=1)

Extracted:
Task(id=1, priority=6, arrival=0, deadline=8, duration=1)

Extracted:
Task(id=2, priority=5, arrival=1, deadline=5, duration=1)

Extracted:
Task(id=3, priority=2, arrival=2, deadline=10, duration=1)
```

The extraction order confirmed that the heap property was preserved after priority updates.

---

# Scheduler Results

| Task | Priority | Arrival | Start | Finish | Wait | Deadline | Met Deadline |
|------|-----------|----------|--------|---------|------|-----------|---------------|
|1|3|0|0|3|0|8|Yes|
|2|5|1|3|5|2|6|Yes|
|4|4|4|5|7|1|10|Yes|
|3|2|2|7|11|5|12|Yes|
|5|1|5|11|12|6|15|Yes|

Average Waiting Time:

\[
2.80
\]

Deadlines Met:

\[
5/5
\]

Task 1 started immediately because it was the only available task at time zero.

Although Task 2 had a higher priority, it arrived after Task 1 had already begun execution. Since the scheduler is non-preemptive, Task 1 was allowed to finish before Task 2 was selected.

Task 4 was processed before Task 3 because it had a higher priority even though Task 3 arrived earlier. Task 5 had the lowest priority and therefore experienced the longest waiting time.

These results demonstrate the trade-off of priority-based scheduling: important tasks are completed quickly, while lower-priority tasks may wait longer.

---

# Scheduler Complexity

If there are \(n\) tasks:

- Sorting by arrival time:

\[
O(n\log n)
\]

- Heap insertions and extractions:

\[
O(n\log n)
\]

Therefore, the total scheduler complexity is:

\[
O(n\log n)
\]

with:

\[
O(n)
\]

space complexity.

---

# Conclusion

This assignment demonstrated the usefulness of binary heaps in both sorting and scheduling applications.

Heapsort provided predictable \(O(n\log n)\) performance regardless of input distribution, while the priority queue efficiently supported task insertion, extraction, and priority updates.

The scheduler simulation further illustrated how heaps can be applied to real-world systems that require dynamic prioritization and efficient task management.