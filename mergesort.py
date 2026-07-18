from typing import List


def merge_sort(values: List[int]) -> List[int]:
    """Return a sorted copy using Merge Sort."""
    if len(values) <= 1:
        return values.copy()

    midpoint = len(values) // 2

    left = merge_sort(values[:midpoint])
    right = merge_sort(values[midpoint:])

    return _merge(left, right)


def _merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result