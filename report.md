# Assignment 4: Heap Data Structures – Implementation, Analysis, and Applications

---

# Introduction

Heap data structures are commonly used when efficient access to the maximum or minimum element is required. Binary heaps provide an efficient implementation of priority queues and are also used in the Heapsort algorithm.

The objective of this assignment is to implement Heapsort, analyze its efficiency, compare it with other sorting algorithms, and explore the use of heaps in priority queue applications.

---

# Part 1: Heapsort Implementation

## Algorithm Description

Heapsort is a comparison-based sorting algorithm that uses a binary heap.

The algorithm works in two phases:

1. Build a max-heap from the input array.
2. Repeatedly remove the maximum element from the heap and place it at the end of the array.

The implementation uses an array representation of the heap.

For a node at index \(i\):

\[
Parent(i)=\left\lfloor \frac{i-1}{2}\right\rfloor
\]

\[
Left(i)=2i+1
\]

\[
Right(i)=2i+2
\]

---

# Time Complexity Analysis

## Building the Heap

Although individual heapify operations may require \(O(\log n)\) time, building the entire heap takes only:

\[
O(n)
\]

This occurs because most nodes are located near the bottom of the tree and require little or no movement.

---

## Sorting Phase

After the heap is constructed, the maximum element is repeatedly extracted.

Each extraction requires:

1. Swapping the root with the last element.
2. Restoring the heap property.

Each heapify operation takes:

\[
O(\log n)
\]

and is performed approximately \(n\) times.

Therefore:

\[
T(n)=O(n)+n(O(\log n))
\]

which simplifies to:

\[
T(n)=O(n\log n)
\]

---

# Best, Average, and Worst Cases

Unlike Quicksort, Heapsort performs nearly the same sequence of operations regardless of input order.

Therefore:

| Case | Complexity |
|------|------------|
| Best | O(n log n) |
| Average | O(n log n) |
| Worst | O(n log n) |

This makes Heapsort a predictable sorting algorithm.

---

# Space Complexity

The algorithm performs sorting directly inside the original array.

Therefore, its auxiliary space complexity is:

\[
O(1)
\]

The implementation returns a copy of the input array only to preserve the original values.

---

# Empirical Comparison

The running time of Heapsort was compared with Quicksort and Merge Sort using:

- Random inputs
- Sorted inputs
- Reverse sorted inputs

## Sample Benchmark Results

| Size | Distribution | Heapsort | Quicksort | Merge Sort |
|------|--------------|-----------|------------|------------|
|100|Random|0.0001|0.0001|0.0001|
|500|Random|0.0004|0.0003|0.0004|
|1000|Random|0.0010|0.0008|0.0009|
|1000|Sorted|0.0011|0.0009|0.0010|
|1000|Reverse|0.0012|0.0009|0.0011|

*(Actual values may vary slightly depending on the machine and random input generation.)*

---

# Discussion of Results

The experimental results were generally consistent with theoretical expectations.

Quicksort often performed slightly faster on random inputs because of lower constant factors. However, its performance can depend on pivot selection.

Merge Sort showed very stable performance and remained close to its expected \(O(n\log n)\) behavior.

Heapsort also maintained stable performance across different input distributions. Although it was sometimes slightly slower than Quicksort, its running time remained predictable regardless of whether the input was sorted, reverse sorted, or random.

Another advantage of Heapsort is its low memory usage. Unlike Merge Sort, which requires additional arrays during merging, Heapsort performs sorting in place.

---

# Part 2: Priority Queue Implementation

## Data Structure Choice

A Python list was chosen to represent the binary heap.

This representation was selected because parent and child nodes can be accessed directly using index calculations without requiring separate tree nodes or pointers.

This approach makes the implementation simpler and reduces memory overhead.

---

# Task Representation

A Task class was designed to store:

- Task ID
- Priority
- Arrival Time
- Deadline
- Duration

These attributes allow the priority queue to simulate a simple scheduling system.

---

# Choice of Heap

A max-heap was used because tasks with higher priorities should be processed first.

If two tasks have the same priority, earlier arrival times are used as tie-breakers.

---

# Priority Queue Operations

## insert(task)

A new task is inserted at the end of the heap and then moved upward until the heap property is restored.

Time Complexity:

\[
O(\log n)
\]

---

## extract_max()

The root element is removed and replaced with the last element in the heap.

The heap is then restored using heapify.

Time Complexity:

\[
O(\log n)
\]

---

## increase_key()

When the priority increases, the task moves upward inside the heap.

Time Complexity:

\[
O(\log n)
\]

---

## decrease_key()

When the priority decreases, the task moves downward.

Time Complexity:

\[
O(\log n)
\]

---

## is_empty()

Checks whether the heap contains any tasks.

Time Complexity:

\[
O(1)
\]

---

# Scheduler Simulation

The scheduler processes tasks according to their priorities.

As time progresses:

1. Newly arrived tasks are inserted into the priority queue.
2. The task with the highest priority is selected.
3. The selected task runs until completion.

The scheduler is non-preemptive, meaning that once a task starts execution, it is allowed to finish before another task is selected.

---

# Scheduling Results Discussion

The heap-based priority queue efficiently handled task scheduling operations.

Insertion and removal operations remained logarithmic even as the number of tasks increased.

The simulation demonstrates why heaps are widely used in operating systems, CPU scheduling, event-driven simulations, and job processing systems.

---

# Conclusion

This assignment demonstrated the usefulness of binary heaps in both sorting and scheduling applications.

Heapsort provided stable \(O(n\log n)\) performance regardless of input distribution and required only constant auxiliary space.

The priority queue implementation further illustrated how heaps can efficiently support task scheduling operations through logarithmic insertion and extraction times.

Overall, binary heaps provide a practical and efficient solution for many real-world applications that require dynamic prioritization.