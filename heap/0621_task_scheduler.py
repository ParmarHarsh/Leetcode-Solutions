from typing import List


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        """
        Calculates the minimum number of days required to complete all tasks
        with a cooldown period (`space`) between identical tasks.

        This implementation tracks the last day each task was executed
        and ensures that at least `space` days pass before executing
        the same task again.

        :param tasks: List of task identifiers
        :param space: Cooldown period between same tasks
        :return: Minimum number of days required
        """

        # Current day counter (represents total intervals)
        intervalCount = 0

        # Dictionary to store the last execution day of each task
        last_seen = {}

        # Iterate through each task in order
        for task in tasks:

            # If the task has been seen before and cooldown is not satisfied
            if task in last_seen and intervalCount - last_seen[task] <= space:
                # Fast forward the current day to the earliest valid day
                intervalCount = last_seen[task] + space + 1
            else:
                # Otherwise, move to the next day
                intervalCount += 1

            # Update the last seen day for the current task
            last_seen[task] = intervalCount

        # Return total intervals (days) required
        return intervalCount

        # ---------------------------------------------------------
        # Time Complexity:
        # O(n) — Each task is processed once.
        #
        # Space Complexity:
        # O(n) — Stores last execution time for each unique task.
        # ---------------------------------------------------------