from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculates the maximum profit that can be achieved from a single
        buy-and-sell transaction given a list of stock prices.

        The algorithm tracks the minimum buying price seen so far and
        computes the profit for each subsequent price, updating the
        maximum profit accordingly.

        :param prices: List of stock prices where prices[i] is the price on day i
        :return: The maximum profit achievable
        """

        # Variable to store the maximum profit found so far
        max_profit = 0

        # Variable to store the profit for the current iteration
        current_profit = 0

        # Initialize the buying price as the first day's price
        buy = prices[0]

        # Iterate through the prices starting from the second day
        for i in range(1, len(prices)):
            # Calculate the profit if selling on the current day
            current_profit = prices[i] - buy

            # Update the maximum profit if the current profit is higher
            max_profit = max(max_profit, current_profit)

            # Update the buying price if a lower price is found
            if prices[i] < buy:
                buy = prices[i]

        # Return the maximum profit after checking all days
        return max_profit

        # ---------------------------------------------------------
        # Time Complexity:
        # O(n) — The list of prices is traversed once.
        #
        # Space Complexity:
        # O(1) — Only constant extra space is used.
        # ---------------------------------------------------------
