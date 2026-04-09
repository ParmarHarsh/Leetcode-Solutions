from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Finds all coordinates in the grid where water can flow to both
        the Pacific and Atlantic oceans.

        Water can flow from a cell to another if the next cell's height
        is less than or equal to the current cell's height.

        This solution performs DFS from the borders of both oceans
        and finds cells reachable from each ocean.

        :param heights: 2D grid of heights
        :return: List of coordinates [r, c] that can reach both oceans
        """

        # Dimensions of the grid
        ROWS, COLS = len(heights), len(heights[0])

        # Sets to track cells reachable from Pacific and Atlantic oceans
        pac, atl = set(), set()

        def dfs(r, c, visited, prevHeight):
            """
            Depth-First Search to mark reachable cells.

            :param r: Current row
            :param c: Current column
            :param visited: Set tracking visited cells
            :param prevHeight: Height of the previous cell
            """

            # Base conditions:
            # - Out of bounds
            # - Already visited
            # - Current height is less than previous height (invalid flow)
            if (
                (r, c) in visited
                or r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or heights[r][c] < prevHeight
            ):
                return

            # Mark current cell as reachable
            visited.add((r, c))

            # Explore all 4 directions
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        # Run DFS from Pacific borders (top row and left column)
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        # Collect cells reachable from both oceans
        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res

        # ---------------------------------------------------------
        # Time Complexity:
        # O(m * n) — Each cell is visited at most twice (once per ocean).
        #
        # Space Complexity:
        # O(m * n) — Storage for visited sets and recursion stack.
        # ---------------------------------------------------------