# Assignment 4: Heap Data Structures – Implementation, Analysis, and Applications

---

# Repository Contents

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

- Python 3.8 or higher
- No external libraries are required.

---

# Running the Programs

## Run Heapsort

```bash
python3 heapsort.py
```

---

## Run Quicksort

```bash
python3 quicksort.py
```

---

## Run Merge Sort

```bash
python3 merge_sort.py
```

---

## Run Sorting Benchmarks

```bash
python3 benchmark.py
```

This compares:

- Heapsort
- Quicksort
- Merge Sort

using:

- Random inputs
- Sorted inputs
- Reverse sorted inputs

---

## Run Priority Queue Example

```bash
python3 priority_queue.py
```

---

## Run Scheduler Simulation

```bash
python3 scheduler.py
```

---

# Summary of Findings

1. Heapsort maintained stable performance across all input distributions.

2. Quicksort generally performed very well on random data but its performance depended on pivot selection.

3. Merge Sort also showed stable performance and produced running times close to Heapsort.

4. Heapsort required less auxiliary memory than Merge Sort because it performs sorting in place.

5. Binary heaps provide an efficient implementation of priority queues, supporting insertion and deletion operations in logarithmic time.

---

# Complexity Summary

## Heapsort

| Case | Complexity |
|------|------------|
| Best Case | O(n log n) |
| Average Case | O(n log n) |
| Worst Case | O(n log n) |

Space Complexity:

```text
O(1)
```

---

## Priority Queue Operations

| Operation | Complexity |
|-----------|------------|
| insert() | O(log n) |
| extract_max() | O(log n) |
| increase_key() | O(log n) |
| decrease_key() | O(log n) |
| peek_max() | O(1) |
| is_empty() | O(1) |

