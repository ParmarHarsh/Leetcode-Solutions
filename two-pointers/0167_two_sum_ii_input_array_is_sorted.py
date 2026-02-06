from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Finds two numbers in a sorted list that add up to a specific target
        and returns their 1-based indices.

        This method uses a two-pointer approach, starting from both ends
        of the list and moving inward based on the current sum.

        :param numbers: A sorted list of integers
        :param target: The target sum to find
        :return: A list containing the 1-based indices of the two numbers
        """

        # Initialize two pointers:
        # ptr_1 starts at the beginning of the list
        # ptr_2 starts at the end of the list
        ptr_1 = 0
        ptr_2 = len(numbers) - 1

        # Continue searching while the two pointers do not cross
        while ptr_1 < ptr_2:
            # Calculate the sum of the values at both pointers
            if numbers[ptr_1] + numbers[ptr_2] == target:
                # If the target sum is found, return 1-based indices
                return [ptr_1 + 1, ptr_2 + 1]

            elif numbers[ptr_1] + numbers[ptr_2] > target:
                # If the sum is too large, move the right pointer left
                ptr_2 = ptr_2 - 1

            elif numbers[ptr_1] + numbers[ptr_2] < target:
                # If the sum is too small, move the left pointer right
                ptr_1 = ptr_1 + 1

        # ---------------------------------------------------------
        # Time Complexity:
        # O(n) — Each pointer moves at most n steps across the list.
        #
        # Space Complexity:
        # O(1) — Only constant extra space is used.
        # ---------------------------------------------------------
