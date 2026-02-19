from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Computes the area of the largest rectangle that can be formed
        within a histogram represented by the list `heights`.

        This implementation uses a monotonic increasing stack.
        Each element in the stack stores a tuple:
        (start_index, height).

        :param heights: List of bar heights in the histogram
        :return: Maximum rectangular area
        """

        # Variable to store the maximum rectangle area found
        max_area = 0

        # Stack to store tuples of (start_index, height)
        # Maintains increasing heights
        my_stack = []

        # Iterate through each bar in the histogram
        for i, h in enumerate(heights):
            # Initially, the start position is the current index
            start = i

            # While the current height is smaller than the height
            # at the top of the stack, calculate area
            while my_stack and my_stack[-1][1] > h:
                index, height = my_stack.pop()

                # Calculate area using the popped height
                max_area = max(max_area, height * (i - index))

                # Update start to the popped index
                start = index

            # Push the current bar with its appropriate start index
            my_stack.append((start, h))

        # Process any remaining bars in the stack
        for i, h in my_stack:
            # Calculate area extending to the end of the histogram
            max_area = max(max_area, h * (len(heights) - i))

        # Return the maximum area found
        return max_area

        # ---------------------------------------------------------
        # Time Complexity:
        # O(n) — Each bar is pushed and popped at most once.
        #
        # Space Complexity:
        # O(n) — The stack may contain up to n elements.
        # ---------------------------------------------------------
