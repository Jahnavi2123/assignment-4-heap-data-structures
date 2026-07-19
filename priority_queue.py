from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class Task:
    task_id: int
    priority: int
    arrival_time: int
    deadline: int
    duration: int = 1

    def __str__(self) -> str:
        return (
            f"Task(id={self.task_id}, priority={self.priority}, "
            f"arrival={self.arrival_time}, deadline={self.deadline}, "
            f"duration={self.duration})"
        )


class MaxPriorityQueue:
    def __init__(self) -> None:
        self.heap: List[Task] = []

        # Maps task IDs to their positions for efficient priority updates.
        self.positions: Dict[int, int] = {}

    def is_empty(self) -> bool:
        return len(self.heap) == 0

    def __len__(self) -> int:
        return len(self.heap)

    @staticmethod
    def _higher_priority(first: Task, second: Task) -> bool:
        if first.priority != second.priority:
            return first.priority > second.priority

        if first.arrival_time != second.arrival_time:
            return first.arrival_time < second.arrival_time

        return first.task_id < second.task_id

    def _swap(self, first: int, second: int) -> None:
        self.heap[first], self.heap[second] = (
            self.heap[second],
            self.heap[first],
        )

        self.positions[self.heap[first].task_id] = first
        self.positions[self.heap[second].task_id] = second

    def _sift_up(self, index: int) -> None:
        while index > 0:
            parent = (index - 1) // 2

            if not self._higher_priority(
                self.heap[index],
                self.heap[parent],
            ):
                break

            self._swap(index, parent)
            index = parent

    def _sift_down(self, index: int) -> None:
        size = len(self.heap)

        while True:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if (
                left < size
                and self._higher_priority(
                    self.heap[left],
                    self.heap[largest],
                )
            ):
                largest = left

            if (
                right < size
                and self._higher_priority(
                    self.heap[right],
                    self.heap[largest],
                )
            ):
                largest = right

            if largest == index:
                return

            self._swap(index, largest)
            index = largest

    def insert(self, task: Task) -> None:
        if task.task_id in self.positions:
            raise ValueError(
                f"Task ID {task.task_id} already exists."
            )

        self.heap.append(task)
        index = len(self.heap) - 1
        self.positions[task.task_id] = index

        self._sift_up(index)

    def peek_max(self) -> Optional[Task]:
        if self.is_empty():
            return None

        return self.heap[0]

    def extract_max(self) -> Optional[Task]:
        if self.is_empty():
            return None

        maximum = self.heap[0]
        last_task = self.heap.pop()

        del self.positions[maximum.task_id]

        if self.heap:
            self.heap[0] = last_task
            self.positions[last_task.task_id] = 0
            self._sift_down(0)

        return maximum

    def change_priority(
        self,
        task_id: int,
        new_priority: int,
    ) -> None:
        if task_id not in self.positions:
            raise KeyError(f"Task ID {task_id} was not found.")

        index = self.positions[task_id]
        old_priority = self.heap[index].priority
        self.heap[index].priority = new_priority

        if new_priority > old_priority:
            self._sift_up(index)
        elif new_priority < old_priority:
            self._sift_down(index)

    def increase_key(
        self,
        task_id: int,
        new_priority: int,
    ) -> None:
        index = self.positions.get(task_id)

        if index is None:
            raise KeyError(f"Task ID {task_id} was not found.")

        if new_priority < self.heap[index].priority:
            raise ValueError(
                "The new priority must be greater than or equal "
                "to the current priority."
            )

        self.change_priority(task_id, new_priority)

    def decrease_key(
        self,
        task_id: int,
        new_priority: int,
    ) -> None:
        index = self.positions.get(task_id)

        if index is None:
            raise KeyError(f"Task ID {task_id} was not found.")

        if new_priority > self.heap[index].priority:
            raise ValueError(
                "The new priority must be less than or equal "
                "to the current priority."
            )

        self.change_priority(task_id, new_priority)


if __name__ == "__main__":
    queue = MaxPriorityQueue()

    queue.insert(Task(1, 3, 0, 8))
    queue.insert(Task(2, 5, 1, 5))
    queue.insert(Task(3, 2, 2, 10))

    print("Highest priority:", queue.peek_max())

    queue.increase_key(1, 6)
    print("After priority update:", queue.peek_max())

    while not queue.is_empty():
        print("Extracted:", queue.extract_max())