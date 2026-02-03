from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds and returns the indices of two numbers in the list `nums`
        such that their sum is equal to `target`.

        The function assumes that exactly one valid solution exists
        and that the same element cannot be used twice.

        :param nums: List of integers to search through
        :param target: The target sum to achieve
        :return: A list containing the indices of the two numbers
        """

        # Initialize an empty list to store the result
        # (Declared but not used since the function returns immediately
        #  once a valid pair is found)
        result = []

        # Hash map to store numbers as keys and their indices as values
        # This allows O(1) average-time lookups for complements
        hash_map = {}

        # Iterate over the list while keeping track of both index and value
        for i, num in enumerate(nums):
            # Calculate and check if the complement needed to reach `target`
            # has already been seen
            if (target - num) not in hash_map:
                # If not found, store the current number and its index
                # for future complement checks
                hash_map[num] = i
            else:
                # If the complement exists, return the indices of the
                # complement and the current number
                return [hash_map[target - num], i]

        # ---------------------------------------------------------
        # Time Complexity:
        # O(n) — The list is traversed once, and hash map operations
        #        (insert and lookup) are O(1) on average.
        #
        # Space Complexity:
        # O(n) — In the worst case, all elements are stored in the hash map.
        # ---------------------------------------------------------
