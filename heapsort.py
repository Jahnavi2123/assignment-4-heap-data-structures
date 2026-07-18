from typing import List


def heapify(values: List[int], heap_size: int, root: int) -> None:
    """Restore the max-heap property for the subtree rooted at root."""
    while True:
        largest = root
        left = 2 * root + 1
        right = 2 * root + 2

        if left < heap_size and values[left] > values[largest]:
            largest = left

        if right < heap_size and values[right] > values[largest]:
            largest = right

        if largest == root:
            return

        values[root], values[largest] = values[largest], values[root]
        root = largest


def heapsort(values: List[int]) -> List[int]:
    """Return a sorted copy of values using Heapsort."""
    result = values.copy()
    size = len(result)

    # Build the max-heap in O(n).
    for index in range(size // 2 - 1, -1, -1):
        heapify(result, size, index)

    # Repeatedly move the maximum element to the end.
    for end in range(size - 1, 0, -1):
        result[0], result[end] = result[end], result[0]
        heapify(result, end, 0)

    return result


if __name__ == "__main__":
    test_cases = [
        [],
        [7],
        [4, 10, 3, 5, 1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [4, 2, 4, 1, 2],
    ]

    for values in test_cases:
        print(f"Input:  {values}")
        print(f"Output: {heapsort(values)}")
        print()