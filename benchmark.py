import random
import statistics
import time
from typing import Callable, Dict, List

from heapsort import heapsort
from merge_sort import merge_sort
from quicksort import quicksort


SortingFunction = Callable[[List[int]], List[int]]


def measure_time(
    algorithm: SortingFunction,
    values: List[int],
    trials: int = 5,
) -> float:
    times = []
    expected = sorted(values)

    for _ in range(trials):
        start = time.perf_counter()
        result = algorithm(values)
        elapsed = time.perf_counter() - start

        if result != expected:
            raise ValueError(
                f"{algorithm.__name__} returned an incorrect result."
            )

        times.append(elapsed)

    return statistics.median(times)


def generate_datasets(size: int) -> Dict[str, List[int]]:
    return {
        "Random": [
            random.randint(0, size * 10)
            for _ in range(size)
        ],
        "Sorted": list(range(size)),
        "Reverse": list(range(size, 0, -1)),
    }


def main() -> None:
    random.seed(42)

    algorithms = {
        "Heapsort": heapsort,
        "Quicksort": quicksort,
        "Merge Sort": merge_sort,
    }

    sizes = [100, 500, 1000, 2000, 5000]

    print(
        f"{'Size':<8}"
        f"{'Distribution':<15}"
        f"{'Heapsort':<15}"
        f"{'Quicksort':<15}"
        f"{'Merge Sort':<15}"
    )

    for size in sizes:
        datasets = generate_datasets(size)

        for distribution, values in datasets.items():
            results = {
                name: measure_time(algorithm, values)
                for name, algorithm in algorithms.items()
            }

            print(
                f"{size:<8}"
                f"{distribution:<15}"
                f"{results['Heapsort']:<15.6f}"
                f"{results['Quicksort']:<15.6f}"
                f"{results['Merge Sort']:<15.6f}"
            )


if __name__ == "__main__":
    main()