import random
from typing import List


def quicksort(values: List[int]) -> List[int]:
    """Return a sorted copy using randomized three-way Quicksort."""
    result = values.copy()

    if len(result) > 1:
        _quicksort(result, 0, len(result) - 1)

    return result


def _quicksort(values: List[int], low: int, high: int) -> None:
    while low < high:
        pivot = values[random.randint(low, high)]

        less = low
        current = low
        greater = high

        while current <= greater:
            if values[current] < pivot:
                values[less], values[current] = (
                    values[current],
                    values[less],
                )
                less += 1
                current += 1

            elif values[current] > pivot:
                values[current], values[greater] = (
                    values[greater],
                    values[current],
                )
                greater -= 1

            else:
                current += 1

        # Process the smaller side recursively to limit stack usage.
        if less - low < high - greater:
            _quicksort(values, low, less - 1)
            low = greater + 1
        else:
            _quicksort(values, greater + 1, high)
            high = less - 1