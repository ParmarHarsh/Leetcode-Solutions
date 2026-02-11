from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Computes how much rainwater can be trapped between bars
        represented by the elevation map.

        This implementation uses a two-pointer approach that keeps
        track of the maximum height seen so far from both the left
        and right sides.

        :param height: List of non-negative integers representing bar heights
        :return: Total units of trapped rainwater
        """

        # If the list is empty, no water can be trapped
        if not height:
            return 0

        # Left pointer starting at the beginning
        l = 0

        # Right pointer starting at the end
        r = len(height) - 1

        # Maximum height encountered so far from the left
        max_l = height[l]

        # Maximum height encountered so far from the right
        max_r = height[r]

        # Variable to store the total trapped water
        result = 0

        # Move pointers inward until they meet
        while l < r:
            # Decide which side to process based on smaller max boundary
            if max_l < max_r:
                l += 1

                # Update the maximum height from the left
                max_l = max(max_l, height[l])

                # Add trapped water at current position
                result += max_l - height[l]
            else:
                r -= 1

                # Update the maximum height from the right
                max_r = max(max_r, height[r])

                # Add trapped water at current position
                result += max_r - height[r]

        # Return the total trapped water
        return result

        # ---------------------------------------------------------
        # Time Complexity:
        # O(n) — Each index is processed at most once.
        #
        # Space Complexity:
        # O(1) — Only constant extra space is used.
        # ---------------------------------------------------------
