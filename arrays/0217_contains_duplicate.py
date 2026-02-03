from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Determines whether the input list contains any duplicate values.

        The function iterates through the list and keeps track of elements
        seen so far using a set. If an element is encountered more than once,
        the function immediately returns True.

        :param nums: List of integers to check for duplicates
        :return: True if any duplicate exists, otherwise False
        """

        # Set to store elements that have already been seen
        my_set = set()

        # Iterate through each number in the list
        for num in nums:
            # If the number is already in the set, a duplicate is found
            if num in my_set:
                return True
            else:
                # Otherwise, add the number to the set
                my_set.add(num)

        # If no duplicates were found after checking all elements
        return False

        # ---------------------------------------------------------
        # Time Complexity:
        # O(n) — Each element is processed once, and set lookups
        #        are O(1) on average.
        #
        # Space Complexity:
        # O(n) — In the worst case, all elements are stored in the set.
        # ---------------------------------------------------------
