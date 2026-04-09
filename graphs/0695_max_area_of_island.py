from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Finds the maximum area of an island in a 2D grid.

        An island is a group of connected 1s (land) connected
        horizontally or vertically. This implementation uses
        Depth-First Search (DFS) to calculate the area of each island.

        :param grid: 2D list of integers (1 = land, 0 = water)
        :return: Maximum area of any island
        """

        # Set to track visited cells
        visited_cells = set()

        # Dimensions of the grid
        row_count = len(grid)
        col_count = len(grid[0])

        def get_area(row, col):
            """
            Recursively calculates the area of an island starting from (row, col).

            :param row: Row index
            :param col: Column index
            :return: Area of the island connected to this cell
            """

            # Base case:
            # - Out of bounds
            # - Already visited
            # - Water cell (0)
            if not (
                0 <= row < row_count
                and 0 <= col < col_count
                and (row, col) not in visited_cells
                and grid[row][col]
            ):
                return 0

            # Mark current cell as visited
            visited_cells.add((row, col))

            # Explore all 4 directions and sum up the area
            return (
                1
                + get_area(row + 1, col)
                + get_area(row - 1, col)
                + get_area(row, col + 1)
                + get_area(row, col - 1)
            )

        # Compute the maximum island area across all cells
        return max(
            get_area(row, col)
            for row in range(row_count)
            for col in range(col_count)
        )

        # ---------------------------------------------------------
        # Time Complexity:
        # O(m * n) — Each cell is visited at most once.
        #
        # Space Complexity:
        # O(m * n) — In the worst case, recursion stack and visited set
        # may store all cells.
        # ---------------------------------------------------------