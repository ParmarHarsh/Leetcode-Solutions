from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Determines the number of car fleets that will arrive at the target.

        Cars are sorted by starting position in descending order.
        We compute the time each car takes to reach the target.
        If a car takes longer than the maximum time seen so far,
        it forms a new fleet; otherwise, it joins an existing fleet.

        :param target: The destination position
        :param position: List of starting positions of cars
        :param speed: List of speeds corresponding to each car
        :return: Number of car fleets that reach the target
        """

        # Pair each car's position with its speed
        cars = list(zip(position, speed))

        # Sort cars by position in descending order
        # (process cars closest to the target first)
        cars.sort(reverse=True)

        # Counter for the number of fleets
        fleets = 0

        # Tracks the maximum time taken by any fleet so far
        max_time = 0

        # Iterate through the sorted cars
        for pos, spd in cars:
            # Time required for the current car to reach the target
            time = (target - pos) / spd

            # If this car takes longer than the current maximum time,
            # it forms a new fleet
            if time > max_time:
                fleets += 1
                max_time = time

        # Return the total number of fleets
        return fleets

        # ---------------------------------------------------------
        # Time Complexity:
        # O(n log n) — Sorting the cars dominates the runtime.
        #
        # Space Complexity:
        # O(n) — Additional space is used to store the paired list.
        # ---------------------------------------------------------
