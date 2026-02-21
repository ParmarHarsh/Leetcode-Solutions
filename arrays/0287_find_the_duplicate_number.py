from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Finds the duplicate number in an array where:
        - The integers are in the range [1, n]
        - There is exactly one duplicate number
        - The duplicate may appear more than once

        This implementation uses Floyd’s Tortoise and Hare (cycle detection)
        algorithm by treating the array as a linked list where each index
        points to the value at that index.

        :param nums: List of integers containing one duplicate
        :return: The duplicate number
        """

        # Initialize slow and fast pointers at the start
        slow = nums[0]
        fast = nums[0]

        # Phase 1: Detect intersection point inside the cycle
        while True:
            # Move slow pointer one step
            slow = nums[slow]

            # Move fast pointer two steps
            fast = nums[nums[fast]]

            # If they meet, a cycle is detected
            if slow == fast:
                break

        # Phase 2: Find the entrance to the cycle (duplicate number)
        slow = nums[0]

        while slow != fast:
            # Move both pointers one step at a time
            slow = nums[slow]
            fast = nums[fast]

        # The meeting point is the duplicate number
        return slow

        # ---------------------------------------------------------
        # Time Complexity:
        # O(n) — Each pointer traverses the array at most a linear number of times.
        #
        # Space Complexity:
        # O(1) — Only constant extra space is used.
        # ---------------------------------------------------------
