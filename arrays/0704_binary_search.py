from typing import List
import math


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Performs binary search on a sorted list to find the index of the target value.

        If the target exists in the list, its index is returned.
        Otherwise, the function returns -1.

        :param nums: Sorted list of integers
        :param target: Integer value to search for
        :return: Index of target if found, otherwise -1
        """

        # Left and right pointers defining the search range
        l = 0
        r = len(nums) - 1

        # Continue searching while the range is valid
        while l <= r:
            # Calculate the middle index (rounded up)
            mid = math.ceil((l + r) / 2)

            # If the middle element matches the target, return its index
            if nums[mid] == target:
                return mid

            # If the middle element is greater than target,
            # search in the left half
            elif nums[mid] > target:
                r = mid - 1

            # Otherwise, search in the right half
            else:
                l = mid + 1

        # Target was not found
        return -1

        # ---------------------------------------------------------
        # Time Complexity:
        # O(log n) — The search space is halved each iteration.
        #
        # Space Complexity:
        # O(1) — Only constant extra space is used.
        # ---------------------------------------------------------
