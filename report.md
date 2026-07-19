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

## Benchmark Results

The algorithms were tested using random, sorted, and reverse-sorted inputs. Each result represents the median running time across multiple trials.

| Size | Distribution | Heapsort (sec) | Quicksort (sec) | Merge Sort (sec) |
|---:|---|---:|---:|---:|
| 100 | Random | 0.000033 | 0.000032 | 0.000042 |
| 100 | Sorted | 0.000033 | 0.000028 | 0.000032 |
| 100 | Reverse | 0.000030 | 0.000037 | 0.000034 |
| 500 | Random | 0.000236 | 0.000202 | 0.000241 |
| 500 | Sorted | 0.000220 | 0.000200 | 0.000171 |
| 500 | Reverse | 0.000212 | 0.000190 | 0.000174 |
| 1000 | Random | 0.000505 | 0.000443 | 0.000567 |
| 1000 | Sorted | 0.000521 | 0.000412 | 0.000369 |
| 1000 | Reverse | 0.000447 | 0.000407 | 0.000381 |
| 2000 | Random | 0.001157 | 0.000962 | 0.003588 |
| 2000 | Sorted | 0.001364 | 0.000926 | 0.000799 |
| 2000 | Reverse | 0.001052 | 0.000922 | 0.000800 |
| 5000 | Random | 0.003355 | 0.002718 | 0.003182 |
| 5000 | Sorted | 0.003315 | 0.002416 | 0.002039 |
| 5000 | Reverse | 0.003005 | 0.002472 | 0.002168 |

---

## Discussion of Sorting Results

The benchmark results were generally consistent with the expected time complexities. All three algorithms handled the tested input sizes efficiently, and their running times increased gradually as the input size increased.

Quicksort was the fastest algorithm in most of the tests. The implementation uses random pivot selection and three-way partitioning, which reduces the chance of creating poor partitions on sorted or reverse-sorted inputs. Because of this, Quicksort remained stable across all three input distributions.

Heapsort also showed consistent performance. Its running time did not change significantly based on whether the input was random, sorted, or reverse sorted. This supports the theoretical analysis that Heapsort runs in \(O(n \log n)\) in the best, average, and worst cases. It was slightly slower than Quicksort in most tests because heap construction and repeated heapify operations involve additional comparisons and swaps.

Merge Sort performed well for sorted and reverse-sorted inputs. For random input of size 2,000, its measured time was noticeably higher than the surrounding results. This appears to be a timing variation rather than a change in the algorithm's complexity, since its performance returned to the expected range at size 5,000. Runtime measurements can be affected by Python interpreter activity, memory allocation, and background system processes.

The results also show that the fastest algorithm can depend on both the implementation and the input. Quicksort had the lowest running time in most cases, Merge Sort performed especially well on ordered inputs, and Heapsort provided the most predictable performance across input distributions.

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

## Priority Queue Test Results

The priority queue was tested using three tasks with different priorities and arrival times.

```text
Highest priority: Task(id=2, priority=5, arrival=1, deadline=5, duration=1)
After priority update: Task(id=1, priority=6, arrival=0, deadline=8, duration=1)
Extracted: Task(id=1, priority=6, arrival=0, deadline=8, duration=1)
Extracted: Task(id=2, priority=5, arrival=1, deadline=5, duration=1)
Extracted: Task(id=3, priority=2, arrival=2, deadline=10, duration=1)


## Add this scheduler results section

```markdown
## Scheduler Results

| Task | Priority | Arrival | Start | Finish | Waiting Time | Deadline | Met Deadline |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 3 | 0 | 0 | 3 | 0 | 8 | Yes |
| 2 | 5 | 1 | 3 | 5 | 2 | 6 | Yes |
| 4 | 4 | 4 | 5 | 7 | 1 | 10 | Yes |
| 3 | 2 | 2 | 7 | 11 | 5 | 12 | Yes |
| 5 | 1 | 5 | 11 | 12 | 6 | 15 | Yes |

The average waiting time was 2.80 time units, and all five tasks completed before their deadlines.

The scheduler selected the highest-priority task among the tasks that had already arrived. Task 1 started first because it was the only available task at time 0. Task 2 had a higher priority, but it arrived after Task 1 had already started. Since the scheduler is non-preemptive, Task 1 was allowed to finish before Task 2 was selected.

Task 4 was processed before Task 3 because it had a higher priority, even though Task 3 arrived earlier. Task 5 had the lowest priority and therefore experienced the longest waiting time. These results show that priority-based scheduling can improve the response time of important tasks, but lower-priority tasks may wait longer.

---

# Conclusion

This assignment demonstrated the usefulness of binary heaps in both sorting and scheduling applications.

Heapsort provided stable \(O(n\log n)\) performance regardless of input distribution and required only constant auxiliary space.

The priority queue implementation further illustrated how heaps can efficiently support task scheduling operations through logarithmic insertion and extraction times.

Overall, binary heaps provide a practical and efficient solution for many real-world applications that require dynamic prioritization.