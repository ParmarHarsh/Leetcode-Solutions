from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        Finds a peak element in the array and returns its index.

        A peak element is an element that is strictly greater than its neighbors.
        This function uses a binary search approach to efficiently locate a peak.

        :param nums: List of integers
        :return: Index of a peak element
        """

        # Initialize left and right pointers
        l, h = 0, len(nums) - 1

        # Perform binary search while the search space is valid
        while l < h:

            # Calculate middle index
            mid = (l + h) // 2

            # Compare mid element with its right neighbor
            if nums[mid] < nums[mid + 1]:
                # If the right neighbor is greater, a peak must exist on the right side
                l = mid + 1
            else:
                # Otherwise, a peak exists on the left side (including mid)
                h = mid

        # When l == h, it points to a peak element
        return l

        # ---------------------------------------------------------
        # Time Complexity:
        # O(log n) — The search space is halved each iteration.
        #
        # Space Complexity:
        # O(1) — Only constant extra space is used.
        # ---------------------------------------------------------