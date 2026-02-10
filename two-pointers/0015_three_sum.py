from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Finds all unique triplets in the list that sum up to zero.

        The function sorts the input list and then uses a fixed pointer
        combined with a two-pointer approach to efficiently find valid
        triplets while avoiding duplicates.

        :param nums: List of integers
        :return: List of unique triplets that sum to zero
        """

        # List to store the resulting triplets
        result = []

        # Sort the list to enable the two-pointer technique
        nums.sort()

        # Iterate through the list, fixing one number at a time
        for i in range(len(nums) - 2):
            # Skip duplicate values to avoid repeating triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Initialize two pointers for the remaining part of the list
            j = i + 1
            k = len(nums) - 1

            # Move the two pointers toward each other
            while j < k:
                # Calculate the sum of the current triplet
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    # Valid triplet found, add it to the result
                    result.append([nums[i], nums[j], nums[k]])

                    # Move both pointers inward
                    j += 1
                    k -= 1

                    # Skip duplicate values for the second element
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # Skip duplicate values for the third element
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

                elif total < 0:
                    # If the sum is too small, move the left pointer right
                    j += 1
                else:
                    # If the sum is too large, move the right pointer left
                    k -= 1

        # Return all unique triplets found
        return result

        # ---------------------------------------------------------
        # Time Complexity:
        # O(n^2) — Sorting takes O(n log n), and the two-pointer
        #          traversal runs in O(n^2) in the worst case.
        #
        # Space Complexity:
        # O(1) (excluding output) — No extra space is used apart
        #        from the result list.
        # ---------------------------------------------------------
