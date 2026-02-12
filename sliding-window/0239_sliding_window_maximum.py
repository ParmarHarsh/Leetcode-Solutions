from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Finds the maximum value in each sliding window of size k
        as it moves from left to right across the array.

        This implementation uses a monotonic deque to keep track
        of indices of useful elements in decreasing order.

        :param nums: List of integers
        :param k: Size of the sliding window
        :return: List of maximum values for each window
        """

        # Deque to store indices of elements in decreasing order of values
        q = deque()

        # List to store the maximum values of each sliding window
        result = []

        # Iterate through the array with index and value
        for i, curr in enumerate(nums):
            # Remove indices whose corresponding values are
            # less than or equal to the current value
            while q and nums[q[-1]] <= curr:
                q.pop()

            # Add the current index to the deque
            q.append(i)

            # Remove the index that is out of the current window
            if q[0] == i - k:
                q.popleft()

            # Once the first window is fully formed,
            # append the maximum (front of deque) to the result
            if i >= k - 1:
                result.append(nums[q[0]])

        # Return the list of sliding window maximums
        return result

        # ---------------------------------------------------------
        # Time Complexity:
        # O(n) — Each element is added to and removed from the deque
        #        at most once.
        #
        # Space Complexity:
        # O(k) — The deque stores at most k indices.
        # ---------------------------------------------------------
