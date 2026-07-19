from dataclasses import dataclass
from typing import List

from priority_queue import MaxPriorityQueue, Task


@dataclass
class SchedulingResult:
    task_id: int
    priority: int
    arrival_time: int
    start_time: int
    completion_time: int
    waiting_time: int
    deadline: int
    met_deadline: bool


def simulate_scheduler(tasks: List[Task]) -> List[SchedulingResult]:
    pending = sorted(
        tasks,
        key=lambda task: (task.arrival_time, task.task_id),
    )

    queue = MaxPriorityQueue()
    results = []

    current_time = 0
    next_task = 0

    while next_task < len(pending) or not queue.is_empty():
        if queue.is_empty() and next_task < len(pending):
            current_time = max(
                current_time,
                pending[next_task].arrival_time,
            )

        while (
            next_task < len(pending)
            and pending[next_task].arrival_time <= current_time
        ):
            queue.insert(pending[next_task])
            next_task += 1

        task = queue.extract_max()

        if task is None:
            continue

        start_time = current_time
        completion_time = start_time + task.duration
        waiting_time = start_time - task.arrival_time

        results.append(
            SchedulingResult(
                task_id=task.task_id,
                priority=task.priority,
                arrival_time=task.arrival_time,
                start_time=start_time,
                completion_time=completion_time,
                waiting_time=waiting_time,
                deadline=task.deadline,
                met_deadline=completion_time <= task.deadline,
            )
        )

        current_time = completion_time

    return results


def display_results(results: List[SchedulingResult]) -> None:
    print(
        f"{'Task':<8}"
        f"{'Priority':<10}"
        f"{'Arrival':<10}"
        f"{'Start':<8}"
        f"{'Finish':<8}"
        f"{'Wait':<8}"
        f"{'Deadline':<10}"
        f"{'Met Deadline'}"
    )

    for result in results:
        print(
            f"{result.task_id:<8}"
            f"{result.priority:<10}"
            f"{result.arrival_time:<10}"
            f"{result.start_time:<8}"
            f"{result.completion_time:<8}"
            f"{result.waiting_time:<8}"
            f"{result.deadline:<10}"
            f"{result.met_deadline}"
        )

    if not results:
        return

    average_waiting_time = sum(
        result.waiting_time for result in results
    ) / len(results)

    deadlines_met = sum(
        result.met_deadline for result in results
    )

    print(f"\nAverage waiting time: {average_waiting_time:.2f}")
    print(
        f"Deadlines met: {deadlines_met}/{len(results)}"
    )


def main() -> None:
    tasks = [
        Task(1, priority=3, arrival_time=0, deadline=8, duration=3),
        Task(2, priority=5, arrival_time=1, deadline=6, duration=2),
        Task(3, priority=2, arrival_time=2, deadline=12, duration=4),
        Task(4, priority=4, arrival_time=4, deadline=10, duration=2),
        Task(5, priority=1, arrival_time=5, deadline=15, duration=1),
    ]

    results = simulate_scheduler(tasks)
    display_results(results)


if __name__ == "__main__":
    main()