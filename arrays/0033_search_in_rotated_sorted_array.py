from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Searches for a target value in a rotated sorted array using binary search.

        The array was originally sorted in ascending order but then rotated
        at some unknown pivot. This function determines which half of the
        array is properly sorted during each iteration and narrows the
        search space accordingly.

        :param nums: Rotated sorted list of integers
        :param target: Integer value to search for
        :return: Index of target if found, otherwise -1
        """

        # Initialize left and right pointers
        i = 0
        j = len(nums) - 1

        # Perform binary search while the search range is valid
        while i <= j:

            # Calculate middle index
            mid = (i + j) // 2

            # If the middle element is the target, return its index
            if target == nums[mid]:
                return mid

            # Check if the left half [i ... mid] is sorted
            if nums[i] <= nums[mid]:

                # If target is not within the sorted left half,
                # search in the right half
                if target > nums[mid] or target < nums[i]:
                    i = mid + 1
                else:
                    j = mid - 1

            # Otherwise, the right half [mid ... j] must be sorted
            else:

                # If target is not within the sorted right half,
                # search in the left half
                if target < nums[mid] or target > nums[j]:
                    j = mid - 1
                else:
                    i = mid + 1

        # Target was not found in the array
        return -1

        # ---------------------------------------------------------
        # Time Complexity:
        # O(log n) — The search space is reduced by half each iteration.
        #
        # Space Complexity:
        # O(1) — Only constant extra space is used.
        # ---------------------------------------------------------
