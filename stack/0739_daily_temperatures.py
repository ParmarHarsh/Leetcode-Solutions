from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        For each day, calculates how many days must pass until
        a warmer temperature occurs. If no such day exists,
        the value remains 0.

        This implementation uses a monotonic stack to keep track
        of temperatures and their indices.

        :param temperatures: List of daily temperatures
        :return: List where each index contains the number of days
                 until a warmer temperature
        """

        # Initialize the result list with 0s
        # Default value is 0 if no warmer day exists
        result = [0] * len(temperatures)

        # Stack to store pairs of [temperature, index]
        # Maintains decreasing order of temperatures
        my_stack = []

        # Iterate through temperatures with index and value
        for i, j in enumerate(temperatures):
            # While the current temperature is higher than
            # the temperature at the top of the stack
            while my_stack and j > my_stack[-1][0]:
                # Pop the previous temperature and its index
                my_stack_j, my_stack_index = my_stack.pop()

                # Calculate the number of days waited
                result[my_stack_index] = (i - my_stack_index)

            # Push the current temperature and index onto the stack
            my_stack.append([j, i])

        # Return the result list
        return result

        # ---------------------------------------------------------
        # Time Complexity:
        # O(n) — Each temperature is pushed and popped at most once.
        #
        # Space Complexity:
        # O(n) — The stack may store up to n elements.
        # ---------------------------------------------------------