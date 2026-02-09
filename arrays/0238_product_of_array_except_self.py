from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Returns an array where each element is the product of all elements
        in the input list except for the element at the same index.

        The solution handles cases involving zero values by first computing
        the total product of non-zero elements and counting how many zeros
        are present in the input.

        :param nums: List of integers
        :return: List where each index contains the product of all other elements
        """

        # Variable to store the product of all non-zero elements
        product = 1

        # List to store the final result
        result = []

        # Counter to track the number of zeros in the input list
        zero_cnt = 0

        # First pass: calculate the product of non-zero elements
        # and count the number of zeros
        for num in nums:
            if num != 0:
                product = product * num
            else:
                # Multiplying by 1 keeps the product unchanged
                product = product * 1
                zero_cnt = zero_cnt + 1

        # If there are more than one zero, all products will be zero
        if zero_cnt > 1:
            return [0] * len(nums)

        # Second pass: build the result array based on zero count
        for num in nums:
            if num == 0:
                # If the current number is zero, the product of others
                # is the product of all non-zero elements
                result.append(product)
            elif zero_cnt == 0:
                # If there are no zeros, divide total product by current number
                result.append(int(product / num))
            else:
                # If there is exactly one zero and current number is not zero
                result.append(0)

        # Return the final result list
        return result

        # ---------------------------------------------------------
        # Time Complexity:
        # O(n) — The list is traversed twice.
        #
        # Space Complexity:
        # O(n) — Extra space is used for the result list.
        # ---------------------------------------------------------
