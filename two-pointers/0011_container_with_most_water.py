from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Calculates the maximum amount of water that can be contained
        between two vertical lines represented by the input list.

        The function uses a two-pointer approach, starting from both
        ends of the list and moving inward to find the maximum possible area.

        :param height: List of non-negative integers representing line heights
        :return: Maximum area of water that can be contained
        """

        # Left pointer starting at the beginning of the list
        l = 0

        # Right pointer starting at the end of the list
        r = len(height) - 1

        # Variable to store the maximum area found
        max_area = 0

        # Variable to store the area calculated at each step
        current_area = 0

        # Move pointers toward each other while maintaining valid indices
        while l < r and r < len(height):
            # Calculate the current area using the shorter line
            current_area = min(height[l], height[r]) * (r - l)

            # Update the maximum area if the current area is larger
            max_area = max(current_area, max_area)

            # Move the pointer pointing to the shorter line
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        # Return the maximum area found
        return max_area

        # ---------------------------------------------------------
        # Time Complexity:
        # O(n) — Each pointer moves at most n steps.
        #
        # Space Complexity:
        # O(1) — Only constant extra space is used.
        # ---------------------------------------------------------
