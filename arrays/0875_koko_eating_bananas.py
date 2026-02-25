from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Determines the minimum integer eating speed (k) such that
        all banana piles can be eaten within h hours.

        Uses binary search on the possible range of eating speeds.

        :param piles: List of integers representing banana piles
        :param h: Total number of hours available
        :return: Minimum integer eating speed required
        """

        # Minimum possible eating speed
        left = 1

        # Maximum possible eating speed (eat the largest pile in 1 hour)
        right = max(piles)

        # Store the smallest valid eating speed found
        output = right

        # Binary search on eating speed range
        while left <= right:

            # Try the middle eating speed
            k = (left + right) // 2

            # Calculate total hours needed at speed k
            hours = 0
            for p in piles:
                # Use ceiling to account for partial hours
                hours = hours + math.ceil(p / k)

            # If total hours are within limit, try smaller speed
            if hours <= h:
                output = min(output, k)
                right = k - 1
            else:
                # Otherwise, increase eating speed
                left = k + 1

        # Return the minimum valid eating speed
        return output

        # ---------------------------------------------------------
        # Time Complexity:
        # O(n log m) — Binary search over eating speeds (m = max pile),
        # and for each speed we iterate through all piles.
        #
        # Space Complexity:
        # O(1) — Only constant extra space is used.
        # ---------------------------------------------------------
