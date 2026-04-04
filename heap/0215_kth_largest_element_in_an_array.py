from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Finds the k-th largest element in an unsorted list.

        This implementation uses a heap-based approach by leveraging
        heapq.nlargest, which returns the k largest elements in descending order.

        The k-th largest element is then the last element in that list.

        :param nums: List of integers
        :param k: The position (1-based) of the largest element to find
        :return: The k-th largest element
        """

        # Get the k largest elements from the list
        # The result is sorted in descending order
        largest_k = heapq.nlargest(k, nums)

        # Return the k-th largest element (last element in the list)
        return largest_k[-1]

        # ---------------------------------------------------------
        # Time Complexity:
        # O(n log k) — heapq.nlargest processes n elements with a heap of size k.
        #
        # Space Complexity:
        # O(k) — Stores k largest elements in the heap.
        # ---------------------------------------------------------