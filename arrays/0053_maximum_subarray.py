from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Finds the contiguous subarray within a list of integers that has
        the largest sum and returns that sum.

        This implementation uses Kadane's Algorithm, which efficiently
        computes the maximum subarray sum in a single pass.

        :param nums: List of integers (can include negative numbers)
        :return: The maximum possible sum of a contiguous subarray
        """

        # Initialize both the maximum sum and the current running sum
        # to the first element of the array
        max_sum = nums[0]
        current_sum = nums[0]

        # Iterate through the remaining elements in the list
        for num in nums[1:]:
            # Decide whether to start a new subarray at the current number
            # or extend the existing subarray
            current_sum = max(num, current_sum + num)

            # Update the maximum sum found so far if needed
            max_sum = max(max_sum, current_sum)

        # Return the maximum subarray sum
        return max_sum

        # ---------------------------------------------------------
        # Time Complexity:
        # O(n) — Each element is processed once.
        #
        # Space Complexity:
        # O(1) — Only constant extra space is used.
        # ---------------------------------------------------------
