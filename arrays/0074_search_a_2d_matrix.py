from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Searches for a target value in a 2D matrix.

        The matrix has the following properties:
        - Each row is sorted in ascending order.
        - The first element of each row is greater than the last element of the previous row.

        The algorithm performs:
        1. Binary search on rows to find the potential row containing the target.
        2. Binary search within that row to find the target.

        :param matrix: 2D list of integers
        :param target: Integer value to search for
        :return: True if target exists in the matrix, otherwise False
        """

        # Number of rows and columns
        rows = len(matrix)
        cols = len(matrix[0])

        # Binary search on rows
        r1 = 0
        r2 = rows - 1

        while r1 <= r2:
            # Find middle row
            midRow = (r1 + r2) // 2

            # If target is greater than the last element of midRow,
            # search in lower rows
            if target > matrix[midRow][-1]:
                r1 = midRow + 1

            # If target is smaller than the first element of midRow,
            # search in upper rows
            elif target < matrix[midRow][0]:
                r2 = midRow - 1

            else:
                # Target must be within this row
                break

        # If no valid row found, return False
        if not (r1 <= r2):
            return False

        # Perform binary search within the identified row
        row = midRow
        l = 0
        r = cols - 1

        while l <= r:
            # Find middle column
            m = (l + r) // 2

            # Adjust search range based on comparison
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                # Target found
                return True

        # Target not found in the matrix
        return False

        # ---------------------------------------------------------
        # Time Complexity:
        # O(log m + log n) — Binary search on rows and columns.
        #
        # Space Complexity:
        # O(1) — Only constant extra space is used.
        # ---------------------------------------------------------