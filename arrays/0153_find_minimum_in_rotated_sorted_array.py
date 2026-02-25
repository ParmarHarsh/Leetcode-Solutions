from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Finds the minimum element in a rotated sorted array.

        The array was originally sorted in ascending order and then rotated.
        This function uses a modified binary search to efficiently locate
        the smallest element.

        :param nums: Rotated sorted list of integers
        :return: Minimum element in the array
        """

        # Initialize left and right pointers
        i = 0
        j = len(nums) - 1

        # Initialize result with the first element
        # This will store the smallest value found so far
        res = nums[0]

        # Perform binary search while the search range is valid
        while i <= j:

            # If the current subarray is already sorted,
            # then nums[i] is the minimum in this range
            if nums[i] < nums[j]:
                res = min(res, nums[i])
                break

            # Calculate middle index
            mid = (i + j) // 2

            # Update result with the smaller value between
            # current result and middle element
            res = min(nums[mid], res)

            # If left half is sorted, move to the right half
            if nums[mid] >= nums[i]:
                i = mid + 1
            else:
                # Otherwise, move to the left half
                j = mid - 1

        # Return the smallest value found
        return res

        # ---------------------------------------------------------
        # Time Complexity:
        # O(log n) — Binary search reduces the search space by half each iteration.
        #
        # Space Complexity:
        # O(1) — Only constant extra space is used.
        # ---------------------------------------------------------
