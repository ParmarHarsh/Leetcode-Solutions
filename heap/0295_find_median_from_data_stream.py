import heapq


class MedianFinder:
    """
    Data structure to efficiently find the median of a stream of numbers.

    Uses two heaps:
    - small: Max heap (implemented as a min heap with negative values)
             stores the smaller half of numbers
    - large: Min heap
             stores the larger half of numbers
    """

    def __init__(self):
        """
        Initializes two heaps:
        - small (max heap using negatives)
        - large (min heap)
        """
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        """
        Adds a number into the data structure.

        Steps:
        1. Push number into max heap (small).
        2. Ensure ordering: all elements in small <= elements in large.
        3. Balance the heaps so their sizes differ by at most 1.

        :param num: Number to add
        """

        # Push into max heap (store negative to simulate max heap)
        heapq.heappush(self.small, -1 * num)

        # Ensure the largest element in small is not greater than
        # the smallest element in large
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Balance heaps if small has more than one extra element
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Balance heaps if large has more than one extra element
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        """
        Returns the median of all inserted numbers.

        - If one heap has more elements, the median is its top.
        - If both heaps have equal size, the median is the average of both tops.

        :return: Median value
        """

        # If small heap has more elements, return its top
        if len(self.small) > len(self.large):
            return -1 * self.small[0]

        # If large heap has more elements, return its top
        if len(self.large) > len(self.small):
            return self.large[0]

        # If both heaps are equal in size, return average of tops
        return (-1 * self.small[0] + self.large[0]) / 2

    # ---------------------------------------------------------
    # Time Complexity:
    # addNum: O(log n) — Heap insertion and balancing operations.
    # findMedian: O(1) — Direct access to heap tops.
    #
    # Space Complexity:
    # O(n) — Stores all inserted numbers across both heaps.
    # ---------------------------------------------------------


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()