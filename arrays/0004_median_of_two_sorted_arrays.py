from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Finds the median of two sorted arrays by merging them
        into a single sorted array and then computing the median.

        :param nums1: First sorted list of integers
        :param nums2: Second sorted list of integers
        :return: Median value of the combined sorted array
        """

        # Append all elements from nums2 into nums1
        for num in nums2:
            nums1.append(num)

        # Sort the combined list
        nums1.sort()

        # Handle edge cases
        if nums1 == []:
            return None
        elif nums1[0] == 0 and len(nums1) == 1:
            return 0

        # Initialize pointers to help locate the median index
        i = 0
        j = 0

        # Move through the array:
        # i moves in steps of 2, j tracks the middle position
        while i < len(nums1):
            j += 1
            i += 2

        # If more than one element exists, compute median accordingly
        if len(nums1) > 1:
            if len(nums1) % 2 == 0:
                # Even length: average of two middle elements
                return (nums1[j - 1] + nums1[j]) / 2
            else:
                # Odd length: return middle element
                return nums1[j - 1]

        # If only one element exists, return it
        return nums1[0]

        # ---------------------------------------------------------
        # Time Complexity:
        # O((m + n) log(m + n)) — Merging and sorting the arrays.
        #
        # Space Complexity:
        # O(1) additional space (in-place modification of nums1),
        # though effectively O(m + n) due to merged data.
        # ---------------------------------------------------------