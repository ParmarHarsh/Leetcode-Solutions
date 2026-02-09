from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Finds the k most frequent elements in the input list.

        The function first counts the frequency of each number, then uses
        a min-heap to keep track of the top k most frequent elements.

        :param nums: List of integers
        :param k: Number of most frequent elements to return
        :return: List containing the k most frequent elements
        """

        # Dictionary to store the frequency of each number
        count = {}

        # Count the occurrences of each number
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Min-heap to store (frequency, number) pairs
        heap = []

        # Push all frequency-number pairs into the heap
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))

        # Remove elements until the heap size is k
        while len(heap) > k:
            heapq.heappop(heap)

        # List to store the final result
        res = []

        # Extract the k most frequent elements from the heap
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        # Return the result list
        return res

        # ---------------------------------------------------------
        # Time Complexity:
        # O(n log n) — Counting frequencies takes O(n), and heap
        #              operations take O(log n) per insertion/removal.
        #
        # Space Complexity:
        # O(n) — Extra space is used for the frequency map and heap.
        # ---------------------------------------------------------
