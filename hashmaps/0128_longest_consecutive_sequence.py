from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Finds the length of the longest consecutive sequence of integers
        in an unsorted list.

        The algorithm uses a set for O(1) average-time lookups and only
        starts counting when the current number is the beginning of
        a sequence.

        :param nums: List of integers
        :return: Length of the longest consecutive sequence
        """

        # Convert the list to a set for fast membership checks
        my_set = set(nums)

        # Variable to store the longest consecutive sequence found
        longest = 0

        # Iterate through each number in the set
        for i in my_set:
            # Only start counting if 'i' is the beginning of a sequence
            # (i.e., i - 1 does not exist in the set)
            if i - 1 not in my_set:
                length = 0

                # Count how long the consecutive sequence continues
                while (i + length) in my_set:
                    length += 1

                # Update the longest sequence length if needed
                longest = max(longest, length)

        # Return the length of the longest consecutive sequence
        return longest

        # ---------------------------------------------------------
        # Time Complexity:
        # O(n) — Each number is visited at most twice (once in the loop
        #        and once in the while sequence check).
        #
        # Space Complexity:
        # O(n) — Extra space is used to store the set of numbers.
        # ---------------------------------------------------------
